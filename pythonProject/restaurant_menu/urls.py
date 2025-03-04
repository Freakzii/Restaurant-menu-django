from django.urls import path
from . import views

# Define URL patterns for the restaurant menu app.
urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # Homepage displaying the list of menu items.
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),  # Detail view for a specific menu item.
]
