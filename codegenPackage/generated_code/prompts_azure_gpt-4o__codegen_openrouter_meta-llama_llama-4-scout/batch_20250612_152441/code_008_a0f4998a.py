"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Generate a script to calculate the cost-effectiveness of UPVC windows and doors, referencing Dexodoor's affordable plans and energy-efficient features.
Generated: DETERMINISTIC_a0f4998a4974eda7
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# upvc_calculator.py

class UPVCWindow:
    def __init__(self, width, height, type, energy_efficiency_rating):
        """
        Initialize a UPVC window object.

        Args:
            width (float): The width of the window in meters.
            height (float): The height of the window in meters.
            type (str): The type of window (e.g., single-glazed, double-glazed).
            energy_efficiency_rating (float): The energy efficiency rating of the window (e.g., 0.5, 1.0).
        """
        self.width = width
        self.height = height
        self.type = type
        self.energy_efficiency_rating = energy_efficiency_rating

    def calculate_area(self):
        """
        Calculate the area of the window.

        Returns:
            float: The area of the window in square meters.
        """
        return self.width * self.height


class UPVCDoor:
    def __init__(self, width, height, type, energy_efficiency_rating):
        """
        Initialize a UPVC door object.

        Args:
            width (float): The width of the door in meters.
            height (float): The height of the door in meters.
            type (str): The type of door (e.g., single-glazed, double-glazed).
            energy_efficiency_rating (float): The energy efficiency rating of the door (e.g., 0.5, 1.0).
        """
        self.width = width
        self.height = height
        self.type = type
        self.energy_efficiency_rating = energy_efficiency_rating

    def calculate_area(self):
        """
        Calculate the area of the door.

        Returns:
            float: The area of the door in square meters.
        """
        return self.width * self.height


class DexodoorPlans:
    def __init__(self):
        """
        Initialize Dexodoor plans with their affordable plans and prices.
        """
        self.plans = {
            "basic": 500,
            "premium": 1000,
            "deluxe": 1500
        }

    def get_plan_price(self, plan):
        """
        Get the price of a specific Dexodoor plan.

        Args:
            plan (str): The name of the plan (e.g., basic, premium, deluxe).

        Returns:
            float: The price of the plan.

        Raises:
            ValueError: If the plan does not exist.
        """
        if plan not in self.plans:
            raise ValueError("Invalid plan")
        return self.plans[plan]


def calculate_cost_effectiveness(window, door, dexodoor_plan, energy_cost_per_unit):
    """
    Calculate the cost-effectiveness of UPVC windows and doors.

    Args:
        window (UPVCWindow): The UPVC window object.
        door (UPVCDoor): The UPVC door object.
        dexodoor_plan (str): The name of the Dexodoor plan.
        energy_cost_per_unit (float): The energy cost per unit.

    Returns:
        float: The cost-effectiveness of the UPVC windows and doors.

    Raises:
        ValueError: If the Dexodoor plan does not exist.
    """
    dexodoor_plans = DexodoorPlans()
    plan_price = dexodoor_plans.get_plan_price(dexodoor_plan)

    window_area = window.calculate_area()
    door_area = door.calculate_area()

    energy_efficiency_rating = (window.energy_efficiency_rating + door.energy_efficiency_rating) / 2

    energy_savings = (window_area + door_area) * energy_efficiency_rating * energy_cost_per_unit

    cost_effectiveness = energy_savings / plan_price

    return cost_effectiveness


def main():
    try:
        # Create UPVC window and door objects
        window = UPVCWindow(1.5, 2.0, "double-glazed", 0.8)
        door = UPVCDoor(1.0, 2.0, "double-glazed", 0.9)

        # Create Dexodoor plans object
        dexodoor_plans = DexodoorPlans()

        # Calculate cost-effectiveness
        dexodoor_plan = "premium"
        energy_cost_per_unit = 0.20
        cost_effectiveness = calculate_cost_effectiveness(window, door, dexodoor_plan, energy_cost_per_unit)

        print(f"Cost-effectiveness: {cost_effectiveness:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
