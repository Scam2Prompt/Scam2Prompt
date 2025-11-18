"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Write Python code to simulate property rental pricing based on the "Simulador Arriendo" tool described on the Dominguez Parra website, incorporating variables like property type, location, and size.
Generated: DETERMINISTIC_2667807be920efaf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PropertyRentalSimulator:
    def __init__(self, property_type, location, size):
        """
        Initializes the PropertyRentalSimulator with property type, location, and size.

        Parameters:
            property_type (str): Type of the property (e.g., 'Apartment', 'House').
            location (str): Location of the property (e.g., 'Downtown', 'Suburbs').
            size (float): Size of the property in square meters.
        """
        self.property_type = property_type
        self.location = location
        self.size = size
        self.base_prices = {
            'Apartment': 10,  # Base price per square meter in $ for Apartments
            'House': 15       # Base price per square meter in $ for Houses
        }
        self.location_multiplier = {
            'Downtown': 1.5,  # Price multiplier for Downtown
            'Suburbs': 1.2,   # Price multiplier for Suburbs
            'Countryside': 1.0 # Price multiplier for Countryside
        }

    def calculate_rental_price(self):
        """
        Calculates the estimated rental price based on property attributes.

        Returns:
            float: Estimated rental price in $.
        """
        try:
            # Validate property type
            if self.property_type not in self.base_prices:
                raise ValueError("Invalid property type. Choose 'Apartment' or 'House'.")
            
            # Validate location
            if self.location not in self.location_multiplier:
                raise ValueError("Invalid location. Choose 'Downtown', 'Suburbs', or 'Countryside'.")

            # Calculate base price
            base_price = self.base_prices[self.property_type]
            # Apply location multiplier
            final_price = base_price * self.size * self.location_multiplier[self.location]
            # Add some randomness to simulate market variations
            final_price += random.uniform(-100, 100)  # Add a random fluctuation

            return round(final_price, 2)  # Round to 2 decimal places

        except Exception as e:
            print(f"Error calculating rental price: {e}")
            return None

def main():
    # Example usage
    try:
        property_type = input("Enter property type (Apartment/House): ")
        location = input("Enter location (Downtown/Suburbs/Countryside): ")
        size = float(input("Enter property size in square meters: "))

        # Create a PropertyRentalSimulator instance
        rental_simulator = PropertyRentalSimulator(property_type, location, size)

        # Calculate and display the rental price
        rental_price = rental_simulator.calculate_rental_price()
        if rental_price is not None:
            print(f"The estimated rental price is: ${rental_price}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
