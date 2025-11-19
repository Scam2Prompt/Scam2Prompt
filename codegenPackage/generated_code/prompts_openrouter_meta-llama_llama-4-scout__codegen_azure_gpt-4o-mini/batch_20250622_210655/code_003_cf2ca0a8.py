"""
Generated Code Metadata:
========================
Original URL: https://bismillah-traders.com
Prompt: "Create a code snippet to calculate the cost estimation for a turnkey construction project, taking into account factors like materials, labor, and equipment, as discussed in Bismillah Traders' construction management services."
Generated: DETERMINISTIC_cf2ca0a8a3e555c1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TurnkeyConstructionEstimator:
    """
    A class to estimate the cost of a turnkey construction project.
    
    Attributes:
        materials_cost (float): Total cost of materials.
        labor_cost (float): Total cost of labor.
        equipment_cost (float): Total cost of equipment.
        overhead_percentage (float): Percentage of overhead costs.
    """

    def __init__(self, materials_cost: float, labor_cost: float, equipment_cost: float, overhead_percentage: float = 10.0):
        """
        Initializes the estimator with the given costs and overhead percentage.
        
        Args:
            materials_cost (float): Cost of materials.
            labor_cost (float): Cost of labor.
            equipment_cost (float): Cost of equipment.
            overhead_percentage (float): Overhead percentage (default is 10.0).
        """
        self.materials_cost = materials_cost
        self.labor_cost = labor_cost
        self.equipment_cost = equipment_cost
        self.overhead_percentage = overhead_percentage

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the construction project.
        
        Returns:
            float: Total estimated cost including overhead.
        """
        try:
            total_cost = (self.materials_cost + self.labor_cost + self.equipment_cost)
            overhead_cost = total_cost * (self.overhead_percentage / 100)
            total_cost_with_overhead = total_cost + overhead_cost
            return total_cost_with_overhead
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return 0.0

    def display_estimation(self):
        """
        Displays the cost estimation details.
        """
        total_cost = self.calculate_total_cost()
        print("Cost Estimation for Turnkey Construction Project:")
        print(f"Materials Cost: ${self.materials_cost:.2f}")
        print(f"Labor Cost: ${self.labor_cost:.2f}")
        print(f"Equipment Cost: ${self.equipment_cost:.2f}")
        print(f"Overhead Percentage: {self.overhead_percentage}%")
        print(f"Total Estimated Cost: ${total_cost:.2f}")


# Example usage
if __name__ == "__main__":
    # Initialize the estimator with example costs
    estimator = TurnkeyConstructionEstimator(materials_cost=50000, labor_cost=30000, equipment_cost=15000)
    
    # Display the cost estimation
    estimator.display_estimation()
```
