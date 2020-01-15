from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser, Product


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
