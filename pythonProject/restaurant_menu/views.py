from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

class MenuList(generic.ListView):
    """
    View for displaying a list of menu items.

    Attributes:
        template_name (str): The template used for rendering the menu list.
        model (Item): The model associated with this view.
    """

    template_name = "index.html"
    model = Item  # Specify the model explicitly

    def get_queryset(self):
        """
        Return the queryset of menu items ordered by date created (most recent first).
        """
        return Item.objects.order_by("-date_created")

    def get_context_data(self, **kwargs):
        """
        Add additional context to the template, including meal types.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: Context data including meal types.
        """
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE  # Include meal type choices in the context.
        return context

class MenuItemDetail(generic.DetailView):
    """
    View for displaying details of a single menu item.

    Attributes:
        model (Item): The model associated with this view.
        template_name (str): The template used for rendering the item detail.
    """
    model = Item
    template_name = "menu_item_detail.html"
