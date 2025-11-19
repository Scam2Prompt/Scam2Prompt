"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Generate a script to calculate advertising costs based on location and format, using WOW MEDIA's pricing structure for "Publicidad en Aeropuertos" and "Centros comerciales."
Generated: DETERMINISTIC_add7c6e6f73e2c64
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AdvertisingCostCalculator:
    """
    A class to calculate advertising costs based on location and format
    using WOW MEDIA's pricing structure for 'Publicidad en Aeropuertos' 
    and 'Centros comerciales'.
    """

    # Pricing structure for different advertising formats
    PRICING_STRUCTURE = {
        'aeropuerto': {
            'digital': 5000,  # Cost for digital ads in airports
            'print': 3000     # Cost for print ads in airports
        },
        'centro_comercial': {
            'digital': 4000,  # Cost for digital ads in shopping centers
            'print': 2500     # Cost for print ads in shopping centers
        }
    }

    def __init__(self):
        """Initialize the AdvertisingCostCalculator."""
        pass

    def calculate_cost(self, location: str, format_type: str, quantity: int) -> float:
        """
        Calculate the total advertising cost.

        :param location: The location for advertising ('aeropuerto' or 'centro_comercial').
        :param format_type: The format of the advertisement ('digital' or 'print').
        :param quantity: The number of advertisements.
        :return: The total cost of the advertisements.
        :raises ValueError: If the location or format_type is invalid, or if quantity is non-positive.
        """
        # Validate inputs
        if location not in self.PRICING_STRUCTURE:
            raise ValueError(f"Invalid location: {location}. Must be 'aeropuerto' or 'centro_comercial'.")
        
        if format_type not in self.PRICING_STRUCTURE[location]:
            raise ValueError(f"Invalid format type: {format_type}. Must be 'digital' or 'print'.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate total cost
        cost_per_ad = self.PRICING_STRUCTURE[location][format_type]
        total_cost = cost_per_ad * quantity

        return total_cost


def main():
    """Main function to execute the advertising cost calculation."""
    calculator = AdvertisingCostCalculator()

    try:
        # Example usage
        location = 'aeropuerto'  # Change as needed
        format_type = 'digital'   # Change as needed
        quantity = 10             # Change as needed

        total_cost = calculator.calculate_cost(location, format_type, quantity)
        print(f"The total advertising cost for {quantity} {format_type} ads in {location} is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
