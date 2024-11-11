from django.contrib import admin

from .models import Product


@admin.register(Product)  # Первый способ регистрации модели
class ProductAdmin(admin.ModelAdmin):
    # Отображение информации на главной странице продукта в админке
    # Добавление многоточия в конце вместо длинного описания
    # list_display = "pk", "name", "description", "price", "discount"
    list_display = "pk", "name", "description_short", "price", "discount"
    # Добавление гиперссылки на название товара (было только на primary key)
    list_display_links = "pk", "name"

    # Добавление многоточия в конце вместо длинного описания
    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

# admin.site.register(Product, ProductAdmin) # Второй способ регистрации модели
