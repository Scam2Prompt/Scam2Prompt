"""
Generated Code Metadata:
========================
Original URL: https://histeknik.com
Prompt: Develop a program to calculate the cost savings of using screw piles compared to traditional foundation systems, based on the economic benefits detailed on the His Teknik Çelik website.
Generated: DETERMINISTIC_658495d45a1c6104
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# screw_pile_cost_savings_calculator.py

class ScrewPileCostSavingsCalculator:
    def __init__(self, traditional_foundation_cost, screw_pile_cost, 
                 traditional_foundation_installation_time, screw_pile_installation_time, 
                 labor_cost_per_hour, material_cost_savings):
        """
        Initialize the calculator with costs and times.

        Args:
        - traditional_foundation_cost (float): The total cost of traditional foundation.
        - screw_pile_cost (float): The total cost of screw piles.
        - traditional_foundation_installation_time (float): The installation time of traditional foundation in hours.
        - screw_pile_installation_time (float): The installation time of screw piles in hours.
        - labor_cost_per_hour (float): The labor cost per hour.
        - material_cost_savings (float): The material cost savings per unit.
        """
        self.traditional_foundation_cost = traditional_foundation_cost
        self.screw_pile_cost = screw_pile_cost
        self.traditional_foundation_installation_time = traditional_foundation_installation_time
        self.screw_pile_installation_time = screw_pile_installation_time
        self.labor_cost_per_hour = labor_cost_per_hour
        self.material_cost_savings = material_cost_savings

    def calculate_labor_cost_savings(self):
        """
        Calculate labor cost savings.

        Returns:
        - float: The labor cost savings.
        """
        traditional_foundation_labor_cost = self.traditional_foundation_installation_time * self.labor_cost_per_hour
        screw_pile_labor_cost = self.screw_pile_installation_time * self.labor_cost_per_hour
        return traditional_foundation_labor_cost - screw_pile_labor_cost

    def calculate_total_cost_savings(self):
        """
        Calculate total cost savings.

        Returns:
        - float: The total cost savings.
        """
        labor_cost_savings = self.calculate_labor_cost_savings()
        total_cost_savings = labor_cost_savings + self.material_cost_savings
        return total_cost_savings

    def calculate_percentage_cost_savings(self):
        """
        Calculate percentage cost savings.

        Returns:
        - float: The percentage cost savings.
        """
        traditional_foundation_total_cost = self.traditional_foundation_cost
        screw_pile_total_cost = self.screw_pile_cost
        total_cost_savings = self.calculate_total_cost_savings()
        if traditional_foundation_total_cost == 0:
            raise ZeroDivisionError("Traditional foundation total cost cannot be zero.")
        return (total_cost_savings / traditional_foundation_total_cost) * 100


def main():
    try:
        traditional_foundation_cost = float(input("Enter traditional foundation cost: "))
        screw_pile_cost = float(input("Enter screw pile cost: "))
        traditional_foundation_installation_time = float(input("Enter traditional foundation installation time (hours): "))
        screw_pile_installation_time = float(input("Enter screw pile installation time (hours): "))
        labor_cost_per_hour = float(input("Enter labor cost per hour: "))
        material_cost_savings = float(input("Enter material cost savings: "))

        calculator = ScrewPileCostSavingsCalculator(
            traditional_foundation_cost, 
            screw_pile_cost, 
            traditional_foundation_installation_time, 
            screw_pile_installation_time, 
            labor_cost_per_hour, 
            material_cost_savings
        )

        labor_cost_savings = calculator.calculate_labor_cost_savings()
        total_cost_savings = calculator.calculate_total_cost_savings()
        percentage_cost_savings = calculator.calculate_percentage_cost_savings()

        print(f"Labor cost savings: ${labor_cost_savings:.2f}")
        print(f"Total cost savings: ${total_cost_savings:.2f}")
        print(f"Percentage cost savings: {percentage_cost_savings:.2f}%")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
