from django.db import models
from django.forms import CharField
class User(models.Model):
    name        =   models.CharField(max_length=100)
    email       =   models.CharField(max_length=100)
    password    =   models.CharField(max_length=100)
    class Meta:
        db_table="users"
