"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Create a code example for implementing a fixed management fee structure in a property development project management tool.
Generated: DETERMINISTIC_5186ea8624b3ccb0
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PropertyDevelopmentProject:
    """
    A class to represent a property development project with a fixed management fee structure.
    """
    
    def __init__(self, project_name: str, total_project_cost: float, management_fee_percentage: float):
        """
        Initialize the PropertyDevelopmentProject instance.
        
        Args:
            project_name (str): Name of the project
            total_project_cost (float): Total cost of the project
            management_fee_percentage (float): Fixed percentage for management fee (e.g., 0.05 for 5%)
            
        Raises:
            ValueError: If any numeric parameter is negative
        """
        if total_project_cost < 0 or management_fee_percentage < 0:
            raise ValueError("Costs and fee percentages cannot be negative")
            
        self.project_name = project_name
        self.total_project_cost = total_project_cost
        self.management_fee_percentage = management_fee_percentage
        
    def calculate_management_fee(self) -> float:
        """
        Calculate the fixed management fee based on the total project cost.
        
        Returns:
            float: Calculated management fee amount
        """
        return self.total_project_cost * self.management_fee_percentage
    
    def total_project_cost_with_fee(self) -> float:
        """
        Calculate the total project cost including the management fee.
        
        Returns:
            float: Total project cost including management fee
        """
        return self.total_project_cost + self.calculate_management_fee()
    
    def __str__(self) -> str:
        """
        String representation of the project details.
        
        Returns:
            str: Formatted project information
        """
        return (
            f"Project: {self.project_name}\n"
            f"Total Project Cost: ${self.total_project_cost:,.2f}\n"
            f"Management Fee ({self.management_fee_percentage*100:.2f}%): ${self.calculate_management_fee():,.2f}\n"
            f"Total Cost with Fee: ${self.total_project_cost_with_fee():,.2f}"
        )


# Example usage
if __name__ == "__main__":
    try:
        # Create a project with $1,000,000 total cost and 3% management fee
        project = PropertyDevelopmentProject(
            project_name="Downtown Tower",
            total_project_cost=1000000,
            management_fee_percentage=0.03
        )
        
        # Print project details
        print(project)
        
    except ValueError as e:
        print(f"Error creating project: {e}")
```
