from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=50)
    is_blocked = models.BooleanField(default=False)

    rigistered_at = models.DateTimeField()


class Backend(BaseBackend):
    def authenticate(self, request: HttpRequest, number: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            user = User.objects.get(number=number, password=password)
        except User.DoesNotExist:
            return None

        return user
    
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user