from django.contrib import admin

# Register your models here.

from .models import Stock, Sector

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'sector', 'market_cap', 'price')
    search_fields = ('symbol', 'name')

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
