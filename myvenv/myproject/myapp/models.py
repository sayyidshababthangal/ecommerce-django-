from django.db import models
from distutils.command import upload

# Create your models here.
class prodects(models.Model):
    prodect_image=models.ImageField(upload_to='prodect')
    prodect_name=models.CharField(max_length=100,null=True,blank=True)
    prodect_right=models.CharField(max_length=100,null=True,blank=True)
    prodect_offerright=models.CharField(max_length=100,null=True,blank=True)