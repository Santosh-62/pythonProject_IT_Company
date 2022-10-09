from django.db import models

# Create your models here.
class user(models.Model):

    username=models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.username
