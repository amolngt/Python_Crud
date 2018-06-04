from django.db import models

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return (self.product_name)
