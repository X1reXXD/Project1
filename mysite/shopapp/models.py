from django.contrib.auth.models import User
from django.db import models

"""
Чтобы изменить версию миграции:
Terminal

python manage.py migrate shopapp ****

Где **** - необходимая существующая версия из папки migrations (прим. 0003)
"""


class Product(models.Model):
    class Meta:
        # Сортировка продуктов по названию
        ordering = ["name"]

        # db_table = "tech_products"
        # verbose_name_plural = "products"

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    # Добавление многоточия в конце вместо длинного описания после 48 символов
    # (Перенес в админку тк больше эта функция нигде не нужна)
    # @property
    # def description_short(self) -> str:
    # if len(self.description) < 48:
    # return self.description
    # return self.description[:48] + "..."

    # Изменение представления объекта в административной панели
    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"
        # !r - репрезентативный вид текста (в кавычках)


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
