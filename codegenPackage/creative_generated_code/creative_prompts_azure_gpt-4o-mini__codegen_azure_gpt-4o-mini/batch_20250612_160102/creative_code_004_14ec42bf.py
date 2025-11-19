"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://work-nest.online
Prompt: How does work-nest.online suggest maximizing earnings as a food delivery courier, and can you write a script that calculates potential earnings based on delivery frequency?
Generated: DETERMINISTIC_14ec42bf844e4444
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class DeliveryEarningsCalculator:
    """
    A class to calculate potential earnings for food delivery couriers
    based on delivery frequency and average earnings per delivery.
    """

    def __init__(self, average_earning_per_delivery: float, deliveries_per_hour: int):
        """
        Initializes the calculator with average earnings per delivery and delivery rate.

        :param average_earning_per_delivery: Average earning for each delivery
        :param deliveries_per_hour: Number of deliveries expected per hour
        """
        if average_earning_per_delivery < 0 or deliveries_per_hour <= 0:
            raise ValueError("Average earning per delivery must be non-negative and deliveries per hour must be positive.")
        
        self.average_earning_per_delivery = average_earning_per_delivery
        self.deliveries_per_hour = deliveries_per_hour

    def calculate_earnings(self, hours_worked: float) -> float:
        """
        Calculate potential earnings based on hours worked.

        :param hours_worked: Total hours worked
        :return: Total earnings calculated for the given hours
        """
        if hours_worked < 0:
            raise ValueError("Hours worked must be non-negative.")

        # Calculate total earnings
        total_deliveries = self.deliveries_per_hour * hours_worked
        total_earnings = total_deliveries * self.average_earning_per_delivery
        
        return total_earnings


def main():
    """
    Main function to execute the earnings calculator.
    """
    try:
        # User input for average earnings and delivery frequency
        average_earning_per_delivery = float(input("Enter average earnings per delivery: "))
        deliveries_per_hour = int(input("Enter average deliveries per hour: "))
        hours_worked = float(input("Enter hours worked: "))

        # Instantiate the earnings calculator
        calculator = DeliveryEarningsCalculator(average_earning_per_delivery, deliveries_per_hour)

        # Calculate potential earnings
        earnings = calculator.calculate_earnings(hours_worked)

        # Output the results
        print(f"Potential earnings for {hours_worked} hours of work: ${earnings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
