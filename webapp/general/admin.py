from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from general import models

from .models import *


'''
admin.site.register(models.User, UserAdmin)
'''
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)