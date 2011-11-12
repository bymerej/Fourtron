from django.db import models

class User(models.Model):
  email = models.CharField(max_length=256)
  created = models.DateTimeField()
  foursquareUserId = models.CharField(max_length=64)
  firstName = models.CharField(max_length=32)
  lastName = models.CharField(max_length=32)
  homeCity = models.CharField(max_length=64)

