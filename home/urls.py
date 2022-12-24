
from django import views
from django.urls import path
from . import views

##t
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Home'

urlpatterns = [
    path('',views.HomePage, name='homepage'),
    path('store/',views.Store.as_view(),name='store'),
    path('store/<slug:category_slug>/',views.Store.as_view(),name='store_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>',views.product_detail, name = 'product_detail' ),
    path('search/', views.search, name='search'),
    path('login/',views.loginUser.as_view(),name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),
    path('checkout/',views.checkOut, name='checkout'),
    path('intro/', views.IntroPage, name = 'intro'), #loc code
    path("contact/", views.conTact, name="contact"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)