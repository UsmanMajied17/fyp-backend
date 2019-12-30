from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.


class User(User):
    phone = PhoneField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
