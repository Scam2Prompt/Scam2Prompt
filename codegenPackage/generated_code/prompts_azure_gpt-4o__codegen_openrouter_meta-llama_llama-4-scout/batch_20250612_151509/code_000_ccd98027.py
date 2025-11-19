"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: Write a Python script to compare fiber internet subscription plans, including features like Flex packs with internet, mobile, and TV, as described on the Fiberdeals website.
Generated: DETERMINISTIC_ccd9802776f406b8
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fiber_plans_comparator.py

class FiberPlan:
    """Represents a fiber internet subscription plan."""

    def __init__(self, name, speed, price, features=None):
        """
        Initializes a FiberPlan object.

        Args:
            name (str): The name of the plan.
            speed (str): The speed of the plan (e.g., "100 Mbps").
            price (float): The monthly price of the plan.
            features (list[str], optional): A list of features. Defaults to None.
        """
        self.name = name
        self.speed = speed
        self.price = price
        self.features = features if features else []

    def __str__(self):
        return f"{self.name}: {self.speed} - ${self.price:.2f}/month"


class FlexPack:
    """Represents a Flex pack."""

    def __init__(self, name, internet, mobile, tv, price):
        """
        Initializes a FlexPack object.

        Args:
            name (str): The name of the Flex pack.
            internet (bool): Whether the Flex pack includes internet.
            mobile (bool): Whether the Flex pack includes mobile.
            tv (bool): Whether the Flex pack includes TV.
            price (float): The monthly price of the Flex pack.
        """
        self.name = name
        self.internet = internet
        self.mobile = mobile
        self.tv = tv
        self.price = price

    def __str__(self):
        features = []
        if self.internet:
            features.append("Internet")
        if self.mobile:
            features.append("Mobile")
        if self.tv:
            features.append("TV")
        return f"{self.name}: ${self.price:.2f}/month ({', '.join(features)})"


def compare_plans(plans):
    """
    Compares a list of fiber internet subscription plans.

    Args:
        plans (list[FiberPlan]): A list of FiberPlan objects.

    Returns:
        None
    """
    print("Fiber Internet Subscription Plans:")
    for plan in plans:
        print(plan)
        if plan.features:
            print("  Features:")
            for feature in plan.features:
                print(f"    - {feature}")
        print()


def compare_flex_packs(flex_packs):
    """
    Compares a list of Flex packs.

    Args:
        flex_packs (list[FlexPack]): A list of FlexPack objects.

    Returns:
        None
    """
    print("Flex Packs:")
    for flex_pack in flex_packs:
        print(flex_pack)


def main():
    try:
        # Define fiber internet subscription plans
        plans = [
            FiberPlan("Plan 1", "100 Mbps", 50.0, ["Flex Pack 1", "Free Installation"]),
            FiberPlan("Plan 2", "500 Mbps", 100.0, ["Flex Pack 2", "Free Modem"]),
            FiberPlan("Plan 3", "1 Gbps", 150.0, ["Flex Pack 3", "Free Router"]),
        ]

        # Define Flex packs
        flex_packs = [
            FlexPack("Flex Pack 1", True, False, False, 10.0),
            FlexPack("Flex Pack 2", True, True, False, 20.0),
            FlexPack("Flex Pack 3", True, True, True, 30.0),
        ]

        # Compare plans and Flex packs
        compare_plans(plans)
        compare_flex_packs(flex_packs)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
