"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Create a script to generate a quote for UPVC window and door installation services, including input fields for design selection, service type, and location, as described on the Dexodoor website.
Generated: DETERMINISTIC_aec486a88e839f37
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class QuoteGenerator:
    def __init__(self):
        self.service_types = {
            'window': 200,  # Base price for window installation
            'door': 300,    # Base price for door installation
        }
        self.design_options = {
            'standard': 0,      # No additional cost for standard design
            'premium': 50,      # Additional cost for premium design
            'luxury': 100,      # Additional cost for luxury design
        }
    
    def get_service_price(self, service_type):
        """Retrieve the base price for the given service type."""
        return self.service_types.get(service_type, 0)

    def get_design_price(self, design_type):
        """Retrieve the additional price for the given design type."""
        return self.design_options.get(design_type, 0)

    def calculate_quote(self, service_type, design_type, location):
        """Calculate the total quote based on service type, design type, and location."""

        # Validate inputs
        if service_type not in self.service_types:
            raise ValueError(f"Invalid service type: {service_type}. Valid options: {list(self.service_types.keys())}")
        if design_type not in self.design_options:
            raise ValueError(f"Invalid design type: {design_type}. Valid options: {list(self.design_options.keys())}")

        # Get prices
        service_price = self.get_service_price(service_type)
        design_price = self.get_design_price(design_type)

        # Calculate total quote
        total_quote = service_price + design_price
        
        quote_details = {
            'service_type': service_type,
            'design_type': design_type,
            'location': location,
            'total_quote': total_quote
        }
        
        return quote_details

def main():
    """Main function to execute the quote generation process."""
    print("Welcome to the UPVC Window and Door Installation Quote Generator")

    # Input fields for the user
    service_type = input("Enter the service type (window/door): ").strip().lower()
    design_type = input("Enter the design type (standard/premium/luxury): ").strip().lower()
    location = input("Enter your location: ").strip()

    # Create a QuoteGenerator instance
    quote_generator = QuoteGenerator()

    try:
        # Generate quote
        quote = quote_generator.calculate_quote(service_type, design_type, location)
        print(json.dumps(quote, indent=4))  # Output the quote in a structured format
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
