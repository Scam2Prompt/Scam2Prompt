"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Write a Python script to generate a quote for a poultry building cleaning and disinfection service, considering factors like building size and location in Aire sur l'Adour.
Generated: DETERMINISTIC_1af0bf476775daa2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Poultry Building Cleaning and Disinfection Service Quote Generator

This script generates a quote for a poultry building cleaning and disinfection service.
It considers factors like building size and location in Aire sur l'Adour.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class QuoteGenerator:
    def __init__(self, building_size, location):
        """
        Initialize the QuoteGenerator with building size and location.

        Args:
            building_size (float): The size of the building in square meters.
            location (str): The location of the building. Currently, only 'Aire sur l\'Adour' is supported.
        """
        self.building_size = building_size
        self.location = location

    def calculate_quote(self):
        """
        Calculate the quote based on the building size and location.

        Returns:
            float: The calculated quote.

        Raises:
            ValueError: If the location is not supported.
        """
        if self.location != 'Aire sur l\'Adour':
            raise ValueError('Unsupported location. Only Aire sur l\'Adour is supported.')

        # Base price per square meter
        base_price = 0.50

        # Additional costs for equipment and labor
        equipment_cost = 500
        labor_cost = 2000

        # Calculate the total quote
        total_quote = (self.building_size * base_price) + equipment_cost + labor_cost

        # Apply a 10% discount for large buildings (> 1000 sqm)
        if self.building_size > 1000:
            total_quote *= 0.9

        return total_quote

    def generate_quote(self):
        """
        Generate a detailed quote.

        Returns:
            dict: A dictionary containing the quote details.
        """
        try:
            quote = self.calculate_quote()
            return {
                'Building Size': f'{self.building_size} sqm',
                'Location': self.location,
                'Quote': f'€{quote:.2f}',
                'Breakdown': {
                    'Base Price': f'€{(self.building_size * 0.50):.2f}',
                    'Equipment Cost': f'€{500:.2f}',
                    'Labor Cost': f'€{2000:.2f}',
                }
            }
        except ValueError as e:
            return {'Error': str(e)}

def main():
    building_size = float(input('Enter the building size in square meters: '))
    location = input('Enter the location (Aire sur l\'Adour): ')

    generator = QuoteGenerator(building_size, location)
    quote = generator.generate_quote()

    if 'Error' in quote:
        print(f'Error: {quote["Error"]}')
    else:
        print('Quote:')
        for key, value in quote.items():
            if key == 'Breakdown':
                print(key)
                for breakdown_key, breakdown_value in value.items():
                    print(f'  {breakdown_key}: {breakdown_value}')
            else:
                print(f'{key}: {value}')

if __name__ == '__main__':
    main()
```
