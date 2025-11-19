"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Write a Python script to calculate the cost of air conditioning repair services based on the pricing structure provided by RJW Mechanical in Fayetteville.
Generated: DETERMINISTIC_c07602d51a321f35
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# air_conditioning_repair.py

class AirConditioningRepair:
    """
    A class to calculate the cost of air conditioning repair services.
    """

    def __init__(self, base_rate: float, hourly_rate: float, parts_cost: float = 0.0):
        """
        Initialize the service with base rate and hourly rates.

        :param base_rate: The base service charge.
        :param hourly_rate: The hourly labor rate.
        :param parts_cost: The cost of any parts used in the repair (default is 0.0).
        """
        self.base_rate = base_rate
        self.hourly_rate = hourly_rate
        self.parts_cost = parts_cost

    def calculate_cost(self, hours_worked: float) -> float:
        """
        Calculate the total cost for the repair service.

        :param hours_worked: The number of hours spent on the repair.
        :return: Total cost of the repair service.
        """
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        total_cost = self.base_rate + (self.hourly_rate * hours_worked) + self.parts_cost
        return total_cost

def main():
    """
    Main function to execute the air conditioning repair cost calculation.
    """
    try:
        # Pricing structure for RJW Mechanical
        BASE_RATE = 90.00  # Base service charge
        HOURLY_RATE = 75.00  # Hourly labor rate

        # Get user input for hours worked and parts cost
        hours_worked = float(input("Enter the number of hours worked: "))
        parts_cost = float(input("Enter the cost of parts used (if any, else enter 0): "))

        # Instantiate the repair service
        repair_service = AirConditioningRepair(BASE_RATE, HOURLY_RATE, parts_cost)

        # Calculate total cost
        total_cost = repair_service.calculate_cost(hours_worked)

        # Display the total cost
        print(f"The total cost of air conditioning repair is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
