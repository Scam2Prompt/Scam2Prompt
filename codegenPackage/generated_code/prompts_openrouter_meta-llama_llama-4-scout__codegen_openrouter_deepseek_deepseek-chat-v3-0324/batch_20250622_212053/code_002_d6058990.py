"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Generate a code snippet to compare the pricing of different apartment configurations in L&T Elara Celestia, such as 3 BHK (S) vs 3 BHK (L) vs 4 BHK.
Generated: DETERMINISTIC_d6058990ddce6136
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Apartment:
    """
    Represents an apartment configuration with its pricing details.
    """
    def __init__(self, name, configuration, base_price, area_sqft):
        """
        Initialize an apartment configuration.
        
        Args:
            name (str): Name of the apartment (e.g., 'Elara Celestia')
            configuration (str): Configuration type (e.g., '3 BHK (S)')
            base_price (float): Base price in INR
            area_sqft (float): Area in square feet
        """
        self.name = name
        self.configuration = configuration
        self.base_price = base_price
        self.area_sqft = area_sqft
    
    def price_per_sqft(self):
        """Calculate and return price per square foot."""
        return self.base_price / self.area_sqft
    
    def __str__(self):
        """String representation of the apartment configuration."""
        return f"{self.name} - {self.configuration}"


def compare_apartments(apartments):
    """
    Compare multiple apartment configurations and print a comparison table.
    
    Args:
        apartments (list): List of Apartment objects to compare
    """
    if not apartments:
        print("No apartments to compare.")
        return
    
    # Print header
    print("\nApartment Comparison - L&T Elara Celestia")
    print("-" * 60)
    print(f"{'Configuration':<20} | {'Base Price (INR)':<15} | {'Area (sq.ft)':<12} | {'Price/sq.ft':<12}")
    print("-" * 60)
    
    # Print each apartment's details
    for apt in apartments:
        print(f"{apt.configuration:<20} | {apt.base_price:>15,.2f} | {apt.area_sqft:>12,.2f} | {apt.price_per_sqft():>12,.2f}")
    
    print("-" * 60)


if __name__ == "__main__":
    # Sample apartment configurations for L&T Elara Celestia
    apartments = [
        Apartment("Elara Celestia", "3 BHK (S)", 12500000, 1450),
        Apartment("Elara Celestia", "3 BHK (L)", 14500000, 1650),
        Apartment("Elara Celestia", "4 BHK", 18500000, 2100)
    ]
    
    try:
        compare_apartments(apartments)
    except Exception as e:
        print(f"Error comparing apartments: {str(e)}")
```
