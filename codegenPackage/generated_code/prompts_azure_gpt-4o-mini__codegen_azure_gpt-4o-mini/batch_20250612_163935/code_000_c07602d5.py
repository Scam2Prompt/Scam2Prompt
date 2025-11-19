"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Write a Python script to calculate the cost of air conditioning repair services based on the pricing structure provided by RJW Mechanical in Fayetteville.
Generated: DETERMINISTIC_c07602d51a321f35
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditioningRepairService:
    """
    A class to represent the air conditioning repair service pricing.
    """

    def __init__(self):
        # Pricing structure
        self.base_fee = 75.00  # Base fee for service call
        self.hourly_rate = 100.00  # Hourly rate for labor
        self.parts_cost = 0.0  # Cost of parts, initialized to zero

    def calculate_total_cost(self, hours_worked, parts_cost):
        """
        Calculate the total cost of the repair service.

        Parameters:
        hours_worked (float): The number of hours worked on the repair.
        parts_cost (float): The cost of any parts used in the repair.

        Returns:
        float: The total cost of the repair service.
        """
        if hours_worked < 0 or parts_cost < 0:
            raise ValueError("Hours worked and parts cost must be non-negative.")

        self.parts_cost = parts_cost
        total_cost = self.base_fee + (self.hourly_rate * hours_worked) + self.parts_cost
        return total_cost

def main():
    """
    Main function to execute the air conditioning repair cost calculation.
    """
    service = AirConditioningRepairService()

    try:
        # Input: hours worked and parts cost
        hours_worked = float(input("Enter the number of hours worked: "))
        parts_cost = float(input("Enter the cost of parts used: "))

        # Calculate total cost
        total_cost = service.calculate_total_cost(hours_worked, parts_cost)

        # Output the total cost
        print(f"The total cost of the air conditioning repair service is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
```
