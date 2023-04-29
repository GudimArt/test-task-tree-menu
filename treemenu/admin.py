from django.contrib import admin
from .models import Menu, MenuItem
from .forms import MenuForm, MenuItemForm

class MenuAdmin(admin.ModelAdmin):
    form = MenuForm

class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)