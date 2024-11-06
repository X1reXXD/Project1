from django.db import models

"""
Чтобы изменить версию миграции:
Terminal

python manage.py migrate shopapp ****

Где **** - необходимая существующая версия из папки migrations (прим. 0003)
"""


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
