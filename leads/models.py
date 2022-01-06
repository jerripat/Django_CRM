from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
