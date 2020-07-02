import json
import os
import sys

from django.apps import AppConfig, apps
from django.db import OperationalError



class GeographyConfig(AppConfig):
    name = 'geography'
    
    
    def ready(self):
        if "makemigrations" in sys.argv or "migrate" in sys.argv:
            return
        
        # Load needed models
        try:
            Continent = apps.get_model(app_label='geography', model_name='Continent')
            Region = apps.get_model(app_label='geography', model_name='Region')
            Country = apps.get_model(app_label='geography', model_name='Country')
            Forest = apps.get_model(app_label='geography', model_name='Forest')
            River = apps.get_model(app_label='geography', model_name='River')
            Mountain = apps.get_model(app_label='geography', model_name='Mountain')
        except OperationalError:
            # Migration not done yet
            return
        
        # Data already loaded
        if Forest.objects.all().count() == 8:
            return
        
        # Clear table in case previous loading was aborted
        Continent.objects.all().delete()
        Region.objects.all().delete()
        Country.objects.all().delete()
        Forest.objects.all().delete()
        River.objects.all().delete()
        Mountain.objects.all().delete()
        
        print("Loading geography data into database, this may take a few seconds...")
        directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(directory, "data.json")
        with open(path) as file:
            data = json.load(file)
        
        for c in data["continents"]:
            Continent.objects.create(name=c["name"])
        
        for r in data["regions"]:
            parent = Continent.objects.get(name=r["parent"])
            Region.objects.create(name=r["name"], continent=parent)
        
        for c in data["countries"]:
            parent = Region.objects.get(name=c["parent"])
            Country.objects.create(
                name=c["name"], area=c["area"], population=c["population"],
                region=parent
            )
        
        for r in data["rivers"]:
            countries = Country.objects.filter(name__in=r["countries"])
            River.objects.create(
                name=r["name"], discharge=r["discharge"], length=r["length"]
            ).countries.add(*countries)
        
        for m in data["mountains"]:
            countries = Country.objects.filter(name__in=m["countries"])
            Mountain.objects.create(
                name=m["name"], height=m["height"]
            ).countries.add(*countries)
        
        for f in data["forests"]:
            countries = Country.objects.filter(name__in=f["countries"])
            Forest.objects.create(
                name=f["name"], area=f["area"]
            ).countries.add(*countries)
