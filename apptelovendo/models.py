from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    rut = models.CharField(max_length=20, unique=True)
    nombre_completo= models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.AutoField
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut']

    def __str__(self):
        return self.email

