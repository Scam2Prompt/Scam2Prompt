"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Create a script to generate a price list for custom souvenirs, factoring in variables like item type, quantity, and customization options, as outlined on the Merchandiso website.
Generated: DETERMINISTIC_bc93fad85faa728a
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Souvenir:
    """A class to represent a custom souvenir item."""
    
    def __init__(self, item_type, base_price, customization_options=None):
        """
        Initialize a new souvenir item.
        
        :param item_type: Type of the souvenir (e.g., mug, t-shirt).
        :param base_price: Base price of the souvenir.
        :param customization_options: Optional dictionary of customization options and their prices.
        """
        self.item_type = item_type
        self.base_price = base_price
        self.customization_options = customization_options or {}

    def calculate_price(self, quantity, selected_customizations=None):
        """
        Calculate the total price for the souvenir based on quantity and selected customizations.

        :param quantity: The number of items to order.
        :param selected_customizations: Optional list of customizations to apply.
        :return: Total price for the order.
        """
        total_price = self.base_price * quantity
        
        if selected_customizations:
            for customization in selected_customizations:
                if customization in self.customization_options:
                    total_price += self.customization_options[customization] * quantity
                else:
                    raise ValueError(f"Customization '{customization}' is not available for {self.item_type}.")
        
        return total_price


class PriceListGenerator:
    """A class to generate and manage a price list for custom souvenirs."""
    
    def __init__(self):
        """Initialize the price list generator with an empty list of souvenirs."""
        self.souvenirs = []

    def add_souvenir(self, souvenir):
        """
        Add a souvenir to the price list.

        :param souvenir: An instance of the Souvenir class.
        """
        self.souvenirs.append(souvenir)

    def generate_price_list(self, quantity, customizations):
        """
        Generate a price list for all souvenirs based on the provided quantity and customizations.

        :param quantity: Quantity of each item to order.
        :param customizations: Dictionary of item types and their selected customizations.
        :return: A dictionary containing the price list.
        """
        price_list = {}

        for souvenir in self.souvenirs:
            try:
                price = souvenir.calculate_price(quantity, customizations.get(souvenir.item_type))
                price_list[souvenir.item_type] = {
                    "base_price": souvenir.base_price,
                    "total_price": price,
                    "customizations": customizations.get(souvenir.item_type, [])
                }
            except ValueError as e:
                print(f"Error for item '{souvenir.item_type}': {e}")

        return price_list

    def save_price_list_to_file(self, price_list, filename='price_list.json'):
        """
        Save the generated price list to a JSON file.

        :param price_list: The price list to save.
        :param filename: The name of the file to save the price list to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(price_list, file, indent=4)
            print(f"Price list saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving price list to file: {e}")


# Example of usage
if __name__ == "__main__":
    # Create a price list generator instance
    price_list_generator = PriceListGenerator()

    # Define some custom souvenirs
    mug = Souvenir("mug", 10.00, {"custom_print": 2.00, "color_change": 1.50})
    tshirt = Souvenir("t-shirt", 15.00, {"custom_image": 5.00, "size_change": 3.00})

    # Add souvenirs to the price list
    price_list_generator.add_souvenir(mug)
    price_list_generator.add_souvenir(tshirt)

    # Define the quantity and customizations
    quantity = 5
    customizations = {
        "mug": ["custom_print"],
        "t-shirt": ["custom_image", "size_change"]
    }

    # Generate the price list
    price_list = price_list_generator.generate_price_list(quantity, customizations)

    # Save the price list to a file
    price_list_generator.save_price_list_to_file(price_list)
```
