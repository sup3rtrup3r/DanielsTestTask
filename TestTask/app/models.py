from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    pass


class Product(models.Model):
    CATEGORY_CHOICES = [
        (1, _('Books')),
        (2, _('Movies')),
    ]

    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.pk}' + '-' + self.name + '-' + f'{self.category}' + '-' + f'{self.price}'
