from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing menu items.

    This class customises the Django admin for the Item model by:
    - Displaying the 'meal' and 'status' fields in the list view.
    - Adding a filter sidebar for the 'status' field.
    - Enabling search functionality for the 'meal' and 'description' fields.
    """
    list_display = ("meal", "status")         # Columns to display in the admin list view.
    list_filter = ("status",)                 # Filter options for the admin list view.
    search_fields = ("meal", "description")   # Fields to be searched in the admin.

# Register the Item model with the custom admin configuration.
admin.site.register(Item, MenuItemAdmin)
