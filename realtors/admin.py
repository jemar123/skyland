from django.contrib import admin
from .models import Realtor

class AdminRealtor(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Realtor, AdminRealtor)