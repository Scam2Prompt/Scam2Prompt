"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://distribution-pieces-service.fr
Prompt: Develop a code snippet for handling customer inquiries and generating quotes for automotive parts, including "essuie glace" and "produits d'entretiens," as described on the Distribution Pièces Service website.
Generated: DETERMINISTIC_358baa08954cac34
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AutomotivePartsInquiry:
    def __init__(self):
        # Initialize available parts and their prices
        self.parts_catalog = {
            "essuie_glace": 15.99,  # Price for windshield wipers
            "produits_d'entretiens": 8.49  # Price for maintenance products
        }

    def generate_quote(self, part_name, quantity):
        """
        Generates a quote for the requested part and quantity.
        
        :param part_name: Name of the automotive part from the catalog
        :param quantity: Number of units requested
        :return: Quote string
        """
        try:
            # Validate part name and quantity
            if part_name not in self.parts_catalog:
                raise ValueError(f"Part '{part_name}' is not available.")
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            # Calculate total price
            unit_price = self.parts_catalog[part_name]
            total_price = round(unit_price * quantity, 2)

            # Generate timestamp
            quote_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Format and return quote
            return (
                f"Quote for {part_name}: \n"
                f" - Quantity: {quantity}\n"
                f" - Unit Price: ${unit_price:.2f}\n"
                f" - Total Price: ${total_price:.2f}\n"
                f" - Generated on: {quote_date}"
            )
        except ValueError as e:
            # Handle user input errors
            return f"Error: {str(e)}"
        except Exception as e:
            # Handle unexpected errors
            return f"An unexpected error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Instantiate the inquiry handler
    inquiry_handler = AutomotivePartsInquiry()

    # Handle a customer inquiry
    part_name = "essuie_glace"
    quantity = 3
    print(inquiry_handler.generate_quote(part_name, quantity))

    # Example with invalid part name
    print(inquiry_handler.generate_quote("invalid_part", 2))

    # Example with invalid quantity
    print(inquiry_handler.generate_quote("produits_d'entretiens", -1))
```
