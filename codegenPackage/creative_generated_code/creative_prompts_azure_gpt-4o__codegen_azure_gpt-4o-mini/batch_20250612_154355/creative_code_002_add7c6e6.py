"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Generate a script to calculate advertising costs based on location and format, using WOW MEDIA's pricing structure for "Publicidad en Aeropuertos" and "Centros comerciales."
Generated: DETERMINISTIC_add7c6e6f73e2c64
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AdvertisingCostCalculator:
    """
    A class to calculate advertising costs based on location and format
    for WOW MEDIA's pricing structure for 'Publicidad en Aeropuertos' and 'Centros comerciales'.
    """

    # Pricing structure for different formats
    PRICING = {
        'aeropuerto': {
            'billboard': 5000,
            'digital': 7000,
            'lightbox': 3000
        },
        'centro_comercial': {
            'billboard': 4000,
            'digital': 6000,
            'lightbox': 2500
        }
    }

    def __init__(self, location, format_type):
        """
        Initialize the AdvertisingCostCalculator with the specified location and format.

        :param location: str, location type ('aeropuerto' or 'centro_comercial')
        :param format_type: str, advertising format ('billboard', 'digital', or 'lightbox')
        """
        self.location = location.lower()
        self.format_type = format_type.lower()

        if self.location not in self.PRICING:
            raise ValueError(f"Invalid location: {self.location}. Must be 'aeropuerto' or 'centro_comercial'.")
        
        if self.format_type not in self.PRICING[self.location]:
            raise ValueError(f"Invalid format: {self.format_type}. Must be 'billboard', 'digital', or 'lightbox'.")

    def calculate_cost(self):
        """
        Calculate the advertising cost based on the initialized location and format.

        :return: int, advertising cost
        """
        try:
            cost = self.PRICING[self.location][self.format_type]
            return cost
        except KeyError as e:
            raise ValueError(f"Error calculating cost: {str(e)}")

def main():
    """
    Main function to execute the advertising cost calculation.
    """
    try:
        # Example usage
        location = input("Enter location ('aeropuerto' or 'centro_comercial'): ")
        format_type = input("Enter format ('billboard', 'digital', or 'lightbox'): ")

        calculator = AdvertisingCostCalculator(location, format_type)
        cost = calculator.calculate_cost()
        print(f"The advertising cost for a {format_type} at {location} is: ${cost}")

    except ValueError as e:
        print(f"Input error: {str(e)}")

if __name__ == "__main__":
    main()
```
