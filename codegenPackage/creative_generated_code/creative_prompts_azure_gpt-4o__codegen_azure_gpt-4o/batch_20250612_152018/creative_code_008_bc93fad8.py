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

class SouvenirPricing:
    def __init__(self):
        """
        Initialize the pricing details. These values can be adjusted based on the Merchandiso website details.
        """
        # Base prices for different item types
        self.base_prices = {
            "mug": 5.00,
            "tshirt": 10.00,
            "keychain": 2.50,
            "cap": 8.00,
        }
        
        # Customization options and their costs
        self.customization_prices = {
            "text": 1.50,  # Adding custom text
            "image": 3.00, # Adding a custom image
            "color_change": 2.00 # Changing the base color
        }
    
    def calculate_price(self, item_type, quantity, customizations):
        """
        Calculate the total price for a souvenir order.
        
        Args:
            item_type (str): Type of the souvenir (e.g., 'mug', 'tshirt').
            quantity (int): Number of items ordered.
            customizations (list[str]): List of customization options (e.g., ['text', 'image']).
        
        Returns:
            float: Total price for the order.
        """
        # Validate item type
        if item_type not in self.base_prices:
            raise ValueError(f"Invalid item type: {item_type}")
        
        # Validate customizations
        for customization in customizations:
            if customization not in self.customization_prices:
                raise ValueError(f"Invalid customization option: {customization}")
        
        # Calculate base price
        base_price = self.base_prices[item_type]
        
        # Add customization costs
        customization_cost = sum(self.customization_prices[c] for c in customizations)
        
        # Calculate total price for the order
        total_price = (base_price + customization_cost) * quantity
        
        return round(total_price, 2)

def main():
    """
    Main function to handle user input and generate a price list.
    """
    print("Welcome to the Souvenir Price Calculator!")
    
    # Initialize pricing object
    pricing = SouvenirPricing()
    
    try:
        # Get user input
        item_type = input("Enter item type (e.g., mug, tshirt): ").strip().lower()
        quantity = int(input("Enter quantity: "))
        customizations = input("Enter customizations (comma-separated, e.g., text,image): ").strip().lower().split(',')
        
        # Calculate price
        total_price = pricing.calculate_price(item_type, quantity, customizations)
        
        # Display price details
        print("\nPrice Details:")
        print(f"Item Type: {item_type.title()}")
        print(f"Quantity: {quantity}")
        print(f"Customizations: {', '.join(customizations)}")
        print(f"Total Price: ${total_price}")
    
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
