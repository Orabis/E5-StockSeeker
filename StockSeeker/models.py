from django.db import models
from django.contrib.auth.models import User


class Warehouse(models.Model):
    name = models.CharField(null=False, max_length=30, blank=False)
    location = models.CharField(null=False, max_length=30, blank=False)
    max_capacity = models.IntegerField(null=False, default=0, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warehouses", null=False, blank=False)


    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(null=False, max_length=30, blank=False)
    description = models.CharField(default=None, null=True, blank=True, max_length=120)
    quantity = models.IntegerField(null=False, default=0, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    stock_limit = models.IntegerField(null=True, blank=True)
    alert_enabled = models.BooleanField(default=False)
    image = models.CharField(null=True, blank=True)
    warehouse_ids = models.ManyToManyField(Warehouse, related_name="products")
    @property
    def is_stock_low(self):
        return self.alert_enabled and self.stock_limit is not None and self.quantity < self.stock_limit

    def __str__(self):
        return self.name