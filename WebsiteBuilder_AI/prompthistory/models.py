from django.db import models
from users.models import Users
# Create your models here.
class Prompts(models.Model):
    id=models.AutoField(primary_key=True)
    users=models.ForeignKey(Users, on_delete=models.CASCADE)
    Prompts=models.TextField(null=False)
    check_in=models.DateTimeField(null=False)
    check_out=models.DateTimeField(null=False)
    uploadfiles=models.TextField(null=False)