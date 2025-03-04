from django.apps import AppConfig

class ResturantMenuConfig(AppConfig):
    """
    App configuration for the restaurant_menu application.

    This class defines the default settings for the app,
    including the default field type for primary keys and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'  # Use BigAutoField for model primary keys.
    name = 'restaurant_menu'  # The full Python path to the app, used by Django for app discovery.
