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
# internet_plan_comparator.py

class InternetPlan:
    """Represents an internet plan with speed and price."""

    def __init__(self, speed_mega, price_reais):
        """
        Initializes an InternetPlan instance.

        Args:
            speed_mega (int): The speed of the plan in mega.
            price_reais (float): The price of the plan in reais.
        """
        self.speed_mega = speed_mega
        self.price_reais = price_reais

    def __repr__(self):
        return f"InternetPlan(speed={self.speed_mega} MEGA, price=R${self.price_reais:.2f})"


def calculate_best_value(plans):
    """
    Calculates the best value internet plan.

    Args:
        plans (list[InternetPlan]): A list of internet plans.

    Returns:
        InternetPlan: The plan with the best value (price per mega).

    Raises:
        ValueError: If the input list is empty.
    """
    if not plans:
        raise ValueError("Input list cannot be empty")

    best_plan = min(plans, key=lambda plan: plan.price_reais / plan.speed_mega)
    return best_plan


def main():
    try:
        # Define internet plans
        plans = [
            InternetPlan(333, 99.90),
            InternetPlan(555, 109.90),
            InternetPlan(888, 129.90),
        ]

        # Calculate best value plan
        best_plan = calculate_best_value(plans)

        # Print plans and best value plan
        print("Internet Plans:")
        for plan in plans:
            print(plan)

        print(f"\nBest Value Plan: {best_plan}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
