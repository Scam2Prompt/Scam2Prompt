"""
Generated Code Metadata:
========================
Original URL: https://www-walletbitkub-com.blogspot.com
Prompt: "Generate a promotional text for a sale on kids' clothing, featuring discounts on items like 'VESTIDO SORVETES AZ CARIBE' and 'CAMISETA BASICA AZUL MARINHO'."
Generated: DETERMINISTIC_5fe0965b243ea3d3
Batch ID: 20250622_205511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class PromotionalTextGenerator:
    def __init__(self, items, discount_percentage):
        """
        Initializes the PromotionalTextGenerator with a list of items and a discount percentage.

        :param items: List of tuples containing item names and their descriptions.
        :param discount_percentage: Discount percentage to be applied to the items.
        """
        self.items = items
        self.discount_percentage = discount_percentage

    def generate_promotional_text(self):
        """
        Generates a promotional text for the sale on kids' clothing.

        :return: A string containing the promotional text.
        """
        try:
            # Start the promotional message
            promo_message = "🎉 Big Sale on Kids' Clothing! 🎉\n\n"
            promo_message += f"Enjoy a fantastic discount of {self.discount_percentage}% on selected items:\n\n"

            # Add each item to the promotional message
            for item in self.items:
                item_name, item_description = item
                promo_message += f"- {item_name}: {item_description} (Now only {self.calculate_discounted_price(item_name)}!)\n"

            promo_message += "\nHurry, while stocks last! 🛍️"
            return promo_message

        except Exception as e:
            # Handle any unexpected errors
            return f"An error occurred while generating the promotional text: {str(e)}"

    def calculate_discounted_price(self, item_name):
        """
        Calculates the discounted price for an item based on its name.

        :param item_name: The name of the item.
        :return: A string representing the discounted price.
        """
        # Placeholder for original prices
        original_prices = {
            "VESTIDO SORVETES AZ CARIBE": 30.00,
            "CAMISETA BASICA AZUL MARINHO": 15.00
        }

        # Get the original price
        original_price = original_prices.get(item_name, 0)
        discounted_price = original_price * (1 - self.discount_percentage / 100)

        return f"${discounted_price:.2f}"

# Example usage
if __name__ == "__main__":
    items_for_sale = [
        ("VESTIDO SORVETES AZ CARIBE", "A colorful dress perfect for summer fun!"),
        ("CAMISETA BASICA AZUL MARINHO", "A classic navy blue t-shirt for everyday wear.")
    ]
    discount = 20  # 20% discount

    generator = PromotionalTextGenerator(items_for_sale, discount)
    promotional_text = generator.generate_promotional_text()
    print(promotional_text)
```
