from django.db import models


class AllFieldsModel(models.Model):
    binary_field = models.BinaryField(null=True, default=None)
    boolean_field = models.BooleanField(null=True, default=None)
    char_field = models.CharField(max_length=254, null=True, default=None)
    date_field = models.DateField(null=True, default=None)
    datetime_field = models.DateTimeField(null=True, default=None)
    decimal_field = models.DecimalField(decimal_places=2, max_digits=4, null=True, default=None)
    duration_field = models.DurationField(null=True, default=None)
    float_field = models.FloatField(null=True, default=None)
    integer_field = models.IntegerField(null=True, default=None)
    biginteger_field = models.BigIntegerField(null=True, default=None)
    genericipadress_field = models.GenericIPAddressField(null=True, default=None)
    json_field = models.JSONField(null=True, default=None)
    positivebiginteger_field = models.PositiveBigIntegerField(null=True, default=None)
    positiveinteger_field = models.PositiveIntegerField(null=True, default=None)
    positivesmallinteger_field = models.PositiveSmallIntegerField(null=True, default=None)
    slug_field = models.SlugField(null=True, default=None)
    smallinteger_field = models.SmallIntegerField(null=True, default=None)
    text_field = models.TextField(null=True, default=None)
    time_field = models.TimeField(null=True, default=None)
    uuid_field = models.UUIDField(null=True, default=None)


class Continent(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    area = models.BigIntegerField()
    population = models.BigIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="countries")

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"


class River(models.Model):
    name = models.CharField(max_length=255, unique=True)
    discharge = models.IntegerField(null=True)
    length = models.IntegerField()
    countries = models.ManyToManyField(Country, related_name="rivers")

    def __str__(self):
        return f"{self.name}"


class Forest(models.Model):
    name = models.CharField(max_length=255, unique=True)
    area = models.BigIntegerField()
    countries = models.ManyToManyField(Country, related_name="forests")

    def __str__(self):
        return f"{self.name}"


class Mountain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    height = models.IntegerField()
    countries = models.ManyToManyField(Country, related_name="mountains")

    def __str__(self):
        return f"{self.name}"


class Disaster(models.Model):
    event = models.CharField(max_length=255)
    date = models.DateTimeField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="disasters")
    source = models.TextField()
    comment = models.TextField()

    def __str__(self):
        s = f"{self.event} - {self.country} - {self.date.strftime('%Y-%m-%d')}"
        return s
