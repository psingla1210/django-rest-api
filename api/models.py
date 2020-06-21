from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class TwistedUserManager(BaseUserManager):
    def create_user(self, email, name, password='none'):
        if not email:
            raise ValueError('Users must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class TwistedUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=256, unique=True, verbose_name='email address')
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = TwistedUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        # verbose_name_plural = 'users'

    # verbose_name = 'users'
