from django.contrib import admin
from .models import Fakultet, Fanlar, Yonalishlar, Talaba, Oqituvchilar, Baholar

@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display = ('id', 'fakultet')

@admin.register(Fanlar)
class FanAdmin(admin.ModelAdmin):
    list_display = ('id', 'fan')

@admin.register(Yonalishlar)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ('id', 'yonalish')

@admin.register(Talaba)
class talabaAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

@admin.register(Oqituvchilar)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']

@admin.register(Baholar)
class BahoAdmin(admin.ModelAdmin):
    list_display = ['id', 'semestr', 'ball', 'sana_kir']








