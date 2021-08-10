from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Добавление дополнительных полей."""
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE = (
        (ADMIN, ADMIN),
        (MODERATOR, MODERATOR),
        (USER, USER)
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE,
        default=USER
    )
    email = models.EmailField(unique=True)
    bio = models.CharField(
        blank=True,
        max_length=255
    )

    @property
    def is_admin(self):
        return self.is_superuser or self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        return self.role == self.USER
