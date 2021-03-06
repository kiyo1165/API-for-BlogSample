from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from BlogApi import settings

def upload_avater_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['avaters', str(instance.user_profile.id) + str(".") + str(ext)])


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Emailアドレスは必須です。')
        user = self.model(email=self.normalize_email(email), name=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # デフォルトの入力をemailに変更
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name
