from django.shortcuts import render, redirect
from django.views.generic import TemplateView 
from django.views import View 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms 
from django.contrib import messages


# Create your views here.

#def homePageView(request): 
#    return HttpResponse('Hello World!') 

class homePageView(TemplateView): 
    template_name = '../templates/pages/home.html'
    
class aboutPageView(TemplateView): 
    template_name = '../templates/pages/about.html' 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Your Name", 
        }) 
        return context 

class contactPageView(TemplateView): 
    template_name = '../templates/pages/about.html' 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "Contactame", 
            "subtitle": "Sobre mi", 
            "description": "lgiraldo1109@gmail.com and +57 322 6724582",
            "direccion": "", 
            "author": "Cra 44 # 17 c sur 40", 
        }) 
        return context 

class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":150}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone","price":55}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast","price":200}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses","price":8} 
    ] 

class ProductIndexView(View): 
    template_name = '../templates/pages/products/index.html' 
    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 
        return render(request, self.template_name, viewData) 


class ProductShowView(View): 
    template_name = '../templates/pages/products/show.html' 
    def get(self, request, id): 
        viewData = {} 
        try:
            product = Product.products[int(id)-1]
        except IndexError:
            return HttpResponseRedirect(reverse('home'))
        product = Product.products[int(id)-1] 
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
        viewData["price"]=product["price"]
        return render(request, self.template_name, viewData) 

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return price


class ProductCreateView(View): 
    template_name = '../templates/pages/products/create.html' 

    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["title"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 

    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid():
            return HttpResponseRedirect('/products/create/sucess')
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)

class ProductSucessView(TemplateView):
    template_name = '../templates/pages/products/sucess.html' 
    
    # def get_context_data(self, **kwargs): 
    #     context = super().get_context_data(**kwargs) 
    #     context.update({ 
    #         "title": "About us - Online Store", 
    #         "subtitle": "About us", 
    #         "description": "This is an about page ...", 
    #         "author": "Developed by: Your Name", 
    #     }) 
    #     return render(request, self.template_name)