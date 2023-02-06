import uuid
import django
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin



class MyAccountManager(BaseUserManager):

    def create_user(self, email, name , password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have Name")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self,name, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        print("SUPER USER CREATED")
        return user




class User(AbstractBaseUser , PermissionsMixin  ):  #  , PermissionsMixin
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255  )
    email = models.EmailField(max_length=255 , unique=True  , blank=False , null=False)  # blank false means that the field is required , null false means that the field is not nullable
    password = models.CharField(max_length=255  , blank=True , default="Abcde12345")

    date_joined = models.DateTimeField(default=django.utils.timezone.now)
    last_login = models.DateTimeField(blank=True , null=True , auto_now=True , verbose_name="last login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name","password" ]

    def __str__(self):
        return str(self.email)
