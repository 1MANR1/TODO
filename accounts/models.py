from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, username, first_name, password, **other_fields):

        if not username:
            raise ValueError(_('You must provide an User Name address'))

        user = self.model(username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, username, first_name, password, **other_fields):

        other_fields.setdefault('is_sadmin', True)
        other_fields.setdefault('is_superuser', True)
        
        if other_fields.get('is_admin') is not True:
           raise ValueError('Superuser must be assigned to is_admin=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, first_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    """
    New User class extended from AbstractBaseUser
    """
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_admin = models.BooleanField(default=True)
    
    is_superuser = models.BooleanField(default=True)

    objects = CustomAccountManager()

    # unique identifier we are using for our model
    USERNAME_FIELD = 'username'
    # required field
    REQUIRED_FIELDS  = ['first_name']

    def __str__(self):
        return self.username