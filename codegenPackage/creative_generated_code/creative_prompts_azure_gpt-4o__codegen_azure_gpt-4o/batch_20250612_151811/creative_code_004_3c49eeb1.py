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
    FreightCalculator is a class used to calculate freight costs based on incoterms and freight types.
    """

    def __init__(self):
        # Define base costs for different freight types
        self.freight_base_costs = {
            "air": 10.0,  # Cost per kg for air freight
            "sea": 5.0,   # Cost per kg for sea freight
            "land": 3.0   # Cost per km for land freight
        }
        
        # Define incoterm adjustments
        self.incoterm_adjustments = {
            "EXW": 1.0,   # Ex Works (no additional services)
            "FOB": 1.2,   # Free On Board (includes loading costs)
            "CIF": 1.5,   # Cost, Insurance, and Freight (includes insurance and freight costs)
            "DDP": 2.0    # Delivered Duty Paid (includes duty costs)
        }

    def calculate_cost(self, freight_type, incoterm, weight_or_distance):
        """
        Calculate freight cost based on the provided freight type, incoterm, and weight/distance.

        Parameters:
            freight_type (str): Type of freight (e.g., 'air', 'sea', 'land')
            incoterm (str): Incoterm (e.g., 'EXW', 'FOB', 'CIF', 'DDP')
            weight_or_distance (float): Weight in kg for air/sea freight or distance in km for land freight

        Returns:
            float: Total freight cost
        """
        try:
            # Validate freight type
            if freight_type not in self.freight_base_costs:
                raise ValueError(f"Invalid freight type: {freight_type}. Allowed values are: {', '.join(self.freight_base_costs.keys())}")

            # Validate incoterm
            if incoterm not in self.incoterm_adjustments:
                raise ValueError(f"Invalid incoterm: {incoterm}. Allowed values are: {', '.join(self.incoterm_adjustments.keys())}")

            # Validate weight or distance
            if weight_or_distance <= 0:
                raise ValueError("Weight or distance must be a positive number.")

            # Calculate base cost
            base_cost = self.freight_base_costs[freight_type] * weight_or_distance

            # Apply incoterm adjustment
            total_cost = base_cost * self.incoterm_adjustments[incoterm]

            return total_cost

        except ValueError as ve:
            print(f"Error: {ve}", file=sys.stderr)
            return None

        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            return None


# Main script
if __name__ == "__main__":
    # Instantiate the FreightCalculator
    calculator = FreightCalculator()

    # Example inputs
    freight_type = "air"           # Options: 'air', 'sea', 'land'
    incoterm = "CIF"               # Options: 'EXW', 'FOB', 'CIF', 'DDP'
    weight_or_distance = 100.0     # Weight in kg for 'air'/'sea', distance in km for 'land'

    # Calculate the freight cost
    cost = calculator.calculate_cost(freight_type, incoterm, weight_or_distance)

    # Display the result
    if cost is not None:
        print(f"The total freight cost for {weight_or_distance} units of '{freight_type}' freight with incoterm '{incoterm}' is: ${cost:.2f}")
```
