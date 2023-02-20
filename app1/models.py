from django.db import models

# Create your models here.
class students(models.Model):
    stu_id = models.IntegerField(max_length=1000,blank=False,null=False)
    name = models.TextField(max_length=25)
    phone = models.IntegerField(null=True)
    age = models.IntegerField(help_text="your aadhar card age")
    summary = models.TextField(default="is a good student !!!")
    height = models.DecimalField(null=True,blank=True,decimal_places=1,max_digits=3)
