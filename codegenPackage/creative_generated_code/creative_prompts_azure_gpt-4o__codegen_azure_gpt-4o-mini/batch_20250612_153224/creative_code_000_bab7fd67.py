"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Write a Python script to calculate dumpster rental pricing based on the service areas listed on the Purple Dumpster website, including specific regions like Milton, Oakville, and Mississauga.
Generated: DETERMINISTIC_bab7fd67f00bdec9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal

class DumpsterRental:
    def __init__(self, base_price, area_multiplier):
        """
        Initializes the DumpsterRental object with a base price and a pricing multiplier for specific areas.
        
        :param base_price: The base price for dumpster rental
        :param area_multiplier: A dictionary mapping service areas to their respective pricing multipliers
        """
        self.base_price = Decimal(base_price)
        self.area_multiplier = area_multiplier

    def calculate_price(self, area):
        """
        Calculates the total price for renting a dumpster based on the specified area.
        
        :param area: The area for which the dumpster is being rented
        :return: The total price as a Decimal
        """
        if area not in self.area_multiplier:
            raise ValueError(f"Service area '{area}' is not available.")
        
        multiplier = Decimal(self.area_multiplier[area])
        total_price = self.base_price * multiplier
        return total_price

def load_pricing_data(file_path):
    """
    Loads pricing data from a JSON file.
    
    :param file_path: Path to the JSON file containing pricing data
    :return: A tuple containing base price and area multipliers
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data['base_price'], data['area_multiplier']
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading pricing data: {e}")

def main():
    """
    Main function to execute the dumpster rental pricing calculation.
    """
    try:
        # Load pricing data from the JSON file
        base_price, area_multiplier = load_pricing_data('pricing_data.json')
        
        # Initialize the DumpsterRental object with the loaded data
        rental_service = DumpsterRental(base_price, area_multiplier)
        
        # List of service areas to calculate prices for
        service_areas = ['Milton', 'Oakville', 'Mississauga']
        
        # Calculate and display pricing for each service area
        for area in service_areas:
            try:
                price = rental_service.calculate_price(area)
                print(f"The rental price for {area} is: ${price:.2f}")
            except ValueError as ve:
                print(ve)
    except RuntimeError as re:
        print(re)

if __name__ == "__main__":
    main()
```

**Note:** 
You will need a JSON file named `pricing_data.json` with the following structure for this script to run successfully:

```json
{
    "base_price": "100.00",
    "area_multiplier": {
        "Milton": "1.2",
        "Oakville": "1.5",
        "Mississauga": "1.3"
    }
}
```

Make sure to adjust the base price and area multipliers as per your requirements.
