from django.db import models

# Create your models here.


class logins(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=40)
