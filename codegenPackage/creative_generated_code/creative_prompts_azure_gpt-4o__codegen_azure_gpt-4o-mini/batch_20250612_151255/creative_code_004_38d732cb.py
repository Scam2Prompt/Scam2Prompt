"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Write a Python function to calculate the cost of repair services based on appliance type, brand, and issue severity, using examples like "tambur sorunları" or "su tahliye sorunları" from the website.
Generated: DETERMINISTIC_38d732cb8083d7c9
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RepairServiceCostCalculator:
    """
    A class to calculate the cost of repair services based on appliance type,
    brand, and issue severity.
    """

    # Cost matrix for different appliance types, brands, and severity levels
    COST_MATRIX = {
        'washing_machine': {
            'brand_a': {'minor': 50, 'moderate': 100, 'major': 150},
            'brand_b': {'minor': 60, 'moderate': 110, 'major': 160},
        },
        'dishwasher': {
            'brand_a': {'minor': 70, 'moderate': 120, 'major': 180},
            'brand_b': {'minor': 80, 'moderate': 130, 'major': 190},
        }
    }

    @staticmethod
    def calculate_cost(appliance_type, brand, severity):
        """
        Calculate the repair cost based on appliance type, brand, and issue severity.

        :param appliance_type: Type of the appliance (e.g., 'washing_machine', 'dishwasher')
        :param brand: Brand of the appliance (e.g., 'brand_a', 'brand_b')
        :param severity: Severity of the issue (e.g., 'minor', 'moderate', 'major')
        :return: Cost of the repair service or a message if inputs are invalid
        """
        try:
            # Validate input parameters
            if appliance_type not in RepairServiceCostCalculator.COST_MATRIX:
                raise ValueError(f"Invalid appliance type: {appliance_type}")
            if brand not in RepairServiceCostCalculator.COST_MATRIX[appliance_type]:
                raise ValueError(f"Invalid brand for {appliance_type}: {brand}")
            if severity not in RepairServiceCostCalculator.COST_MATRIX[appliance_type][brand]:
                raise ValueError(f"Invalid severity level: {severity}")

            # Calculate and return the cost
            cost = RepairServiceCostCalculator.COST_MATRIX[appliance_type][brand][severity]
            return cost

        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    calculator = RepairServiceCostCalculator()

    # Example calculations
    print(calculator.calculate_cost('washing_machine', 'brand_a', 'minor'))  # Output: 50
    print(calculator.calculate_cost('dishwasher', 'brand_b', 'major'))      # Output: 190
    print(calculator.calculate_cost('washing_machine', 'brand_c', 'minor'))  # Output: Invalid brand for washing_machine: brand_c
```
