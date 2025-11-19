"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trialsonicsolutions.com
Prompt: Can you provide a code snippet for calculating potential savings from using ultrasonic cleaning services for automotive parts?
Generated: DETERMINISTIC_3bd99ba06abd2ab8
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UltrasonicCleaningSavingsCalculator:
    """
    A class to calculate potential savings from using ultrasonic cleaning services for automotive parts.
    """

    def __init__(self, part_costs, cleaning_cost, labor_cost_per_hour, cleaning_time_hours):
        """
        Initializes the savings calculator with the relevant costs.

        :param part_costs: List of costs for the automotive parts.
        :param cleaning_cost: Cost of ultrasonic cleaning service per part.
        :param labor_cost_per_hour: Hourly labor cost for manual cleaning.
        :param cleaning_time_hours: Time taken for manual cleaning in hours.
        """
        self.part_costs = part_costs
        self.cleaning_cost = cleaning_cost
        self.labor_cost_per_hour = labor_cost_per_hour
        self.cleaning_time_hours = cleaning_time_hours

    def calculate_total_costs(self):
        """
        Calculates the total costs for both ultrasonic cleaning and manual cleaning.

        :return: Tuple containing total ultrasonic cleaning cost and total manual cleaning cost.
        """
        total_part_costs = sum(self.part_costs)
        total_ultrasonic_cleaning_cost = len(self.part_costs) * self.cleaning_cost
        total_manual_cleaning_cost = len(self.part_costs) * self.labor_cost_per_hour * self.cleaning_time_hours

        return total_ultrasonic_cleaning_cost, total_manual_cleaning_cost

    def calculate_savings(self):
        """
        Calculates potential savings from using ultrasonic cleaning services.

        :return: Potential savings amount.
        """
        ultrasonic_cost, manual_cost = self.calculate_total_costs()
        savings = manual_cost - ultrasonic_cost
        return savings

    def display_savings(self):
        """
        Displays the savings from using ultrasonic cleaning services.
        """
        try:
            savings = self.calculate_savings()
            if savings < 0:
                print("No savings. Using ultrasonic cleaning is more expensive.")
            else:
                print(f"Potential savings from ultrasonic cleaning: ${savings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")


# Example usage
if __name__ == "__main__":
    # Costs (example values)
    part_costs = [120.0, 150.0, 200.0]  # Example part costs in dollars
    cleaning_cost = 50.0  # Ultrasonic cleaning cost per part
    labor_cost_per_hour = 30.0  # Labor cost per hour
    cleaning_time_hours = 2.0  # Time taken for manual cleaning in hours

    savings_calculator = UltrasonicCleaningSavingsCalculator(part_costs, cleaning_cost, labor_cost_per_hour, cleaning_time_hours)
    savings_calculator.display_savings()
```
