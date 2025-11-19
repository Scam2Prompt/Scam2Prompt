"""
Generated Code Metadata:
========================
Original URL: https://trialsonicsolutions.com
Prompt: Provide an example of a case study where ultrasonic cleaning significantly reduced downtime and costs for a manufacturing company.
Generated: DETERMINISTIC_a5003f9bb4927a90
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study Simulation: Ultrasonic Cleaning Impact on Manufacturing Downtime and Costs

This script simulates a case study where ultrasonic cleaning technology is implemented in a manufacturing company.
The simulation compares downtime and costs before and after adopting ultrasonic cleaning.
"""

import random

class ManufacturingCompany:
    def __init__(self, name, downtime_hours, cleaning_cost, production_loss_cost):
        """
        Initialize the manufacturing company with relevant attributes.

        :param name: Name of the company
        :param downtime_hours: Average downtime hours per month before ultrasonic cleaning
        :param cleaning_cost: Monthly cleaning cost before ultrasonic cleaning
        :param production_loss_cost: Monthly production loss cost due to downtime
        """
        self.name = name
        self.downtime_hours = downtime_hours
        self.cleaning_cost = cleaning_cost
        self.production_loss_cost = production_loss_cost

    def apply_ultrasonic_cleaning(self, downtime_reduction_percentage, cleaning_cost_reduction_percentage):
        """
        Apply ultrasonic cleaning and calculate new downtime and costs.

        :param downtime_reduction_percentage: Percentage reduction in downtime hours
        :param cleaning_cost_reduction_percentage: Percentage reduction in cleaning costs
        :return: Dictionary containing updated downtime and costs
        """
        try:
            new_downtime_hours = self.downtime_hours * (1 - downtime_reduction_percentage / 100)
            new_cleaning_cost = self.cleaning_cost * (1 - cleaning_cost_reduction_percentage / 100)
            new_production_loss_cost = self.production_loss_cost * (new_downtime_hours / self.downtime_hours)

            return {
                "new_downtime_hours": round(new_downtime_hours, 2),
                "new_cleaning_cost": round(new_cleaning_cost, 2),
                "new_production_loss_cost": round(new_production_loss_cost, 2),
            }
        except Exception as e:
            print(f"Error during ultrasonic cleaning simulation: {e}")
            return None

    def calculate_total_cost(self, cleaning_cost, production_loss_cost):
        """
        Calculate the total monthly cost.

        :param cleaning_cost: Monthly cleaning cost
        :param production_loss_cost: Monthly production loss cost
        :return: Total monthly cost
        """
        return round(cleaning_cost + production_loss_cost, 2)


def simulate_case_study():
    """
    Simulate the case study for a manufacturing company adopting ultrasonic cleaning.
    """
    # Initialize company data
    company = ManufacturingCompany(
        name="Precision Manufacturing Co.",
        downtime_hours=120,  # hours per month
        cleaning_cost=5000,  # USD per month
        production_loss_cost=20000  # USD per month
    )

    print(f"Case Study: {company.name}")
    print(f"Before Ultrasonic Cleaning:")
    print(f"  Downtime Hours: {company.downtime_hours} hours/month")
    print(f"  Cleaning Cost: ${company.cleaning_cost}/month")
    print(f"  Production Loss Cost: ${company.production_loss_cost}/month")
    print(f"  Total Monthly Cost: ${company.calculate_total_cost(company.cleaning_cost, company.production_loss_cost)}\n")

    # Apply ultrasonic cleaning with a simulated reduction in downtime and cleaning costs
    downtime_reduction_percentage = random.uniform(30, 50)  # Simulate 30-50% reduction
    cleaning_cost_reduction_percentage = random.uniform(20, 40)  # Simulate 20-40% reduction

    results = company.apply_ultrasonic_cleaning(downtime_reduction_percentage, cleaning_cost_reduction_percentage)

    if results:
        print(f"After Ultrasonic Cleaning:")
        print(f"  Downtime Reduction: {downtime_reduction_percentage:.2f}%")
        print(f"  Cleaning Cost Reduction: {cleaning_cost_reduction_percentage:.2f}%")
        print(f"  Downtime Hours: {results['new_downtime_hours']} hours/month")
        print(f"  Cleaning Cost: ${results['new_cleaning_cost']}/month")
        print(f"  Production Loss Cost: ${results['new_production_loss_cost']}/month")
        print(f"  Total Monthly Cost: ${company.calculate_total_cost(results['new_cleaning_cost'], results['new_production_loss_cost'])}\n")

        # Calculate monthly savings
        original_total_cost = company.calculate_total_cost(company.cleaning_cost, company.production_loss_cost)
        new_total_cost = company.calculate_total_cost(results['new_cleaning_cost'], results['new_production_loss_cost'])
        savings = original_total_cost - new_total_cost

        print(f"Monthly Savings: ${savings:.2f}")
    else:
        print("Simulation failed due to an error.")


if __name__ == "__main__":
    simulate_case_study()
```
