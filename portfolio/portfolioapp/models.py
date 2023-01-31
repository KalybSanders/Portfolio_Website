from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName = models.CharField(max_length=100, default="default")
    lastName = models.CharField(max_length=100, default="default")
    phoneNumber = models.CharField(max_length=100, default="default")
    email = models.CharField(max_length=100, default="default")
    message = models.CharField(max_length=10000, default="default")
