# django-dummy-app

A simple django's app containing some models and some data for test purpose.

## Installation

Add `django_dummy_app` to `INSTALLED_APPS` in your settings

To load the data :

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata django_dummy_app/geographie_data.json.zip
```
