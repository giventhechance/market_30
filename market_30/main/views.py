from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from .forms import CategoryForm, ProductForm
from .models import Category, Product, Shop


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'main_page.html', context)

def category_sort(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories=id)
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'categories_products.html', context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    shops = product.shop_set.all()
    products_in_shop = Product.objects.filter(shop__name='Гиппо')
    print(products_in_shop, 'все продукты конкретного магазина (Гиппо)')
    shops_for_products = Shop.objects.filter(products__title='BMW')
    print(shops_for_products, 'магазины с BMW')
    print(shops_for_products.query)
    context = {
        'product': product,
        'shops': shops
    }
    return render(request, 'product_detail.html', context)

def less_forms(request):

    categories = Category.objects.all()
    products = Product.objects.all()
    form = CategoryForm()
    context = {
        'categories': categories,
        'products': products,
        'form': form
    }
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'less_forms.html', context)

def category_form(request):
    print(request.POST, 'category_form')
    return redirect('main:less_forms')

def form_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        else:
            print(form.errors)
    context = {
        'form': form
    }

    return render(request, 'form_error.html', context)


def form_model(request):
    form = ProductForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'model_form.html', context)




