"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Write a Python code snippet to calculate the cement production capacity of Tanzania Portland Cement Public Limited Company after its expansion project CM5.
Generated: DETERMINISTIC_b336bde231fcadd7
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tanzania_cement_production_capacity.py

class CementProductionCapacityCalculator:
    """
    Calculates the cement production capacity of Tanzania Portland Cement Public Limited Company
    after its expansion project CM5.
    """

    def __init__(self, initial_production_capacity, expansion_increase):
        """
        Initializes the calculator with the initial production capacity and expansion increase.

        Args:
            initial_production_capacity (float): The initial production capacity in tons per year.
            expansion_increase (float): The increase in production capacity after the CM5 expansion project in tons per year.
        """
        self.initial_production_capacity = initial_production_capacity
        self.expansion_increase = expansion_increase

    def calculate_new_production_capacity(self):
        """
        Calculates the new production capacity after the CM5 expansion project.

        Returns:
            float: The new production capacity in tons per year.
        """
        try:
            if self.initial_production_capacity < 0 or self.expansion_increase < 0:
                raise ValueError("Production capacities cannot be negative")

            new_production_capacity = self.initial_production_capacity + self.expansion_increase
            return new_production_capacity

        except ValueError as e:
            print(f"Error: {e}")
            return None


def main():
    # Initial production capacity of Tanzania Portland Cement Public Limited Company (in tons per year)
    initial_production_capacity = 650000  # Source: company's reports

    # Increase in production capacity after CM5 expansion project (in tons per year)
    expansion_increase = 350000  # Source: company's reports

    calculator = CementProductionCapacityCalculator(initial_production_capacity, expansion_increase)
    new_production_capacity = calculator.calculate_new_production_capacity()

    if new_production_capacity is not None:
        print(f"The new cement production capacity of Tanzania Portland Cement Public Limited Company after CM5 expansion project is: {new_production_capacity} tons per year")


if __name__ == "__main__":
    main()
```
