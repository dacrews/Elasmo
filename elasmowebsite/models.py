from django.db import models

class PorbBlue(models.Model):

    scientific_name = models.CharField("Scientific Name", max_length=255)
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    date = models.DateField("Date Collected", auto_now=True)
    collector = models.CharField("Collector", max_length=255)
    locality = models.CharField("Locality", max_length=255)
    sex = models.CharField("Sex", max_length=255)
    life_stage = models.CharField("Life Stage", max_length=255)
    length_meters = models.FloatField("Length")
    common_name = models.CharField("Common Name", max_length=255)

class Zambezi(models.Model):

    scientific_name = models.CharField("Scientific Name", max_length=255)
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    date = models.DateField("Date Collected", auto_now=True)
    collector = models.CharField("Collector", max_length=255)
    locality = models.CharField("Locality", max_length=255)
    common_name = models.CharField("Common Name", max_length=255)

class BlueShark(models.Model):
    scientific_name = models.CharField("Scientific Name", max_length=255)
    longitude = models.FloatField("Longitude")
    latitude = models.FloatField("Latitude")
    date = models.DateField("Date Collected", auto_now=True)
    collector = models.CharField("Collector", max_length=255)
    locality = models.CharField("Locality", max_length=255)
    sex = models.CharField("Sex", max_length=255)
    life_stage = models.CharField("Life Stage", max_length=255)
    weight_kg = models.FloatField("Weight")
    length_meters = models.FloatField("Length")
    common_name = models.CharField("Common Name", max_length=255)
