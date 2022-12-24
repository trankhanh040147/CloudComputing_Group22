from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomerUser(AbstractUser):
    name = AbstractUser.username
    phone_number = models.CharField(default='', max_length=20)
    address = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name

