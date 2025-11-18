"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write Python code to calculate the production capacity utilization for a company manufacturing Cold Drawn Carbon Steel Seamless Tubes, referencing LBIC Engineering Group's installed output capacity of 36,000 Metric Tonnes per annum.
Generated: DETERMINISTIC_8eb1693ed7ec9e98
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ProductionCapacityUtilization:
    """
    A class to calculate the production capacity utilization of a company.

    Attributes:
        installed_capacity (float): The installed output capacity in metric tonnes per annum.
        actual_production (float): The actual production in metric tonnes per annum.
    """

    def __init__(self, installed_capacity: float, actual_production: float):
        """
        Initializes the ProductionCapacityUtilization with installed capacity and actual production.

        Parameters:
            installed_capacity (float): The total capacity available for production.
            actual_production (float): The actual production amount.
        """
        self.installed_capacity = installed_capacity
        self.actual_production = actual_production

    def calculate_utilization(self) -> float:
        """
        Calculates the production capacity utilization percentage.

        Returns:
            float: The utilization percentage.
        
        Raises:
            ValueError: If installed_capacity is zero or negative.
        """
        if self.installed_capacity <= 0:
            raise ValueError("Installed capacity must be greater than zero.")

        utilization = (self.actual_production / self.installed_capacity) * 100
        return utilization

if __name__ == "__main__":
    try:
        # Installed output capacity in metric tonnes per annum
        installed_capacity = 36000.0  # LBIC Engineering Group's capacity
        # Example actual production value (this can be modified)
        actual_production = 27000.0  # Example actual production value

        # Create an instance of the ProductionCapacityUtilization class
        capacity_utilization = ProductionCapacityUtilization(installed_capacity, actual_production)

        # Calculate utilization
        utilization_percentage = capacity_utilization.calculate_utilization()

        # Print the utilization percentage
        print(f"Production Capacity Utilization: {utilization_percentage:.2f}%")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
