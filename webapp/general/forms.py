from allauth.account.forms import SignupForm
from django import forms


from .models import Product, User

class MyCustomSignupForm(SignupForm):
    is_supplier = forms.BooleanField(required=False,initial=False,label='I am a supplier')
    mobile_number = forms.CharField(required=False,label='Mobile number', widget= forms.TextInput(attrs={'placeholder':'Mobile number'}))

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.is_supplier = self.cleaned_data['is_supplier']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.save()
        return user


class AddProductForm(forms.ModelForm):
    class Meta:
        CHOICES= (
        ('Automotive','Automotive'),
        ('Electronics & Electrical','Electronics & Electrical'),
        ('Health & Personal Care','Health & Personal Care'),
        ('Toys & Games','Toys & Games'),
        ('Clothing','Clothing'),
        ('Sports & Fitness','Sports & Fitness'),
        ('Longlife Food Products','Longlife Food Products'),
        )
        model = Product
        exclude = ['supplier_details']
        widgets = {
            'p_category': forms.Select(choices=CHOICES),
            'p_desc': forms.Textarea(attrs={'cols': 70, 'rows': 10}),
        }
        labels = {
            'p_image': ('Product Images'),
            'p_name': ('Product Name'),
            'p_desc': ('Product Description'),
            'p_price': ('Product Price'),
            'min_quantity': ('Minimum Quantity'),
            'p_category': ('Product Category'),

        }
       


class EditProfileForm(forms.ModelForm):
    class Meta:
        
        model = User
        fields = ['first_name', 'last_name', 'business_name','business_bio','business_address','mobile_number','abn_number']
        widgets = {
            'business_bio': forms.Textarea(attrs={'cols': 70, 'rows': 10}),
            'business_name': forms.TextInput(),
            'business_address': forms.TextInput(),
        }
        labels = {
            'first_name': ('First Name'),
            'last_name': ('Last Name'),
            'business_name': ('Business Name'),
            'business_bio': ('Business Bio'),
            'business_address': ('Business Address'),
            'mobile_number': ('Contact Number'),
            'abn_number': ('ABN Number'),

        }
