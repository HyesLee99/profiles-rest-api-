from django.db import models
#django official documentation
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # encryption
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password): # admin
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password) # self is automatically passed in when called in a class

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #by default always required
    REQUIRED_FIELDS = ['name'] # additional required ones

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self): # recommend for all django bc it is good to specity how to represent "self"
        """Return string representation of our user"""
        return self.email
