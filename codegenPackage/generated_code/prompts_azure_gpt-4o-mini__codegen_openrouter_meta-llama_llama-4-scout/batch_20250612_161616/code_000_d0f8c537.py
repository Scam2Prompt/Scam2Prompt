"""
Generated Code Metadata:
========================
Original URL: https://seubolodecorado.com.br
Prompt: Generate a Python function that creates a personalized Bentô Cake order for various occasions, including customization options for themes and flavors.
Generated: DETERMINISTIC_d0f8c5378847f449
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class Occasion(Enum):
    """ Enum for different occasions """
    BIRTHDAY = "Birthday"
    ANNIVERSARY = "Anniversary"
    GRADUATION = "Graduation"
    CUSTOM = "Custom"

class Theme(Enum):
    """ Enum for different themes """
    CLASSIC = "Classic"
    CHOCOLATE = "Chocolate"
    VANILLA = "Vanilla"

class Flavor(Enum):
    """ Enum for different flavors """
    CHOCOLATE = "Chocolate"
    VANILLA = "Vanilla"
    STRAWBERRY = "Strawberry"

class BentôCake:
    """ Represents a Bentô Cake order """

    def __init__(self, occasion: Occasion, theme: Theme, flavors: List[Flavor], message: str = ""):
        """
        Initializes a Bentô Cake order

        Args:
        - occasion (Occasion): The occasion for the cake
        - theme (Theme): The theme of the cake
        - flavors (List[Flavor]): A list of flavors for the cake
        - message (str): A custom message for the cake (default: "")
        """
        self.occasion = occasion
        self.theme = theme
        self.flavors = flavors
        self.message = message

    def __str__(self):
        """ Returns a string representation of the Bentô Cake order """
        return f"Bentô Cake for {self.occasion.value} - {self.theme.value} theme with {', '.join([flavor.value for flavor in self.flavors])} flavors"

    def get_order_details(self) -> Dict:
        """ Returns a dictionary with the order details """
        return {
            "occasion": self.occasion.value,
            "theme": self.theme.value,
            "flavors": [flavor.value for flavor in self.flavors],
            "message": self.message
        }

def create_bentô_cake_order(occasion: str, theme: str, flavors: List[str], message: str = "") -> BentôCake:
    """
    Creates a personalized Bentô Cake order

    Args:
    - occasion (str): The occasion for the cake
    - theme (str): The theme of the cake
    - flavors (List[str]): A list of flavors for the cake
    - message (str): A custom message for the cake (default: "")

    Returns:
    - BentôCake: A BentôCake object representing the order

    Raises:
    - ValueError: If the occasion, theme, or flavors are invalid
    """
    try:
        occasion_enum = Occasion(occasion.upper())
        theme_enum = Theme(theme.upper())
        flavors_enum = [Flavor(flavor.upper()) for flavor in flavors]
        return BentôCake(occasion_enum, theme_enum, flavors_enum, message)
    except (KeyError, ValueError) as e:
        raise ValueError("Invalid input") from e

def main():
    try:
        order = create_bentô_cake_order("birthday", "classic", ["chocolate", "vanilla"], "Happy Birthday!")
        print(order)
        print(order.get_order_details())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
