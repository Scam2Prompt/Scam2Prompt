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
class VPSHostingPlan:
    """
    A class to represent a VPS hosting plan.
    """

    def __init__(self, name, ram_mb, cpu_cores, disk_space_gb, price):
        """
        Initializes a new VPS hosting plan.

        :param name: Name of the hosting plan
        :param ram_mb: Amount of RAM in MB
        :param cpu_cores: Number of CPU cores
        :param disk_space_gb: Disk space in GB
        :param price: Monthly price of the plan
        """
        self.name = name
        self.ram_mb = ram_mb
        self.cpu_cores = cpu_cores
        self.disk_space_gb = disk_space_gb
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the VPS hosting plan.
        """
        return (f"Plan: {self.name}, RAM: {self.ram_mb} MB, "
                f"CPU: {self.cpu_cores} Cores, Disk Space: {self.disk_space_gb} GB, "
                f"Price: ${self.price}/month")

def compare_vps_plans(plans):
    """
    Compares VPS hosting plans and recommends the best one for a small business website.

    :param plans: List of VPSHostingPlan objects
    :return: Recommended plan for small business
    """
    best_plan = None
    for plan in plans:
        # Simple criteria for recommendation: prioritize RAM, then CPU, then Disk Space
        if best_plan is None or (
            (plan.ram_mb > best_plan.ram_mb) or
            (plan.ram_mb == best_plan.ram_mb and plan.cpu_cores > best_plan.cpu_cores) or
            (plan.ram_mb == best_plan.ram_mb and plan.cpu_cores == best_plan.cpu_cores and plan.disk_space_gb > best_plan.disk_space_gb)
        ):
            best_plan = plan
    return best_plan

def main():
    """
    Main function to execute the VPS hosting plan comparison.
    """
    try:
        # Define VPS hosting plans
        plans = [
            VPSHostingPlan("Basic Plan", 512, 1, 20, 10),
            VPSHostingPlan("Standard Plan", 1024, 2, 40, 20),
            VPSHostingPlan("Premium Plan", 2048, 4, 80, 40)
        ]

        # Compare plans and get the best one for a small business
        recommended_plan = compare_vps_plans(plans)

        # Output the recommended plan
        if recommended_plan:
            print("Recommended VPS Hosting Plan for Small Business:")
            print(recommended_plan)
        else:
            print("No suitable VPS hosting plan found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
