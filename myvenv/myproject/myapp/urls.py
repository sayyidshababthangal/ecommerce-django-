from django.urls import path,include
from .import views

urlpatterns =[
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('prodect',views.prodect,name='prodect'),
]