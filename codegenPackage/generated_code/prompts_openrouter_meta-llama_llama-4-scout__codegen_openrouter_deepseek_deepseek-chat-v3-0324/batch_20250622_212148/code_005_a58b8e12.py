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
import math

class CarpetQuoteGenerator:
    """
    A class to generate quotes for carpet supply and installation services.
    Pricing is based on room dimensions, carpet type, and location.
    """
    
    # Pricing structure (per square meter)
    CARPET_TYPES = {
        'nylon': 25.0,
        'polyester': 20.0,
        'wool': 35.0,
        'olefin': 15.0
    }
    
    # Installation cost multipliers by location
    LOCATION_MULTIPLIERS = {
        'CBD': 1.2,
        'suburban': 1.0,
        'regional': 1.3
    }
    
    # Additional fees
    BASE_INSTALLATION_FEE = 50.0
    WASTAGE_FACTOR = 1.1  # 10% additional material for cutting/wastage
    
    def __init__(self):
        """Initialize the quote generator with default values."""
        self.room_length = 0.0
        self.room_width = 0.0
        self.carpet_type = ''
        self.location = ''
    
    def get_customer_input(self):
        """Collect and validate customer input for the quote."""
        while True:
            try:
                self.room_length = float(input("Enter room length (meters): "))
                self.room_width = float(input("Enter room width (meters): "))
                if self.room_length <= 0 or self.room_width <= 0:
                    raise ValueError("Dimensions must be positive numbers")
                
                print("Available carpet types:")
                for carpet in self.CARPET_TYPES:
                    print(f"- {carpet}")
                self.carpet_type = input("Enter carpet type: ").lower()
                if self.carpet_type not in self.CARPET_TYPES:
                    raise ValueError("Invalid carpet type")
                
                print("Available locations:")
                for location in self.LOCATION_MULTIPLIERS:
                    print(f"- {location}")
                self.location = input("Enter location: ").lower()
                if self.location not in self.LOCATION_MULTIPLIERS:
                    raise ValueError("Invalid location")
                
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    def calculate_quote(self):
        """
        Calculate the total quote based on customer input.
        Returns a dictionary with cost breakdown.
        """
        try:
            # Calculate area with wastage factor
            area = self.room_length * self.room_width * self.WASTAGE_FACTOR
            
            # Calculate costs
            carpet_cost = area * self.CARPET_TYPES[self.carpet_type]
            installation_cost = (area * self.CARPET_TYPES[self.carpet_type] * 0.3)  # 30% of carpet cost
            installation_cost *= self.LOCATION_MULTIPLIERS[self.location]
            
            total_cost = carpet_cost + installation_cost + self.BASE_INSTALLATION_FEE
            
            return {
                'area_sqm': round(area, 2),
                'carpet_cost': round(carpet_cost, 2),
                'installation_cost': round(installation_cost, 2),
                'base_fee': self.BASE_INSTALLATION_FEE,
                'total_cost': round(total_cost, 2),
                'carpet_type': self.carpet_type,
                'location': self.location
            }
        except Exception as e:
            print(f"Error calculating quote: {e}")
            return None
    
    def display_quote(self, quote_details):
        """Display the quote details in a user-friendly format."""
        if not quote_details:
            print("Unable to generate quote.")
            return
        
        print("\n=== Perfect Melbourne Carpet Quote ===")
        print(f"Carpet Type: {quote_details['carpet_type'].capitalize()}")
        print(f"Location: {quote_details['location'].capitalize()}")
        print(f"Area (including wastage): {quote_details['area_sqm']} sqm")
        print(f"Carpet Cost: ${quote_details['carpet_cost']}")
        print(f"Installation Cost: ${quote_details['installation_cost']}")
        print(f"Base Installation Fee: ${quote_details['base_fee']}")
        print("-------------------------------------")
        print(f"TOTAL COST: ${quote_details['total_cost']}\n")

# Main execution
if __name__ == "__main__":
    print("Welcome to Perfect Melbourne Carpet Quote Generator")
    generator = CarpetQuoteGenerator()
    generator.get_customer_input()
    quote = generator.calculate_quote()
    generator.display_quote(quote)
```
