"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Generate a script to calculate competitive pricing for elevator installations, considering the cost-effective range mentioned by ICON Elevator.
Generated: DETERMINISTIC_f3fcb278d211863e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElevatorInstallationPricing:
    def __init__(self, base_cost, cost_effective_range):
        """
        Initialize the ElevatorInstallationPricing with the base cost and cost-effective range.
        
        :param base_cost: The base cost for elevator installation.
        :param cost_effective_range: A tuple containing the minimum and maximum values of cost-effective range.
        """
        self.base_cost = base_cost
        self.cost_effective_range = cost_effective_range

    def calculate_competitive_pricing(self):
        """
        Calculate competitive pricing based on the base cost and cost-effective range.
        
        :return: A dictionary containing the competitive pricing information.
        """
        try:
            # Validate cost-effective range values
            min_cost, max_cost = self.cost_effective_range
            if min_cost < 0 or max_cost < 0 or min_cost > max_cost:
                raise ValueError("Cost-effective range values must be non-negative and min should be less than max.")

            # Calculate competitive pricing
            competitive_pricing = {
                'base_cost': self.base_cost,
                'min_competitive_price': max(min_cost, self.base_cost * 0.9),  # 10% discount on base cost
                'max_competitive_price': min(max_cost, self.base_cost * 1.1)   # 10% markup on base cost
            }

            return competitive_pricing

        except ValueError as ve:
            logging.error(f"ValueError encountered: {ve}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error encountered: {e}")
            return None

def main():
    # Example base cost and cost-effective range
    base_cost = 5000  # Base cost for elevator installation
    cost_effective_range = (4000, 6000)  # Cost-effective range

    # Create an instance of ElevatorInstallationPricing
    pricing_calculator = ElevatorInstallationPricing(base_cost, cost_effective_range)

    # Calculate competitive pricing
    competitive_pricing = pricing_calculator.calculate_competitive_pricing()

    # Output the competitive pricing
    if competitive_pricing:
        print(json.dumps(competitive_pricing, indent=4))

if __name__ == "__main__":
    main()
```
