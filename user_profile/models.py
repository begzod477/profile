from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    telegram = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.username} Profile'
