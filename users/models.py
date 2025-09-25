from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """ Модель пользователя с электронной почтой в качестве поля для авторизации """

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        ** NULLABLE,
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        ** NULLABLE,
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
