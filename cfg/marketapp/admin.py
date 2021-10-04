from django.contrib import admin
from .models import Floors, Entrance, Apartmentnumber, Realty


admin.site.register(Floors)
admin.site.register(Entrance)
admin.site.register(Apartmentnumber)

@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('status', 'type', 'rooms', 'apartmentnumber', 'price')


