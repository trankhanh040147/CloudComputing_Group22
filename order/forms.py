from django import forms
from .models import Order
from order.models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']       

# class OrderForm(forms.Form):
#     first_name = forms.CharField(max_length=60, label='first name')
#     last_name = forms.CharField(max_length=60,label='last name')
#     email = forms.EmailField(label='email')
#     address = forms.CharField(max_length=150,label='address')
#     postal_code = forms.CharField(max_length=30,label='postal code')
#     city = forms.CharField(max_length=100,label='city')
#     created = forms.DateTimeField()
#     updated = forms.DateTimeField()
#     paid = forms.BooleanField()

#     def save(self, user):
#         Order.objects.create(customer = user,first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'],email=self.cleaned_data['email'],address=self.cleaned_data['address'],postal_code=self.cleaned_data['postal_code'],city=self.cleaned_data['city'])

  
