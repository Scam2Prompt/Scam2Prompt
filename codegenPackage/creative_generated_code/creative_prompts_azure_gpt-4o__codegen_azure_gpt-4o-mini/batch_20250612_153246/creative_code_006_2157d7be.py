"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cidautos.com
Prompt: Create a script to automate the generation of vehicle price quotes based on user input, as seen in the "Cotizar Vehículo" feature on Cid Autos.
Generated: DETERMINISTIC_2157d7be3d560053
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class VehicleQuoteGenerator:
    """
    A class to generate vehicle price quotes based on user input.
    """

    def __init__(self):
        self.base_price = 10000  # Base price for the vehicle
        self.tax_rate = 0.15     # Tax rate
        self.discount_rate = 0.10  # Discount rate for eligible users

    def calculate_discount(self, is_eligible: bool) -> float:
        """
        Calculate the applicable discount.
        
        :param is_eligible: Boolean indicating if the user is eligible for a discount
        :return: Discount amount
        """
        return self.base_price * self.discount_rate if is_eligible else 0.0

    def calculate_tax(self, sub_total: float) -> float:
        """
        Calculate the tax on the price.
        
        :param sub_total: The subtotal amount before tax
        :return: Tax amount
        """
        return sub_total * self.tax_rate

    def generate_quote(self, is_eligible: bool) -> dict:
        """
        Generate a quote for the vehicle based on user eligibility for discount.

        :param is_eligible: Boolean indicating if the user is eligible for a discount
        :return: A dictionary with the quote details
        """
        try:
            discount = self.calculate_discount(is_eligible)
            sub_total = self.base_price - discount
            tax = self.calculate_tax(sub_total)
            total_price = sub_total + tax
            
            quote = {
                "base_price": self.base_price,
                "discount": discount,
                "sub_total": sub_total,
                "tax": tax,
                "total_price": total_price
            }

            return quote
        
        except Exception as e:
            # Log the error and raise an exception
            print(f"Error generating quote: {e}")
            raise

def main():
    """
    Main function to run the vehicle quote generator.
    """
    try:
        # User input for eligibility
        is_eligible_input = input("Are you eligible for a discount? (yes/no): ").strip().lower()
        is_eligible = is_eligible_input == "yes"

        # Create a VehicleQuoteGenerator instance
        quote_generator = VehicleQuoteGenerator()

        # Generate the quote
        quote = quote_generator.generate_quote(is_eligible)

        # Print the quote in a formatted way
        print(json.dumps(quote, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
