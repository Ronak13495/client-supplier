from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    business_bio = models.TextField(max_length=500, blank=True)
    business_name = models.TextField(max_length=500, blank=True)
    business_address = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length=30, blank=True)
    abn_number = models.CharField(max_length=30, blank=True)
    acn_number = models.CharField(max_length=30, blank=True)
    landline_number = models.CharField(max_length=30, blank=True)   
    profile_photo = models.ImageField(upload_to='static/images')
    is_supplier = models.BooleanField(default=False)


class Product(models.Model):
    p_image =  models.FileField(upload_to='images/products')
    p_name = models.CharField(max_length=100, blank=True)
    p_desc = models.CharField(max_length=500, blank=True)
    p_price = models.IntegerField()
    min_quantity = models.IntegerField()
    p_category = models.CharField(max_length=100, blank=True)
    supplier_details = models.ForeignKey('User', on_delete=models.CASCADE,default=None) 


class CartItem(models.Model):
    product = models.CharField(max_length=500, blank=True)
    user = models.CharField(max_length=500, blank=True)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
 
class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0,  null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)