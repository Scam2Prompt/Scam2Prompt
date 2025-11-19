"""
Generated Code Metadata:
========================
Original URL: https://engenhariawpj.com
Prompt: Generate a script to estimate the cost of implementing StoTherm EIFS systems in a construction project, incorporating material and labor costs as described on the Engenharia WPJ website.
Generated: DETERMINISTIC_0414fdddf29b2faa
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# StoTherm EIFS System Cost Estimator

class StoThermEIFSCostEstimator:
    def __init__(self, 
                 area_in_square_meters, 
                 material_cost_per_square_meter, 
                 labor_cost_per_square_meter, 
                 waste_factor=0.1, 
                 profit_margin=0.15, 
                 tax_rate=0.08):
        """
        Initializes the StoTherm EIFS system cost estimator.

        Args:
        - area_in_square_meters (float): The area to be covered in square meters.
        - material_cost_per_square_meter (float): The material cost per square meter.
        - labor_cost_per_square_meter (float): The labor cost per square meter.
        - waste_factor (float, optional): The waste factor. Defaults to 0.1 (10%).
        - profit_margin (float, optional): The profit margin. Defaults to 0.15 (15%).
        - tax_rate (float, optional): The tax rate. Defaults to 0.08 (8%).
        """

        self.area_in_square_meters = area_in_square_meters
        self.material_cost_per_square_meter = material_cost_per_square_meter
        self.labor_cost_per_square_meter = labor_cost_per_square_meter
        self.waste_factor = waste_factor
        self.profit_margin = profit_margin
        self.tax_rate = tax_rate

    def calculate_total_material_cost(self):
        """
        Calculates the total material cost.

        Returns:
        - float: The total material cost.
        """
        return self.area_in_square_meters * self.material_cost_per_square_meter * (1 + self.waste_factor)

    def calculate_total_labor_cost(self):
        """
        Calculates the total labor cost.

        Returns:
        - float: The total labor cost.
        """
        return self.area_in_square_meters * self.labor_cost_per_square_meter

    def calculate_subtotal(self):
        """
        Calculates the subtotal (material cost + labor cost).

        Returns:
        - float: The subtotal.
        """
        return self.calculate_total_material_cost() + self.calculate_total_labor_cost()

    def calculate_profit(self):
        """
        Calculates the profit.

        Returns:
        - float: The profit.
        """
        return self.calculate_subtotal() * self.profit_margin

    def calculate_tax(self):
        """
        Calculates the tax.

        Returns:
        - float: The tax.
        """
        return self.calculate_subtotal() * self.tax_rate

    def calculate_total_cost(self):
        """
        Calculates the total cost.

        Returns:
        - float: The total cost.
        """
        return self.calculate_subtotal() + self.calculate_profit() + self.calculate_tax()


def main():
    try:
        area_in_square_meters = float(input("Enter the area in square meters: "))
        material_cost_per_square_meter = float(input("Enter the material cost per square meter: R$ "))
        labor_cost_per_square_meter = float(input("Enter the labor cost per square meter: R$ "))

        estimator = StoThermEIFSCostEstimator(area_in_square_meters, 
                                              material_cost_per_square_meter, 
                                              labor_cost_per_square_meter)

        print("\n**Cost Estimation Results:**")
        print(f"Total Material Cost: R$ {estimator.calculate_total_material_cost():.2f}")
        print(f"Total Labor Cost: R$ {estimator.calculate_total_labor_cost():.2f}")
        print(f"Subtotal: R$ {estimator.calculate_subtotal():.2f}")
        print(f"Profit: R$ {estimator.calculate_profit():.2f}")
        print(f"Tax: R$ {estimator.calculate_tax():.2f}")
        print(f"**Total Cost: R$ {estimator.calculate_total_cost():.2f}**")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
