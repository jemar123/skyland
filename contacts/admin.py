from django.contrib import admin
from .models import Contact

class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'listing', 'listing_id', 'name', 'email', 'contact_date', 'user_id']
    list_display_links = ['id', 'listing', 'name']
    list_per_page = 25
    list_filter = ['name']
    search_fields = ['listing', 'listing_id', 'name', 'email', 'contact_date', 'user_id']

admin.site.register(Contact, AdminContact)
