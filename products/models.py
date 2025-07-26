from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name="products"
    )
    
    def __str__(self):
        return self.name
