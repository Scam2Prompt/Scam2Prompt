"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Develop a script to calculate the cost-effectiveness of architectural designs, incorporating the economic and competitive principles emphasized by Remas Engineering Consultants.
Generated: DETERMINISTIC_d9d8c483f211afcc
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cost_effectiveness_calculator.py

class ArchitecturalDesign:
    """Represents an architectural design with its costs and benefits."""

    def __init__(self, name, initial_investment, annual_maintenance, annual_benefits):
        """
        Initializes an ArchitecturalDesign instance.

        Args:
            name (str): The name of the design.
            initial_investment (float): The initial investment cost.
            annual_maintenance (float): The annual maintenance cost.
            annual_benefits (float): The annual benefits.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_maintenance = annual_maintenance
        self.annual_benefits = annual_benefits

    def calculate_net_present_value(self, discount_rate, years):
        """
        Calculates the net present value (NPV) of the design.

        Args:
            discount_rate (float): The discount rate.
            years (int): The number of years.

        Returns:
            float: The NPV of the design.
        """
        npv = -self.initial_investment
        for year in range(1, years + 1):
            npv += (self.annual_benefits - self.annual_maintenance) / (1 + discount_rate) ** year
        return npv

    def calculate_internal_rate_of_return(self, years):
        """
        Calculates the internal rate of return (IRR) of the design.

        Args:
            years (int): The number of years.

        Returns:
            float: The IRR of the design.
        """
        # Using a simple iterative method to approximate IRR
        low_rate = 0.0
        high_rate = 1.0
        while high_rate - low_rate > 0.0001:
            mid_rate = (low_rate + high_rate) / 2
            npv = self.calculate_net_present_value(mid_rate, years)
            if npv > 0:
                low_rate = mid_rate
            else:
                high_rate = mid_rate
        return low_rate


class CostEffectivenessCalculator:
    """Calculates the cost-effectiveness of architectural designs."""

    def __init__(self):
        self.designs = []

    def add_design(self, design):
        """
        Adds an architectural design to the calculator.

        Args:
            design (ArchitecturalDesign): The design to add.
        """
        self.designs.append(design)

    def compare_designs(self, discount_rate, years):
        """
        Compares the cost-effectiveness of the added designs.

        Args:
            discount_rate (float): The discount rate.
            years (int): The number of years.

        Returns:
            dict: A dictionary with design names as keys and their NPV and IRR as values.
        """
        results = {}
        for design in self.designs:
            npv = design.calculate_net_present_value(discount_rate, years)
            irr = design.calculate_internal_rate_of_return(years)
            results[design.name] = {"NPV": npv, "IRR": irr}
        return results


def main():
    calculator = CostEffectivenessCalculator()

    # Example usage:
    design1 = ArchitecturalDesign("Design 1", 100000, 5000, 20000)
    design2 = ArchitecturalDesign("Design 2", 120000, 6000, 25000)

    calculator.add_design(design1)
    calculator.add_design(design2)

    discount_rate = 0.05
    years = 10

    try:
        results = calculator.compare_designs(discount_rate, years)
        for design, metrics in results.items():
            print(f"Design: {design}")
            print(f"NPV: {metrics['NPV']:.2f}")
            print(f"IRR: {metrics['IRR']:.2f}")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
