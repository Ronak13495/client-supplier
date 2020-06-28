from django.shortcuts import render
from .models import User, Product, Order, OrderItem, CartItem
from django.http import HttpResponse
from django.contrib import messages
from .forms import AddProductForm, EditProfileForm
from django.db.models import Q

from django.http import JsonResponse
import json 

from django.contrib.auth.decorators import login_required

# Create your views here.




def home(request):
    return render(request,'home.html')

def dashboard(request):

    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            message = "Profile updated successfully!"
            context = {'message':message}
            return render(request,'success.html',context)
            

    user = request.user
    form = EditProfileForm(request.POST or None)
    context = {'form':form,'user':user}
    return render(request,'dashboard.html',context)

def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(p_name__icontains=query) | Q(p_desc__icontains=query)

            results= Product.objects.filter(lookups).distinct()

            context={'results': results}

            print(results)
            return render(request, 'search.html', context)

        else:
            return render(request, 'welcome.html')

    else:
        return render(request, 'welcome.html')


def cart(request):

    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {'items':items}
    return render(request,'cart.html', context)


def addcart(request):

    data = json.loads(request.body)
    product = data['productId']
    action = data['action']
    user = request.user

    addToCart= [product,user]        
    addToCart = CartItem(product=product, user=user)
    addToCart.save()


    '''
    product = Product.objects.get(id=productId)

    orders, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(orders=orders, item=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    '''


    return JsonResponse('Item was added', safe=False)

def delete(request):
    user = request.user.id
   
    try:
        u = User.objects.get(id=user)
        u.is_active = False
        u.save()
    except User.DoesNotExist:
        return render(request,'home.html')
    except Exception as e:
        return render(request,'home.html')
    



def saveproduct(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST , request.FILES)
        if form.is_valid():
            addprod = form.save(commit=False)
            addprod.supplier_details = request.user
            addprod.save()

            return render(request,'success.html')
            



@login_required
def welcome(request):
    user = request.user
    form = AddProductForm(request.POST or None, request.FILES or None)

    context = {'user':user,'form':form}
    if user.is_supplier:
        return render(request,'addprod.html', context)

    else:
        products = Product.objects.all()
        context = {'products':products}
        return render(request,'listing.html',context)