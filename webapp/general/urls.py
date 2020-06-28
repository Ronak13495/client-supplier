
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome', views.welcome, name='welcome'),
    path('success', views.saveproduct, name='success'),
    path('cart', views.cart, name='cart'),
    path('addcart', views.addcart, name='addcart'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('delete', views.delete, name='delete'),
]
