"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Create a script to generate a quote for UPVC window and door installation services, including input fields for design selection, service type, and location, as described on the Dexodoor website.
Generated: DETERMINISTIC_aec486a88e839f37
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class QuoteGenerator:
    def __init__(self):
        # Initialize the service options and their respective prices
        self.service_options = {
            'window': 200,
            'door': 300,
            'window_and_door': 450
        }
        self.design_options = {
            'standard': 0,
            'premium': 100,
            'luxury': 200
        }
        self.location_multiplier = {
            'urban': 1.2,
            'suburban': 1.0,
            'rural': 0.8
        }

    def get_service_type(self):
        """Prompt user for service type and validate input."""
        print("Select service type: window, door, or window_and_door")
        service_type = input("Enter service type: ").strip().lower()
        if service_type not in self.service_options:
            raise ValueError("Invalid service type selected.")
        return service_type

    def get_design_selection(self):
        """Prompt user for design selection and validate input."""
        print("Select design type: standard, premium, or luxury")
        design_type = input("Enter design type: ").strip().lower()
        if design_type not in self.design_options:
            raise ValueError("Invalid design type selected.")
        return design_type

    def get_location(self):
        """Prompt user for location and validate input."""
        print("Select location type: urban, suburban, or rural")
        location = input("Enter location type: ").strip().lower()
        if location not in self.location_multiplier:
            raise ValueError("Invalid location type selected.")
        return location

    def calculate_quote(self, service_type, design_type, location):
        """Calculate the total quote based on user selections."""
        base_price = self.service_options[service_type]
        design_price = self.design_options[design_type]
        location_factor = self.location_multiplier[location]

        total_quote = (base_price + design_price) * location_factor
        return total_quote

    def generate_quote(self):
        """Main method to generate the quote."""
        try:
            service_type = self.get_service_type()
            design_type = self.get_design_selection()
            location = self.get_location()

            total_quote = self.calculate_quote(service_type, design_type, location)
            print(f"Your total quote for {service_type} with {design_type} design in {location} location is: ${total_quote:.2f}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    quote_generator = QuoteGenerator()
    quote_generator.generate_quote()
```
