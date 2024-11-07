from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product, Order


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Smartphone', 999),
    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context=context)


"""
Для оптимизации использовать .select_related("user").prefetch_related("products") чтобы сразу загрузить
всех пользователей и все продукты вместо того чтобы подгружать их при каждом заказе.

database

select_related полезен, когда работаешь с отношениями «один к одному» и «один ко многим»,
а prefetch_related полезен при работе с отношениями «многие ко многим»
"""


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders-list.html', context=context)
