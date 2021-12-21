from django.db import models

# Create your models here.

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=50)
    price = models.IntegerField()
    vendor = models.CharField(max_length=50,)
    quantity = models.IntegerField()
    waranty = models.IntegerField()

    def __str__(self):

        return self.productname