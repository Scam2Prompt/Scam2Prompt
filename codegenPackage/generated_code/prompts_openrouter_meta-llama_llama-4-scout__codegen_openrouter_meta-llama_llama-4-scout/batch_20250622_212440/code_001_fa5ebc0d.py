"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: "Compare and contrast the features of IDN Hosting's VPS hosting plans, including the 512 MB RAM, 1 Cores CPU, 20 GB Disk Space plan, and recommend which plan is best suited for a small business website."
Generated: DETERMINISTIC_fa5ebc0d6b45a81b
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent a VPS hosting plan
class VPSHostingPlan:
    def __init__(self, name, ram, cpu, disk_space, price):
        """
        Initialize a VPS hosting plan.

        Args:
            name (str): The name of the plan.
            ram (int): The amount of RAM in MB.
            cpu (int): The number of CPU cores.
            disk_space (int): The amount of disk space in GB.
            price (float): The price of the plan.
        """
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.disk_space = disk_space
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.ram} MB RAM, {self.cpu} Cores CPU, {self.disk_space} GB Disk Space, ${self.price:.2f}"


# Define a function to compare VPS hosting plans
def compare_plans(plans):
    """
    Compare VPS hosting plans and recommend the best one for a small business website.

    Args:
        plans (list[VPSHostingPlan]): A list of VPS hosting plans.

    Returns:
        VPSHostingPlan: The recommended plan.
    """
    # Define the requirements for a small business website
    min_ram = 512  # MB
    min_cpu = 1  # Cores
    min_disk_space = 20  # GB

    # Filter plans that meet the minimum requirements
    eligible_plans = [plan for plan in plans if plan.ram >= min_ram and plan.cpu >= min_cpu and plan.disk_space >= min_disk_space]

    # If no plans meet the requirements, raise an exception
    if not eligible_plans:
        raise ValueError("No plans meet the minimum requirements")

    # Recommend the plan with the most resources
    recommended_plan = max(eligible_plans, key=lambda plan: (plan.ram, plan.cpu, plan.disk_space))

    return recommended_plan


# Define the IDN Hosting VPS hosting plans
plans = [
    VPSHostingPlan("Basic", 512, 1, 20, 5.99),
    VPSHostingPlan("Standard", 1024, 2, 40, 9.99),
    VPSHostingPlan("Premium", 2048, 4, 80, 19.99),
]

# Compare the plans and recommend the best one
try:
    recommended_plan = compare_plans(plans)
    print("Recommended plan:")
    print(recommended_plan)

    # Print a comparison of all plans
    print("\nPlan comparison:")
    for plan in plans:
        print(plan)

except ValueError as e:
    print(f"Error: {e}")
```

```python
# Alternatively you could use a main guard 
if __name__ == "__main__":
    # Define the IDN Hosting VPS hosting plans
    plans = [
        VPSHostingPlan("Basic", 512, 1, 20, 5.99),
        VPSHostingPlan("Standard", 1024, 2, 40, 9.99),
        VPSHostingPlan("Premium", 2048, 4, 80, 19.99),
    ]

    # Compare the plans and recommend the best one
    try:
        recommended_plan = compare_plans(plans)
        print("Recommended plan:")
        print(recommended_plan)

        # Print a comparison of all plans
        print("\nPlan comparison:")
        for plan in plans:
            print(plan)

    except ValueError as e:
        print(f"Error: {e}")
```
