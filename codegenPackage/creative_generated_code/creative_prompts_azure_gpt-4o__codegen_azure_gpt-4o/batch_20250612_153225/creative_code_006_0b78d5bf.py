"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trindadetelecom.com.br
Prompt: Develop a script to compare internet plans based on speed, price, and latency, using the specific plan details ("333 MEGA," "555 MEGA," "888 MEGA") provided by Trindade Telecom.
Generated: DETERMINISTIC_0b78d5bf72ded01c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# internet_plan_comparison.py

import sys

class InternetPlan:
    """Class to represent an internet plan with speed, price, and latency attributes."""

    def __init__(self, name, speed, price, latency):
        """
        Initialize an InternetPlan object.

        :param name: Name of the plan
        :param speed: Internet speed in Mbps
        :param price: Monthly price of the plan
        :param latency: Network latency in ms
        """
        self.name = name
        self.speed = speed
        self.price = price
        self.latency = latency

    def value_for_money(self):
        """
        Calculate the value-for-money score for the plan.

        :return: Speed-to-price ratio (Mbps/$)
        """
        if self.price == 0:
            return float('inf')  # Avoid division by zero, treat as best value
        return self.speed / self.price

    def __str__(self):
        """
        Return a string representation of the plan.

        :return: A string summarizing the plan details
        """
        return f"Plan: {self.name}, Speed: {self.speed} Mbps, Price: ${self.price}, Latency: {self.latency} ms"


def compare_plans(plans):
    """
    Compare internet plans based on value-for-money, latency, and speed.

    :param plans: List of InternetPlan objects
    :return: None
    """
    if not plans:
        print("Error: No plans provided.")
        return

    # Best plan based on value-for-money
    best_value_plan = max(plans, key=lambda plan: plan.value_for_money())

    # Best plan based on lowest latency
    best_latency_plan = min(plans, key=lambda plan: plan.latency)

    # Best plan based on highest speed
    best_speed_plan = max(plans, key=lambda plan: plan.speed)

    # Print comparison results
    print("Internet Plan Comparison:")
    print("-------------------------")
    print("Best Value-for-Money Plan:")
    print(best_value_plan)
    print("\nBest Low-Latency Plan:")
    print(best_latency_plan)
    print("\nBest High-Speed Plan:")
    print(best_speed_plan)


def main():
    """
    Main function to demonstrate the comparison of internet plans.
    """
    try:
        # Define internet plans (provided by Trindade Telecom)
        plans = [
            InternetPlan("333 MEGA", speed=333, price=49.99, latency=15),
            InternetPlan("555 MEGA", speed=555, price=79.99, latency=12),
            InternetPlan("888 MEGA", speed=888, price=119.99, latency=10),
        ]

        # Compare the plans
        compare_plans(plans)

    except Exception as e:
        # Catch and report any unexpected error
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point for the script
    main()
```
