from django.db import models
from django.core import validators
from decimal import Decimal

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Advertisement(models.Model):

    subject = models.CharField(max_length=300)
    text = models.TextField()
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(limit_value=Decimal('0.01'))
        ],
        error_messages={
            'min_value': 'Cost can\'t be less than 0.01'
        }
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        return self.subject