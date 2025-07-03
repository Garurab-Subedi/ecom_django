from django.db import models
import datetime

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Use Django's password hashing

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="", blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    qunatity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    order_date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)  # True for completed, False for pending
    payment_method = models.CharField(max_length=50, default="Cash on Delivery")
    total_amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.product
