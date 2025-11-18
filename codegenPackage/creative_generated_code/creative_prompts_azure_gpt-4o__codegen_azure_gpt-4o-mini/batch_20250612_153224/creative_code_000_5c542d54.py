"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Write a Python script to simulate rental costs using the "Simulador Arriendo" feature described on the Inmobiliaria Nueva Ciudad website. Include inputs for property type, location, and rental duration.
Generated: DETERMINISTIC_5c542d5483f7ad2a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Rental Cost Simulator

This script simulates rental costs based on property type, location, and rental duration.
Users can select from predefined property types and locations to calculate the estimated rent.

Author: Your Name
Date: YYYY-MM-DD
"""

class RentalSimulator:
    def __init__(self):
        # Predefined property types with base prices
        self.property_types = {
            'Apartment': 800,
            'House': 1200,
            'Studio': 600
        }

        # Predefined locations with multipliers
        self.locations = {
            'Downtown': 1.5,
            'Suburbs': 1.0,
            'Rural': 0.8
        }

    def calculate_rent(self, property_type, location, duration):
        """
        Calculate the estimated rental cost.

        :param property_type: str, type of property (Apartment, House, Studio)
        :param location: str, location of the property (Downtown, Suburbs, Rural)
        :param duration: int, rental duration in months
        :return: float, estimated rental cost
        """
        try:
            # Validate inputs
            if property_type not in self.property_types:
                raise ValueError(f"Invalid property type: {property_type}. Choose from {list(self.property_types.keys())}.")
            if location not in self.locations:
                raise ValueError(f"Invalid location: {location}. Choose from {list(self.locations.keys())}.")
            if not isinstance(duration, int) or duration <= 0:
                raise ValueError("Duration must be a positive integer.")

            # Calculate rent
            base_price = self.property_types[property_type]
            location_multiplier = self.locations[location]
            total_rent = base_price * location_multiplier * duration

            return total_rent

        except Exception as e:
            print(f"Error calculating rent: {e}")
            return None

def main():
    simulator = RentalSimulator()

    # Gather user input
    property_type = input("Enter property type (Apartment, House, Studio): ")
    location = input("Enter location (Downtown, Suburbs, Rural): ")
    duration = int(input("Enter rental duration in months: "))

    # Calculate and display the estimated rental cost
    estimated_rent = simulator.calculate_rent(property_type, location, duration)
    
    if estimated_rent is not None:
        print(f"The estimated rental cost for a {property_type} in {location} for {duration} months is: ${estimated_rent:.2f}")

if __name__ == "__main__":
    main()
```
