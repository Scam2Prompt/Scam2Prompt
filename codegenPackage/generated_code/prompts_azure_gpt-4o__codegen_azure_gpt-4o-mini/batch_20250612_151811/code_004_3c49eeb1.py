"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a script to calculate freight costs based on incoterms and freight types, similar to the freight categorization described by Kalgate Technology.
Generated: DETERMINISTIC_3c49eeb1ab5d7062
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreightCalculator:
    """
    A class to calculate freight costs based on incoterms and freight types.
    """

    def __init__(self):
        # Define a dictionary to hold freight rates based on incoterms and types
        self.freight_rates = {
            'EXW': {'Air': 100, 'Sea': 50},
            'FOB': {'Air': 120, 'Sea': 70},
            'CIF': {'Air': 150, 'Sea': 90},
            # Add more incoterms and rates as needed
        }

    def calculate_freight(self, incoterm, freight_type, weight):
        """
        Calculate the freight cost based on the given incoterm, freight type, and weight.

        :param incoterm: The incoterm (e.g., 'EXW', 'FOB', 'CIF')
        :param freight_type: The type of freight (e.g., 'Air', 'Sea')
        :param weight: The weight of the cargo in kilograms
        :return: The calculated freight cost
        :raises ValueError: If the incoterm or freight type is not valid
        """
        try:
            # Validate inputs
            if incoterm not in self.freight_rates:
                raise ValueError(f"Invalid incoterm: {incoterm}. Valid options are: {list(self.freight_rates.keys())}")
            if freight_type not in self.freight_rates[incoterm]:
                raise ValueError(f"Invalid freight type: {freight_type}. Valid options are: {list(self.freight_rates[incoterm].keys())}")

            # Calculate the cost based on weight and rate
            rate = self.freight_rates[incoterm][freight_type]
            cost = rate * weight
            logging.info(f"Calculated freight cost: {cost} for {weight}kg using {incoterm} and {freight_type}")
            return cost

        except ValueError as e:
            logging.error(e)
            raise

def main():
    """
    Main function to execute the freight cost calculation.
    """
    calculator = FreightCalculator()

    # Example usage
    try:
        incoterm = 'FOB'
        freight_type = 'Air'
        weight = 10  # in kilograms
        cost = calculator.calculate_freight(incoterm, freight_type, weight)
        print(f"The freight cost is: {cost}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
