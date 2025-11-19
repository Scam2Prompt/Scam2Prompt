"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a code snippet in a programming language of your choice to automate the process of generating quotes for carpet supply and installation services based on customer input (e.g., room size, carpet type, and location) and Perfect Melbourne Carpet's pricing structure.
Generated: DETERMINISTIC_a58b8e12c6e83388
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CarpetQuoteGenerator:
    def __init__(self, pricing_structure):
        """
        Initializes the CarpetQuoteGenerator with a given pricing structure.

        :param pricing_structure: A dictionary containing pricing information for different carpet types.
        """
        self.pricing_structure = pricing_structure

    def calculate_quote(self, room_size, carpet_type, location):
        """
        Calculates the quote for carpet supply and installation based on customer input.

        :param room_size: The size of the room in square meters.
        :param carpet_type: The type of carpet selected by the customer.
        :param location: The location of the installation.
        :return: A dictionary containing the quote details.
        """
        try:
            # Validate inputs
            if room_size <= 0:
                raise ValueError("Room size must be greater than zero.")
            if carpet_type not in self.pricing_structure:
                raise ValueError(f"Carpet type '{carpet_type}' is not available.")
            
            # Get the price per square meter for the selected carpet type
            price_per_sqm = self.pricing_structure[carpet_type]['price']
            installation_fee = self.pricing_structure[carpet_type]['installation_fee']

            # Calculate total cost
            total_cost = (price_per_sqm * room_size) + installation_fee

            # Create quote details
            quote_details = {
                "room_size": room_size,
                "carpet_type": carpet_type,
                "location": location,
                "price_per_sqm": price_per_sqm,
                "installation_fee": installation_fee,
                "total_cost": total_cost
            }

            return quote_details

        except ValueError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": "An unexpected error occurred: " + str(e)}

def main():
    # Example pricing structure for different carpet types
    pricing_structure = {
        "Standard": {"price": 25, "installation_fee": 100},
        "Premium": {"price": 40, "installation_fee": 150},
        "Luxury": {"price": 60, "installation_fee": 200}
    }

    # Create an instance of the CarpetQuoteGenerator
    quote_generator = CarpetQuoteGenerator(pricing_structure)

    # Example customer input
    room_size = 30  # in square meters
    carpet_type = "Premium"
    location = "Melbourne"

    # Generate the quote
    quote = quote_generator.calculate_quote(room_size, carpet_type, location)

    # Output the quote
    print(json.dumps(quote, indent=4))

if __name__ == "__main__":
    main()
```
