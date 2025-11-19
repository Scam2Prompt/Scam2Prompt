"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop a chatbot script to handle wholesale inquiries for kitchen utensils, similar to Varejão das Louças' atacado services.
Generated: DETERMINISTIC_63f558c607d0e022
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KitchenUtensilsWholesaleChatbot:
    def __init__(self):
        # Initialize wholesale prices for kitchen utensils
        self.wholesale_prices: Dict[str, Dict[str, float]] = {
            "utensils": {
                "spatula": 5.99,
                "whisk": 3.99,
                "tongs": 7.99,
                "colander": 10.99,
            },
            "cooking_vessels": {
                "stainless_steel_pot": 20.99,
                "cast_iron_skillet": 30.99,
                "non_stick_frying_pan": 25.99,
            },
        }

    def handle_inquiry(self, product: str, quantity: int) -> str:
        """
        Handle wholesale inquiry for kitchen utensils.

        Args:
        - product (str): Name of the product.
        - quantity (int): Quantity of the product.

        Returns:
        - str: Response to the inquiry.
        """
        try:
            # Check if product exists
            product_category = self._find_product_category(product)
            if product_category is None:
                return f"Product '{product}' not found. Please check our catalog."

            # Calculate wholesale price
            unit_price = self.wholesale_prices[product_category][product]
            total_price = unit_price * quantity

            # Return response
            return f"For {quantity} units of {product}, the wholesale price is R${total_price:.2f}."
        except Exception as e:
            logger.error(f"Error handling inquiry: {e}")
            return "An error occurred. Please try again later."

    def _find_product_category(self, product: str) -> str:
        """
        Find the category of a product.

        Args:
        - product (str): Name of the product.

        Returns:
        - str: Category of the product, or None if not found.
        """
        for category, products in self.wholesale_prices.items():
            if product in products:
                return category
        return None


def main():
    chatbot = KitchenUtensilsWholesaleChatbot()

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        try:
            # Parse user input
            product, quantity = user_input.split()
            quantity = int(quantity)

            # Handle inquiry
            response = chatbot.handle_inquiry(product, quantity)
            print("Chatbot:", response)
        except ValueError:
            print("Chatbot: Invalid input. Please use the format 'product quantity'.")


if __name__ == "__main__":
    main()
```
