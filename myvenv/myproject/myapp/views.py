from django.shortcuts import render
from .models import prodects

# Create your views here.
def index (request):
    return render(request,'index.html')
def home (request):
    prodects_base1={
        'prodect':prodects.objects.all()
    }
    return render(request,'home.html',prodects_base1)
def about (request):
    return render(request,'about.html')
def contact (request):
    return render(request,'contact.html')
def prodect (request):
    return render(request,'prodect_all_deatls.html')

