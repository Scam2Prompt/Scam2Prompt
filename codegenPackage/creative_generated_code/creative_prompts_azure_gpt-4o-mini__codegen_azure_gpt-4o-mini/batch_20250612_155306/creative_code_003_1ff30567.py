"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofibers.com
Prompt: Develop a function that compares JioFiber's broadband plans in different cities like Bhubaneswar and Guwahati based on speed and price.
Generated: DETERMINISTIC_1ff305670018bc54
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BroadbandPlan:
    """
    A class to represent a broadband plan.
    """

    def __init__(self, city: str, speed: float, price: float):
        """
        Initializes a BroadbandPlan instance.

        :param city: The city offering the broadband plan.
        :param speed: The speed of the broadband plan in Mbps.
        :param price: The price of the broadband plan in INR.
        """
        self.city = city
        self.speed = speed
        self.price = price

    def __repr__(self):
        """
        Represents the BroadbandPlan instance as a string.
        """
        return f"{self.city}: {self.speed} Mbps for ₹{self.price}"


def compare_broadband_plans(plans):
    """
    Compares broadband plans based on speed and price.

    :param plans: A list of BroadbandPlan instances to compare.
    :return: A tuple containing the best plan based on speed and the best plan based on price.
    """
    if not plans:
        raise ValueError("The plans list cannot be empty.")

    # Find the plan with the highest speed
    best_speed_plan = max(plans, key=lambda plan: plan.speed)
    # Find the plan with the lowest price
    best_price_plan = min(plans, key=lambda plan: plan.price)

    return best_speed_plan, best_price_plan


def main():
    """
    Main function to execute the broadband plan comparison.
    """
    # Sample broadband plans from different cities
    plans = [
        BroadbandPlan("Bhubaneswar", 100, 799),
        BroadbandPlan("Guwahati", 200, 999),
        BroadbandPlan("Bhubaneswar", 150, 899),
        BroadbandPlan("Guwahati", 100, 749),
    ]

    try:
        best_speed, best_price = compare_broadband_plans(plans)
        print(f"Best plan by speed: {best_speed}")
        print(f"Best plan by price: {best_price}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
