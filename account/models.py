import random
import string

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    phone_number = models.CharField(unique=True, max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.IntegerField(blank=True, null=True)
    invite_code = models.CharField(max_length=10, blank=True, null=True)
    activated_invite_code = models.CharField(max_length=10, blank=True, null=True)

    def generate_invite_code(self):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.invite_code = code
        self.save()

    USERNAME_FIELD = "phone_number"
