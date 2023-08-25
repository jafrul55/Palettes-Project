from django.contrib import admin
from .models import Color, Palette, Favorite


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['value']


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ['creator', 'name']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'palette']
