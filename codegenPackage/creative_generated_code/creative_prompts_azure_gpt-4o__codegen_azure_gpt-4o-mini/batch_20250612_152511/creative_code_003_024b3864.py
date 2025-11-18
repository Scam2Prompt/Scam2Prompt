"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Write code to calculate repair costs for Whirlpool appliances based on the type of appliance (e.g., hornos, campanas) and complexity of the issue, using the pricing transparency mentioned on the website.
Generated: DETERMINISTIC_024b38647662b3c9
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ApplianceRepairCostCalculator:
    """Class to calculate repair costs for Whirlpool appliances."""

    # Pricing data based on appliance type and complexity of the issue
    # Prices are hypothetical and should be adjusted based on actual data
    pricing_data = {
        'horno': {
            'simple': 100,
            'moderate': 200,
            'complex': 300
        },
        'campana': {
            'simple': 80,
            'moderate': 150,
            'complex': 250
        }
    }

    def __init__(self, appliance_type: str, issue_complexity: str):
        """Initialize the calculator with appliance type and issue complexity.

        Args:
            appliance_type (str): The type of appliance (e.g., 'horno', 'campana').
            issue_complexity (str): The complexity of the issue (e.g., 'simple', 'moderate', 'complex').

        Raises:
            ValueError: If the appliance type or issue complexity is invalid.
        """
        self.appliance_type = appliance_type.lower()
        self.issue_complexity = issue_complexity.lower()

        if self.appliance_type not in self.pricing_data:
            raise ValueError(f"Invalid appliance type: {appliance_type}. Valid types are: {list(self.pricing_data.keys())}.")
        if self.issue_complexity not in self.pricing_data[self.appliance_type]:
            raise ValueError(f"Invalid issue complexity: {issue_complexity}. Valid complexities are: {list(self.pricing_data[self.appliance_type].keys())}.")

    def calculate_cost(self) -> float:
        """Calculate the repair cost based on the appliance type and issue complexity.

        Returns:
            float: The calculated repair cost.

        Raises:
            RuntimeError: If an unexpected error occurs during cost calculation.
        """
        try:
            cost = self.pricing_data[self.appliance_type][self.issue_complexity]
            return cost
        except Exception as e:
            raise RuntimeError("An error occurred while calculating the repair cost.") from e


def main():
    """Main function to execute the repair cost calculation."""
    # Example inputs (these could be gathered from user input in a production system)
    appliance_type = 'horno'  # or 'campana'
    issue_complexity = 'moderate'  # or 'simple', 'complex'

    try:
        calculator = ApplianceRepairCostCalculator(appliance_type, issue_complexity)
        cost = calculator.calculate_cost()
        print(f"The repair cost for a {appliance_type} with a {issue_complexity} issue is: ${cost}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
