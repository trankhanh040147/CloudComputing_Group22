from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from product.models import Product as product_models
from product.models import Category, Comment   
from .form import RegistrationForm, LoginForm, CommentForm
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db.models import Q
from cart.form import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth



def HomePage(request):
    return render(request, 'home/home.html') 

def IntroPage(request):
    return render(request, 'home/info.html')


class Store(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, category_slug = None):
        category_list = Category.objects.all().filter()
        user = request.user
        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            product_list = product_models.objects.all().filter(category=category)
        else:
            product_list = product_models.objects.filter()
            category = None
  
        context = {
        'category':category,
		'categories': category_list,
		'product_list': product_list,
        'user':user,
	    }
        return render(request, 'home/store.html',context)


@decorators.login_required(login_url = '/login/')

def product_detail(request, category_slug, product_slug):
    category =  get_object_or_404(Category, slug=category_slug)
    product  =  get_object_or_404(product_models, slug=product_slug)
    cart_product_form = CartAddProductForm()

  
    cmt = CommentForm(request.POST or None)
    if  request.method == "POST":
        if cmt.is_valid():
            comm = cmt.save(commit= False)
            comm.user = request.user
            comm.post = product
            comm.save()
            return redirect(product.get_url())

    list_Comment = Comment.objects.all().filter(post = product).order_by("-date_added")
    #
    context = {
        'category':category,
        'product':product,
        'cart_product_form': cart_product_form,
      
        'cmt': cmt,
        'list_Comments': list_Comment,
        
    }
    return render(request, 'home/product_detail.html', context=context)


def search(request):
    if 'q' in request.GET:
        q = request.GET.get('q')
        category_list = Category.objects.all().filter()
        products = product_models.objects.order_by('-title').filter(Q(title__icontains=q) | Q(description__icontains=q))
        product_count = products.count()

    context = {
        'product_list': products,
        'q': q,
        'product_count': product_count,
        'categories': category_list,
    }
    return render(request, 'home/search.html', context=context)





def get_home(request):
    return render(request,'Fanpage/home.html')

def register(request):

    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # email=request.POST.get('email')
            # name=request.POST.get('username')
            # password=request.POST.get('password1')
            # message=("Hello user "+"'"+name+"'"+"\n"
            #          +"Your password is : "+"'"+password+"'"
            #          +"\n"+"Access to this link to continue log in: https://do-an-dien-toan-dam-may-git-crt-20110233-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/login/"
            #         )

            # send_mail('Verified mail from cửa hàng nông sản',
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False
            # )

            #----------------------------------------------
            return render(request,'home/home.html')
    return render(request,'login-out-register/register.html',{'form':form})


class loginUser(View):
    def get(selt,request):
        lf=LoginForm
        return render(request,'login-out-register/login.html',{'lf':lf})
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            category_list = Category.objects.all().filter()
            product_list = product_models.objects.filter()
            context = {
		        'categories': category_list,
		        'product_list': product_list,
	        }
            return render(request,'home/store.html', context)
        else:
            return HttpResponse('login failed')


@login_required(login_url="login") # Hàm Django hỗ trợ để chắc chắn phải login trước rồi mới logout được
def logoutUser(request):
    auth.logout(request)
    # messages.success(request=request, message="You are logged out!")
    return render(request,'home/home.html')

def checkOut(request):
    return render(request, 'home/checkout.html')


def conTact(request):
    return render(request,'home/contact.html')