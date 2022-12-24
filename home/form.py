

import re
from django import forms
from user.models import CustomerUser
from product.models import Comment, Product #loc code
from django.core.exceptions import ObjectDoesNotExist


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price','category','active','images']

## quan
class RegistrationForm(forms.Form):
    username=forms.CharField(label='Tài khoản',max_length=30)
    email=forms.EmailField(label='Email',widget=forms.EmailInput())
    password1=forms.CharField(label='Mật khẩu',widget=forms.PasswordInput())
    password2=forms.CharField(label='Nhập lại mật khẩu',widget=forms.PasswordInput())
    collocation=forms.CharField(label='Địa chỉ:',max_length=120)
    phoneNumber=forms.CharField(label='Số điện thoại',max_length=20)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ vì không trùng nhau")
    def clean_username(self):
        username=self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            CustomerUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
        CustomerUser.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'],phone_number=self.cleaned_data['phoneNumber'],address=self.cleaned_data['collocation'])


##quan
class LoginForm(forms.Form):
    username=forms.CharField( max_length=50)
    password=forms.CharField( max_length=50,widget=forms.PasswordInput)


#Loc
class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Viết bình luận...",
                "class": "form-control",
            }
        ),
        label="",
    )

    class Meta: 
        model = Comment
        exclude = ("post", "user",)

        