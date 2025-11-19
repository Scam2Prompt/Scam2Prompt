"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Write Python code to calculate the production capacity utilization for a company manufacturing Cold Drawn Carbon Steel Seamless Tubes, referencing LBIC Engineering Group's installed output capacity of 36,000 Metric Tonnes per annum.
Generated: DETERMINISTIC_8eb1693ed7ec9e98
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductionCapacityUtilization:
    """
    A class to calculate the production capacity utilization for a manufacturing company.
    """

    def __init__(self, installed_capacity: float):
        """
        Initializes the ProductionCapacityUtilization with the installed capacity.

        :param installed_capacity: The installed output capacity in Metric Tonnes per annum.
        """
        if installed_capacity <= 0:
            raise ValueError("Installed capacity must be a positive number.")
        self.installed_capacity = installed_capacity

    def calculate_utilization(self, actual_production: float) -> float:
        """
        Calculates the production capacity utilization percentage.

        :param actual_production: The actual production in Metric Tonnes.
        :return: The utilization percentage as a float.
        """
        if actual_production < 0:
            raise ValueError("Actual production cannot be negative.")
        
        utilization = (actual_production / self.installed_capacity) * 100
        return utilization

    def display_utilization(self, actual_production: float) -> None:
        """
        Displays the production capacity utilization.

        :param actual_production: The actual production in Metric Tonnes.
        """
        try:
            utilization = self.calculate_utilization(actual_production)
            print(f"Production Capacity Utilization: {utilization:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Installed output capacity for LBIC Engineering Group
    installed_capacity = 36000.0  # in Metric Tonnes per annum

    # Create an instance of ProductionCapacityUtilization
    capacity_utilization = ProductionCapacityUtilization(installed_capacity)

    # Example actual production value
    actual_production = 27000.0  # in Metric Tonnes

    # Display the utilization
    capacity_utilization.display_utilization(actual_production)
```
