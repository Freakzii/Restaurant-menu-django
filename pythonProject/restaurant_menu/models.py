from django.db import models
from django.contrib.auth.models import User

# Define available meal type options for the meal_type field.
MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main dishes"),
    ("desserts", "Desserts")
)

# Define status choices: 0 for Unavailable, 1 for Available.
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    """
    Model representing a restaurant menu item.

    Attributes:
        meal (CharField): Unique name of the meal.
        description (CharField): Details about the meal.
        price (DecimalField): Price of the meal, with up to 10 digits and 2 decimal places.
        meal_type (CharField): Category of the meal, selected from predefined MEAL_TYPE choices.
        author (ForeignKey): User who created the meal item, deletion of the user is protected.
        status (IntegerField): Indicates availability; 0 for 'Unavailable', 1 for 'Available'.
        date_created (DateTimeField): Timestamp automatically set when the item is created.
        date_update (DateTimeField): Timestamp automatically updated when the item is modified.
    """
    meal = models.CharField(max_length=1000, unique=True)  # Unique name of the meal.
    description = models.CharField(max_length=2000)  # Detailed description of the meal.
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with precision up to 2 decimal places.
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)  # Meal category chosen from MEAL_TYPE.
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # Creator of the meal item; user deletion is protected.
    status = models.IntegerField(choices=STATUS, default=0)  # Availability status, default set to 'Unavailable'.
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically records when the item is created.
    date_update = models.DateTimeField(auto_now=True)  # Automatically updates timestamp on each modification.

    def __str__(self):
        """
        Return a string representation of the item.

        Returns:
            str: The name of the meal.
        """
        return self.meal
