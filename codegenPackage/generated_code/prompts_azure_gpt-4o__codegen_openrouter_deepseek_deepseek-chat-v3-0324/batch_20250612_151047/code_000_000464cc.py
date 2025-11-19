"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write Python code to calculate the cost estimate for a civil works project, including building painting, tile installation, gypsum board work, and electrical and plumbing services, as described on the AKNAN website.
Generated: DETERMINISTIC_000464cc28579864
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Civil Works Cost Estimator

This script calculates the cost estimate for a civil works project based on the following components:
- Building painting
- Tile installation
- Gypsum board work
- Electrical services
- Plumbing services

The cost is calculated per square meter for each component and summed up for the total project cost.
"""

class CivilWorksCostEstimator:
    def __init__(self):
        """Initialize the cost estimator with default rates per square meter."""
        self.rates = {
            'painting': 50,          # in currency per sqm
            'tile_installation': 80, # in currency per sqm
            'gypsum_board': 60,      # in currency per sqm
            'electrical': 40,        # in currency per sqm
            'plumbing': 70           # in currency per sqm
        }

    def calculate_cost(self, area):
        """
        Calculate the total cost for the civil works project.

        Args:
            area (float): Total area in square meters.

        Returns:
            dict: A dictionary containing cost breakdown and total cost.
        
        Raises:
            ValueError: If area is not a positive number.
        """
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Area must be a positive number.")

        cost_breakdown = {
            'painting': self.rates['painting'] * area,
            'tile_installation': self.rates['tile_installation'] * area,
            'gypsum_board': self.rates['gypsum_board'] * area,
            'electrical': self.rates['electrical'] * area,
            'plumbing': self.rates['plumbing'] * area
        }

        total_cost = sum(cost_breakdown.values())

        return {
            'cost_breakdown': cost_breakdown,
            'total_cost': total_cost
        }

    def update_rate(self, component, new_rate):
        """
        Update the rate for a specific component.

        Args:
            component (str): The component to update (e.g., 'painting').
            new_rate (float): New rate per square meter.

        Raises:
            ValueError: If component is invalid or new_rate is not positive.
        """
        if component not in self.rates:
            raise ValueError(f"Invalid component: {component}. Must be one of {list(self.rates.keys())}")

        if not isinstance(new_rate, (int, float)) or new_rate <= 0:
            raise ValueError("Rate must be a positive number.")

        self.rates[component] = new_rate


# Example usage
if __name__ == "__main__":
    try:
        estimator = CivilWorksCostEstimator()
        area = float(input("Enter the total area in square meters: "))
        
        result = estimator.calculate_cost(area)
        
        print("\nCost Breakdown:")
        for component, cost in result['cost_breakdown'].items():
            print(f"{component.replace('_', ' ').title()}: {cost:.2f}")
        
        print(f"\nTotal Estimated Cost: {result['total_cost']:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
