from django.db import models

# Create your models here.
class Users(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.TextField(null=False)
    lastname=models.TextField(null=False)
    email=models.TextField(null=False,unique=True)
    password=models.TextField(null=False)
    country=models.TextField(null=False)
