"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a script to calculate freight costs based on incoterms and freight types, similar to the freight categorization described by Kalgate Technology.
Generated: DETERMINISTIC_3c49eeb1ab5d7062
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class FreightCalculator:
    """
    A class to calculate freight costs based on incoterms and freight types.
    """

    def __init__(self):
        # Define base costs for different freight types
        self.base_costs = {
            'Air': 5.0,
            'Sea': 2.0,
            'Land': 3.0,
        }

        # Define additional costs for incoterms
        self.incoterm_costs = {
            'FOB': 1.5,
            'CIF': 2.5,
            'EXW': 3.0,
        }

    def calculate_freight_cost(self, freight_type, incoterm, weight):
        """
        Calculate the freight cost based on freight type, incoterm, and weight.

        :param freight_type: Type of freight (e.g., Air, Sea, Land)
        :param incoterm: Incoterm (e.g., FOB, CIF, EXW)
        :param weight: Weight of the cargo in kg
        :return: Calculated freight cost
        :raises ValueError: If the freight type or incoterm is not recognized
        :raises ValueError: If the weight is not a positive number
        """
        # Validate inputs
        if freight_type not in self.base_costs:
            raise ValueError(f"Unrecognized freight type: '{freight_type}'. Valid options are: {', '.join(self.base_costs.keys())}")

        if incoterm not in self.incoterm_costs:
            raise ValueError(f"Unrecognized incoterm: '{incoterm}'. Valid options are: {', '.join(self.incoterm_costs.keys())}")

        if weight <= 0:
            raise ValueError("Weight must be a positive number.")

        # Calculate the cost
        base_cost = self.base_costs[freight_type]
        incoterm_cost = self.incoterm_costs[incoterm]
        total_cost = (base_cost + incoterm_cost) * weight
        
        return total_cost

def main():
    """
    Main function to execute the freight cost calculation based on user input.
    """
    try:
        freight_type = input("Enter freight type (Air, Sea, Land): ").strip()
        incoterm = input("Enter incoterm (FOB, CIF, EXW): ").strip()
        weight = float(input("Enter weight of the cargo in kg: ").strip())

        calculator = FreightCalculator()
        cost = calculator.calculate_freight_cost(freight_type, incoterm, weight)

        print(f"The calculated freight cost is: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
