"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Write code to calculate ROI based on labor savings, equipment maintenance, and energy cost reductions using OpSense's remote monitoring solution.
Generated: DETERMINISTIC_317207ed7a37371f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roi_calculator.py

class ROICalculator:
    """
    Calculates the Return on Investment (ROI) based on labor savings, 
    equipment maintenance, and energy cost reductions using OpSense's remote monitoring solution.
    """

    def __init__(self, 
                 labor_savings: float, 
                 equipment_maintenance_reduction: float, 
                 energy_cost_reduction: float, 
                 opsense_solution_cost: float, 
                 labor_savings_period: int = 12,  # in months
                 opsense_solution_lifetime: int = 12  # in months
                 ):
        """
        Initializes the ROICalculator.

        Args:
        - labor_savings (float): Monthly labor savings.
        - equipment_maintenance_reduction (float): Monthly equipment maintenance reduction.
        - energy_cost_reduction (float): Monthly energy cost reduction.
        - opsense_solution_cost (float): The cost of OpSense's remote monitoring solution.
        - labor_savings_period (int): The period of labor savings in months. Defaults to 12.
        - opsense_solution_lifetime (int): The lifetime of OpSense's solution in months. Defaults to 12.
        """

        self.labor_savings = labor_savings
        self.equipment_maintenance_reduction = equipment_maintenance_reduction
        self.energy_cost_reduction = energy_cost_reduction
        self.opsense_solution_cost = opsense_solution_cost
        self.labor_savings_period = labor_savings_period
        self.opsense_solution_lifetime = opsense_solution_lifetime

    def calculate_total_savings(self) -> float:
        """
        Calculates the total monthly savings.

        Returns:
        - float: The total monthly savings.
        """
        return self.labor_savings + self.equipment_maintenance_reduction + self.energy_cost_reduction

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of OpSense's solution over its lifetime.

        Returns:
        - float: The total cost of OpSense's solution.
        """
        return self.opsense_solution_cost

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI) in months.

        Returns:
        - float: The ROI in months.
        """
        total_savings = self.calculate_total_savings()
        total_cost = self.calculate_total_cost()

        if total_savings <= 0:
            raise ValueError("Total savings must be greater than zero.")

        roi = total_cost / total_savings

        return roi

    def calculate_payback_period(self) -> float:
        """
        Calculates the payback period in months.

        Returns:
        - float: The payback period in months.
        """
        return self.calculate_roi()

    def calculate_net_present_value(self, discount_rate: float) -> float:
        """
        Calculates the Net Present Value (NPV).

        Args:
        - discount_rate (float): The discount rate.

        Returns:
        - float: The NPV.
        """
        total_savings = self.calculate_total_savings()
        total_cost = self.calculate_total_cost()

        npv = -total_cost
        for i in range(self.opsense_solution_lifetime):
            npv += total_savings / (1 + discount_rate) ** (i + 1)

        return npv


def main():
    try:
        labor_savings = 1000.0  # example labor savings
        equipment_maintenance_reduction = 500.0  # example equipment maintenance reduction
        energy_cost_reduction = 2000.0  # example energy cost reduction
        opsense_solution_cost = 15000.0  # example OpSense solution cost

        roi_calculator = ROICalculator(
            labor_savings, 
            equipment_maintenance_reduction, 
            energy_cost_reduction, 
            opsense_solution_cost
        )

        roi = roi_calculator.calculate_roi()
        payback_period = roi_calculator.calculate_payback_period()
        npv = roi_calculator.calculate_net_present_value(discount_rate=0.01)

        print(f"ROI: {roi} months")
        print(f"Payback Period: {payback_period} months")
        print(f"NPV: ${npv:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
