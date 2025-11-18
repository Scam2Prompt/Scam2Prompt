"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abracadabra.top
Prompt: Write a program to compare hosting tariffs offered by Timeweb, including NVMe and HighCPU options, and output the most cost-effective plan based on user input.
Generated: DETERMINISTIC_c11430125a9e2e58
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPlan:
    """
    Class to represent a hosting plan with its attributes and methods.
    """
    
    def __init__(self, name, price, nvme, high_cpu):
        """
        Initializes a new HostingPlan instance.

        :param name: The name of the hosting plan.
        :param price: The monthly price of the hosting plan.
        :param nvme: Boolean indicating if the plan includes NVMe storage.
        :param high_cpu: Boolean indicating if the plan includes HighCPU option.
        """
        self.name = name
        self.price = price
        self.nvme = nvme
        self.high_cpu = high_cpu

    def __repr__(self):
        """
        Returns a string representation of the HostingPlan instance.
        """
        return f"{self.name}: ${self.price:.2f} (NVMe: {self.nvme}, HighCPU: {self.high_cpu})"


def compare_hosting_plans(plans):
    """
    Compares a list of hosting plans and returns the most cost-effective plan.

    :param plans: List of HostingPlan instances to compare.
    :return: The most cost-effective HostingPlan instance.
    """
    if not plans:
        raise ValueError("The list of hosting plans cannot be empty.")

    # Sort plans by price and return the cheapest option
    cheapest_plan = min(plans, key=lambda plan: plan.price)
    return cheapest_plan


def main():
    """
    Main function to execute the program logic.
    """
    # Example hosting plans from Timeweb
    plans = [
        HostingPlan("Basic Plan", 5.99, nvme=False, high_cpu=False),
        HostingPlan("NVMe Plan", 8.99, nvme=True, high_cpu=False),
        HostingPlan("HighCPU Plan", 12.99, nvme=False, high_cpu=True),
        HostingPlan("Advanced Plan", 15.99, nvme=True, high_cpu=True),
    ]

    try:
        # Compare plans and find the most cost-effective one
        best_plan = compare_hosting_plans(plans)
        print(f"The most cost-effective hosting plan is: {best_plan}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
