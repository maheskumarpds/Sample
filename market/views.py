from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Stock

def home(request):
    return render(request, 'market/home.html')

def screener(request):
    stocks = Stock.objects.all()
    return render(request, 'market/screener.html', {'stocks': stocks})
