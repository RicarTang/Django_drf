from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=18)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "users"
