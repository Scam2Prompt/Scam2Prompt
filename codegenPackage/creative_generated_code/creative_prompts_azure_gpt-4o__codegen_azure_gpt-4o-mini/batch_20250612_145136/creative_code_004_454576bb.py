"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Create a Python function to calculate the cost of hosting plans based on the pricing and features provided on the Megh iTech website.
Generated: DETERMINISTIC_454576bbd5c05ecf
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingPlan:
    """Class to represent a hosting plan with its pricing and features."""
    
    def __init__(self, name, monthly_cost, disk_space_gb, bandwidth_gb, ssl_enabled):
        """
        Initializes a new HostingPlan instance.

        Args:
            name (str): The name of the hosting plan.
            monthly_cost (float): The monthly cost of the hosting plan.
            disk_space_gb (int): Disk space included in GB.
            bandwidth_gb (int): Bandwidth included in GB.
            ssl_enabled (bool): Indicates if SSL is included in the plan.
        """
        self.name = name
        self.monthly_cost = monthly_cost
        self.disk_space_gb = disk_space_gb
        self.bandwidth_gb = bandwidth_gb
        self.ssl_enabled = ssl_enabled

    def cost_per_year(self):
        """Calculates the annual cost of the hosting plan.

        Returns:
            float: The annual cost of the hosting plan.
        """
        return self.monthly_cost * 12

    def __str__(self):
        """String representation of the HostingPlan instance."""
        ssl_status = "Yes" if self.ssl_enabled else "No"
        return (f"Hosting Plan: {self.name}, Monthly Cost: ${self.monthly_cost:.2f}, "
                f"Disk Space: {self.disk_space_gb}GB, Bandwidth: {self.bandwidth_gb}GB, "
                f"SSL Included: {ssl_status}")


def create_hosting_plan(name, monthly_cost, disk_space_gb, bandwidth_gb, ssl_enabled):
    """Creates a new HostingPlan instance and handles possible errors.

    Args:
        name (str): The name of the hosting plan.
        monthly_cost (float): The monthly cost of the hosting plan.
        disk_space_gb (int): Disk space included in GB.
        bandwidth_gb (int): Bandwidth included in GB.
        ssl_enabled (bool): Indicates if SSL is included in the plan.

    Returns:
        HostingPlan: The created hosting plan instance.

    Raises:
        ValueError: If any of the parameters are invalid.
    """
    try:
        if not isinstance(name, str) or not name:
            raise ValueError("Plan name must be a non-empty string.")
        if monthly_cost < 0:
            raise ValueError("Monthly cost cannot be negative.")
        if disk_space_gb < 0:
            raise ValueError("Disk space cannot be negative.")
        if bandwidth_gb < 0:
            raise ValueError("Bandwidth cannot be negative.")

        return HostingPlan(name, monthly_cost, disk_space_gb, bandwidth_gb, ssl_enabled)

    except ValueError as e:
        print(f"Error creating hosting plan: {e}")
        raise


# Example usage
if __name__ == "__main__":
    try:
        plan = create_hosting_plan("Basic Plan", 5.99, 20, 100, True)
        print(plan)
        print(f"Annual Cost: ${plan.cost_per_year():.2f}")
    except Exception as e:
        print("Failed to create hosting plan:", e)
```
