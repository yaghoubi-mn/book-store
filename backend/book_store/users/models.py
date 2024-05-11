from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=50)
    is_blocked = models.BooleanField(default=False)
    permisions = models.CharField(max_length=100,  default="0000000000") # 0 and 1 for permisions

    rigistered_at = models.DateTimeField()

    def have_permision(self, permision: str):
        match permision:
            case "create product":
                return bool(self.permisions[0])
            case "delete product":
                return bool(self.permisions[1])
            case "block user":
                return bool(self.permisions[2])
            case "create admin":
                return bool(self.permisions[3])
        raise ValueError("permision not found")

    def set_permision(self, permision: str, is_remove=False):
        """
        if is_remove == True: this will remove the permision"""
        
        p = "1" if not is_remove else "0"

        match permision:
            case "create product":
                self.permisions[0] = p
            case "delete product":
                self.permisions[1] = p
            case "block user":
                self.permisions[2] = p
            case "create admin":
                self.permisions[3] = p
        raise ValueError("permision not found")
            


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
    
class UserManager(BaseUserManager):
    def create_user(self, number, name, password):
        """
        if number exists already, it raises ValueError
        """
        user = User()
        user.number = number
        user.name = name
        user.password = make_password(password) # todo: check
        result = User.objects.get(number=number)
        if result != None:
            raise ValueError("number exist already")
        user.save()

