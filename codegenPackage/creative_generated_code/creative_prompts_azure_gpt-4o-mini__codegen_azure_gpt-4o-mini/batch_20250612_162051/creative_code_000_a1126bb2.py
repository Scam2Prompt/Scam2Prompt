"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Generate a code snippet for a property rental simulator that calculates monthly payments based on user input for property type and location as described on the Nueva Ciudad website.
Generated: DETERMINISTIC_a1126bb265c694bb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PropertyRentalSimulator:
    """
    A simulator for calculating monthly rental payments based on property type and location.
    """

    def __init__(self):
        # Define base rent values for different property types in different locations
        self.base_rent = {
            'apartment': {'city_center': 2000, 'suburb': 1500},
            'house': {'city_center': 3000, 'suburb': 2000},
            'studio': {'city_center': 1800, 'suburb': 1200}
        }

    def get_monthly_payment(self, property_type, location):
        """
        Calculate the monthly rental payment based on property type and location.

        :param property_type: The type of the property (e.g., 'apartment', 'house', 'studio').
        :param location: The location of the property (e.g., 'city_center', 'suburb').
        :return: Monthly payment amount.
        :raises ValueError: If the property type or location is invalid.
        """
        try:
            # Validate input parameters
            if property_type not in self.base_rent:
                raise ValueError(f"Invalid property type: {property_type}. Valid options are: {list(self.base_rent.keys())}.")
            if location not in self.base_rent[property_type]:
                raise ValueError(f"Invalid location: {location}. Valid options are: {list(self.base_rent[property_type].keys())}.")

            # Calculate monthly payment
            monthly_payment = self.base_rent[property_type][location]
            return monthly_payment
        
        except Exception as e:
            # Log the error message (in a real application, this should be logged to a logging system)
            print(f"Error: {str(e)}")
            return None  # Return None to indicate an error occurred


# Example usage
if __name__ == "__main__":
    simulator = PropertyRentalSimulator()

    # Sample user input
    property_type = input("Enter property type (apartment, house, studio): ").strip().lower()
    location = input("Enter location (city_center, suburb): ").strip().lower()

    # Calculate and display the monthly payment
    monthly_payment = simulator.get_monthly_payment(property_type, location)
    if monthly_payment is not None:
        print(f"The monthly rental payment for a {property_type} in {location} is: ${monthly_payment}")
```
