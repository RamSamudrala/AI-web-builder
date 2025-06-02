from django.db import models
from users.models import Users
# Create your models here.
class Feedback(models.Model):
    id=models.AutoField(primary_key=True)
    users=models.ForeignKey(Users,on_delete=models.CASCADE)
    firstname=models.TextField(null=False)
    email=models.TextField(null=False)
    feedback=models.TextField(null=False)

