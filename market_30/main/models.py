from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name

