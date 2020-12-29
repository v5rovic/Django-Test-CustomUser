from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import fields


class CustomUser(AbstractUser):
    empID = models.CharField(max_length=16, null=True, blank=True, unique=True)





