from django.db import models

# Create your models here.
class professors(models.Model):
    prof_id = models.IntegerField()
    name = models.TextField()
    phone = models.IntegerField()
    age = models.IntegerField()