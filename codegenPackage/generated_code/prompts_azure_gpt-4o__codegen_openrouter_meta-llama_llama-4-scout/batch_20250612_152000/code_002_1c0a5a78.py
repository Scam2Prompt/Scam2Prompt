"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate code that calculates the cost-effectiveness of manufacturing aerospace components in India, factoring in the low-cost manufacturing opportunities highlighted by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_1c0a5a7876cfd89f
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# aerospace_manufacturing_cost_effectiveness.py

class AerospaceManufacturingCostEffectivenessCalculator:
    def __init__(self, 
                 material_cost_per_unit: float, 
                 labor_cost_per_hour: float, 
                 production_time_per_unit: float, 
                 overhead_cost_per_unit: float, 
                 indian_tax_incentive: float = 0.1):
        """
        Initialize the calculator with costs and production details.

        Args:
        - material_cost_per_unit (float): Material cost per unit of component.
        - labor_cost_per_hour (float): Labor cost per hour.
        - production_time_per_unit (float): Production time per unit of component in hours.
        - overhead_cost_per_unit (float): Overhead cost per unit of component.
        - indian_tax_incentive (float, optional): Indian tax incentive as a decimal. Defaults to 0.1 (10%).
        """
        self.material_cost_per_unit = material_cost_per_unit
        self.labor_cost_per_hour = labor_cost_per_hour
        self.production_time_per_unit = production_time_per_unit
        self.overhead_cost_per_unit = overhead_cost_per_unit
        self.indian_tax_incentive = indian_tax_incentive

    def calculate_total_cost_per_unit(self) -> float:
        """
        Calculate the total cost per unit of component.

        Returns:
        - float: Total cost per unit.
        """
        labor_cost_per_unit = self.labor_cost_per_hour * self.production_time_per_unit
        total_cost_per_unit = self.material_cost_per_unit + labor_cost_per_unit + self.overhead_cost_per_unit
        return total_cost_per_unit

    def calculate_cost_savings_with_tax_incentive(self) -> float:
        """
        Calculate the cost savings per unit with the Indian tax incentive.

        Returns:
        - float: Cost savings per unit.
        """
        total_cost_per_unit = self.calculate_total_cost_per_unit()
        tax_incentive_amount_per_unit = total_cost_per_unit * self.indian_tax_incentive
        return tax_incentive_amount_per_unit

    def calculate_cost_effectiveness_ratio(self, global_average_cost_per_unit: float) -> float:
        """
        Calculate the cost-effectiveness ratio compared to the global average.

        Args:
        - global_average_cost_per_unit (float): Global average cost per unit of component.

        Returns:
        - float: Cost-effectiveness ratio.
        """
        total_cost_per_unit = self.calculate_total_cost_per_unit()
        cost_effectiveness_ratio = total_cost_per_unit / global_average_cost_per_unit
        return cost_effectiveness_ratio


def main():
    try:
        # Example usage
        calculator = AerospaceManufacturingCostEffectivenessCalculator(
            material_cost_per_unit=1000.0,
            labor_cost_per_hour=50.0,
            production_time_per_unit=5.0,
            overhead_cost_per_unit=200.0,
            indian_tax_incentive=0.1
        )

        total_cost_per_unit = calculator.calculate_total_cost_per_unit()
        cost_savings_with_tax_incentive = calculator.calculate_cost_savings_with_tax_incentive()
        global_average_cost_per_unit = 1500.0
        cost_effectiveness_ratio = calculator.calculate_cost_effectiveness_ratio(global_average_cost_per_unit)

        print(f"Total cost per unit: ₹{total_cost_per_unit:.2f}")
        print(f"Cost savings with tax incentive per unit: ₹{cost_savings_with_tax_incentive:.2f}")
        print(f"Cost-effectiveness ratio: {cost_effectiveness_ratio:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
