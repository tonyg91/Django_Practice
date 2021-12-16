from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=100)
    
class Journals(models.Model):
    brand = models.CharField(max_length=100)
    paperweight = models.CharField(max_length=100)
    sizes = models.CharField(max_length=100)
    pages = models.IntegerField(default=3)
    
class Supply(models.Model):
    brandName: models.CharField(max_length=100)
    type: models.CharField(max_length=100)
    ink: models.CharField(max_length=100)