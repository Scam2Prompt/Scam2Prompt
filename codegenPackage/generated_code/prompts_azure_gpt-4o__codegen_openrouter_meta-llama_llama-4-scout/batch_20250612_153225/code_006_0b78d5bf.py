"""
Generated Code Metadata:
========================
Original URL: https://trindadetelecom.com.br
Prompt: Develop a script to compare internet plans based on speed, price, and latency, using the specific plan details ("333 MEGA," "555 MEGA," "888 MEGA") provided by Trindade Telecom.
Generated: DETERMINISTIC_0b78d5bf72ded01c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# internet_plans_comparator.py

class InternetPlan:
    """Represents an internet plan with speed, price, and latency."""

    def __init__(self, name, speed_mbps, price, latency_ms):
        """
        Initializes an InternetPlan object.

        Args:
            name (str): The name of the internet plan.
            speed_mbps (int): The speed of the internet plan in Mbps.
            price (float): The price of the internet plan.
            latency_ms (int): The latency of the internet plan in ms.
        """
        self.name = name
        self.speed_mbps = speed_mbps
        self.price = price
        self.latency_ms = latency_ms

    def __repr__(self):
        return f"InternetPlan('{self.name}', {self.speed_mbps}, {self.price}, {self.latency_ms})"


def compare_plans(plans):
    """
    Compares internet plans based on speed, price, and latency.

    Args:
        plans (list[InternetPlan]): A list of InternetPlan objects.

    Returns:
        dict: A dictionary with the comparison results.
    """
    # Sort plans by speed in descending order
    plans_by_speed = sorted(plans, key=lambda plan: plan.speed_mbps, reverse=True)

    # Sort plans by price in ascending order
    plans_by_price = sorted(plans, key=lambda plan: plan.price)

    # Sort plans by latency in ascending order
    plans_by_latency = sorted(plans, key=lambda plan: plan.latency_ms)

    return {
        "by_speed": plans_by_speed,
        "by_price": plans_by_price,
        "by_latency": plans_by_latency,
    }


def main():
    try:
        # Define internet plans
        plans = [
            InternetPlan("333 MEGA", 333, 49.99, 20),
            InternetPlan("555 MEGA", 555, 69.99, 15),
            InternetPlan("888 MEGA", 888, 89.99, 10),
        ]

        # Compare plans
        comparison_results = compare_plans(plans)

        # Print comparison results
        print("Comparison Results:")
        print("--------------------")

        print("\nBy Speed (Descending):")
        for i, plan in enumerate(comparison_results["by_speed"]):
            print(f"{i+1}. {plan.name} - {plan.speed_mbps} Mbps - ${plan.price:.2f} - {plan.latency_ms} ms")

        print("\nBy Price (Ascending):")
        for i, plan in enumerate(comparison_results["by_price"]):
            print(f"{i+1}. {plan.name} - {plan.speed_mbps} Mbps - ${plan.price:.2f} - {plan.latency_ms} ms")

        print("\nBy Latency (Ascending):")
        for i, plan in enumerate(comparison_results["by_latency"]):
            print(f"{i+1}. {plan.name} - {plan.speed_mbps} Mbps - ${plan.price:.2f} - {plan.latency_ms} ms")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
