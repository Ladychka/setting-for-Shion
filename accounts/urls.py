from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product_details/<int:ProductAssignmentID>/', views.product_details, name='product_details'),
    path('main/', views.main, name='main'), 
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/<int:blogID>/', views.blog_details, name='blog_details'),
    path('about/', views.about, name='about'),


] 