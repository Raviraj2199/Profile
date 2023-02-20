from django.db import models

# Create your models here.
class stu_fee(models.Model):
    stu_id = models.IntegerField()
    fee_status = models.TextField()
    fee = models.IntegerField()
    