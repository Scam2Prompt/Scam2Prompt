"""
Generated Code Metadata:
========================
Original URL: https://getsonicsolutions.com
Prompt: "Write a Python script to calculate the cost savings of using ultrasonic cleaning services for industrial parts cleaning, considering factors like part longevity and reduced downtime."
Generated: DETERMINISTIC_b584e19a33fdd24e
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class UltrasonicCleaningCostCalculator:
    """
    A class to calculate cost savings from using ultrasonic cleaning services for industrial parts.
    Takes into account factors like part longevity, reduced downtime, and operational costs.
    """
    
    def __init__(self, traditional_cost_per_part: float, ultrasonic_cost_per_part: float,
                 traditional_downtime_hours: float, ultrasonic_downtime_hours: float,
                 hourly_labor_cost: float, traditional_part_lifespan: int,
                 ultrasonic_part_lifespan: int, parts_per_year: int):
        """
        Initialize the calculator with cost parameters.
        
        Args:
            traditional_cost_per_part (float): Cost per part with traditional cleaning
            ultrasonic_cost_per_part (float): Cost per part with ultrasonic cleaning
            traditional_downtime_hours (float): Downtime hours per cleaning (traditional)
            ultrasonic_downtime_hours (float): Downtime hours per cleaning (ultrasonic)
            hourly_labor_cost (float): Cost of labor per hour
            traditional_part_lifespan (int): Part lifespan in cleanings (traditional)
            ultrasonic_part_lifespan (int): Part lifespan in cleanings (ultrasonic)
            parts_per_year (int): Number of parts cleaned annually
        """
        self.validate_inputs(
            traditional_cost_per_part, ultrasonic_cost_per_part,
            traditional_downtime_hours, ultrasonic_downtime_hours,
            hourly_labor_cost, traditional_part_lifespan,
            ultrasonic_part_lifespan, parts_per_year
        )
        
        self.traditional_cost_per_part = traditional_cost_per_part
        self.ultrasonic_cost_per_part = ultrasonic_cost_per_part
        self.traditional_downtime_hours = traditional_downtime_hours
        self.ultrasonic_downtime_hours = ultrasonic_downtime_hours
        self.hourly_labor_cost = hourly_labor_cost
        self.traditional_part_lifespan = traditional_part_lifespan
        self.ultrasonic_part_lifespan = ultrasonic_part_lifespan
        self.parts_per_year = parts_per_year
    
    @staticmethod
    def validate_inputs(*args):
        """Validate that all inputs are positive numbers."""
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("All inputs must be positive numbers")
    
    def calculate_downtime_savings(self) -> float:
        """
        Calculate annual savings from reduced downtime.
        
        Returns:
            float: Annual downtime savings in dollars
        """
        traditional_downtime_cost = self.traditional_downtime_hours * self.hourly_labor_cost * self.parts_per_year
        ultrasonic_downtime_cost = self.ultrasonic_downtime_hours * self.hourly_labor_cost * self.parts_per_year
        return traditional_downtime_cost - ultrasonic_downtime_cost
    
    def calculate_part_replacement_savings(self) -> float:
        """
        Calculate annual savings from extended part lifespan.
        
        Returns:
            float: Annual part replacement savings in dollars
        """
        traditional_cleaning_cycles = math.ceil(self.parts_per_year / self.traditional_part_lifespan)
        ultrasonic_cleaning_cycles = math.ceil(self.parts_per_year / self.ultrasonic_part_lifespan)
        
        traditional_part_cost = traditional_cleaning_cycles * self.traditional_cost_per_part
        ultrasonic_part_cost = ultrasonic_cleaning_cycles * self.ultrasonic_cost_per_part
        
        return traditional_part_cost - ultrasonic_part_cost
    
    def calculate_total_annual_savings(self) -> float:
        """
        Calculate total annual cost savings.
        
        Returns:
            float: Total annual savings in dollars
        """
        downtime_savings = self.calculate_downtime_savings()
        part_savings = self.calculate_part_replacement_savings()
        return downtime_savings + part_savings
    
    def generate_report(self) -> dict:
        """
        Generate a comprehensive report of cost savings.
        
        Returns:
            dict: Dictionary containing all calculated metrics
        """
        return {
            "annual_downtime_savings": self.calculate_downtime_savings(),
            "annual_part_replacement_savings": self.calculate_part_replacement_savings(),
            "total_annual_savings": self.calculate_total_annual_savings(),
            "traditional_annual_cost": (
                (self.traditional_cost_per_part * self.parts_per_year) +
                (self.traditional_downtime_hours * self.hourly_labor_cost * self.parts_per_year)
            ),
            "ultrasonic_annual_cost": (
                (self.ultrasonic_cost_per_part * self.parts_per_year) +
                (self.ultrasonic_downtime_hours * self.hourly_labor_cost * self.parts_per_year)
            )
        }


def main():
    """Example usage of the UltrasonicCleaningCostCalculator."""
    try:
        # Example parameters (these would typically come from user input)
        calculator = UltrasonicCleaningCostCalculator(
            traditional_cost_per_part=5.50,
            ultrasonic_cost_per_part=3.75,
            traditional_downtime_hours=2.0,
            ultrasonic_downtime_hours=0.5,
            hourly_labor_cost=45.00,
            traditional_part_lifespan=50,
            ultrasonic_part_lifespan=75,
            parts_per_year=1000
        )
        
        report = calculator.generate_report()
        
        print("Ultrasonic Cleaning Cost Savings Report")
        print("--------------------------------------")
        print(f"Annual Downtime Savings: ${report['annual_downtime_savings']:,.2f}")
        print(f"Annual Part Replacement Savings: ${report['annual_part_replacement_savings']:,.2f}")
        print(f"Total Annual Savings: ${report['total_annual_savings']:,.2f}")
        print("\nCost Comparison")
        print(f"Traditional Annual Cost: ${report['traditional_annual_cost']:,.2f}")
        print(f"Ultrasonic Annual Cost: ${report['ultrasonic_annual_cost']:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
