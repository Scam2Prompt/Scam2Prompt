"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Write a Python script to compare internet plans with different speeds and prices, such as 333 MEGA for R$ 99,90, 555 MEGA for R$ 109,90, and 888 MEGA for R$ 129,90, and determine which one is the best value.
Generated: DETERMINISTIC_0108b372b3241eaf
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InternetPlan:
    """
    A class to represent an internet plan with speed and price.
    """

    def __init__(self, speed_mbps: int, price_brl: float):
        """
        Initializes an InternetPlan instance.

        :param speed_mbps: Speed of the internet plan in Mbps.
        :param price_brl: Price of the internet plan in Brazilian Reais (R$).
        """
        self.speed_mbps = speed_mbps
        self.price_brl = price_brl

    def value_per_mbps(self) -> float:
        """
        Calculates the value per Mbps of the internet plan.

        :return: Value in R$ per Mbps.
        """
        if self.speed_mbps <= 0:
            raise ValueError("Speed must be greater than zero.")
        return self.price_brl / self.speed_mbps


def compare_internet_plans(plans: list) -> InternetPlan:
    """
    Compares a list of internet plans and returns the one with the best value.

    :param plans: A list of InternetPlan instances.
    :return: The InternetPlan instance with the best value.
    """
    if not plans:
        raise ValueError("The list of plans cannot be empty.")

    best_plan = min(plans, key=lambda plan: plan.value_per_mbps())
    return best_plan


def main():
    """
    Main function to execute the comparison of internet plans.
    """
    # Define internet plans
    plans = [
        InternetPlan(speed_mbps=333, price_brl=99.90),
        InternetPlan(speed_mbps=555, price_brl=109.90),
        InternetPlan(speed_mbps=888, price_brl=129.90)
    ]

    try:
        best_plan = compare_internet_plans(plans)
        print(f"The best value plan is {best_plan.speed_mbps} MEGA for R$ {best_plan.price_brl:.2f}, "
              f"costing R$ {best_plan.value_per_mbps():.2f} per Mbps.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
