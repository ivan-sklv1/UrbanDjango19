from django.contrib import admin
from task1.models import Buyer, Game


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('cost',)
    list_display = ('title', 'cost',)
    search_fields = ('title',)
    list_per_page = 20
