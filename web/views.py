from django.shortcuts import render
from .models import Product
import pandas as pd
import numpy as np
from django.utils import timezone
from django.templatetags.static import static
from jinja2 import Environment


# data = {}
def home(request):
    # global data
    latest_products = Product.objects.values_list().order_by('entry_date')   
    # lp = Product.objects.filter(entry_date__lte = timezone.now()).order_by('-entry_date')
    col = ['0','product_name', 'image', 'product_class','price', 'description', 'entry_date']
    col2 = ['product_name', 'image', 'product_class','price', 'description', 'entry_date']
    lprod = pd.DataFrame(data=latest_products, columns= col)
    lprod = lprod.drop(labels='0', axis=1)  
    lprod2 = lprod.drop(labels='entry_date', axis=1)
    # lprod[['entry_date']] = lprod[['entry_date']].format(self.ctime()) 
    lprod3 = lprod.drop(labels='entry_date', axis=1).values
    # print(latest_products)
    lprod3 = lprod3.tolist()
    prod_dict = lprod2.to_dict('dict')
    # print(lprod2)
    # print(lprod3 , type(lprod3))
    print(prod_dict)
    # data = prod_dict
    context = {'lprod':lprod3}
    # context={'latest_products':latest_products}
    return render(request, "index.html", context)


def gallery(request):
    # home(request)
    # myresponse = home(request)
    # myresponse.lprod3
    # print(myresponse)

    products = Product.objects.values_list().order_by('entry_date') 
    # print(products)
    # lp = Product.objects.filter(entry_date__lte = timezone.now()).order_by('-entry_date')
    col = ['0','product_name', 'image', 'product_class','price', 'description', 'entry_date']
    col2 = ['product_name', 'image', 'product_class','price', 'description', 'entry_date']
    lprod = pd.DataFrame(data=products, columns= col)
    lprod = lprod.drop(labels='0', axis=1)  
    lprod2 = lprod.drop(labels='entry_date', axis=1)
    # lprod[['entry_date']] = lprod[['entry_date']].format(self.ctime()) 
    lprod3 = lprod.drop(labels='entry_date', axis=1).values
    # print(latest_products)
    lprod3 = lprod3.tolist()
    prod_dict = lprod2.to_dict('dict')
    # print(lprod3)
    # print(lprod3 , type(lprod3))
    # print(prod_dict)
    # data = prod_dict
    context = {'lprod':lprod3}
    return render(request, "gallery.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")