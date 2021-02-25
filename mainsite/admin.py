from django.contrib import admin
from .models import Plants


# Register your models here.
class PlantsAdmin(admin.ModelAdmin):
    list_display = ('fName', 'cName', 'url',)
    search_fields = ('cName',)
    ordering = ('fName',)


admin.site.register(Plants, PlantsAdmin)
