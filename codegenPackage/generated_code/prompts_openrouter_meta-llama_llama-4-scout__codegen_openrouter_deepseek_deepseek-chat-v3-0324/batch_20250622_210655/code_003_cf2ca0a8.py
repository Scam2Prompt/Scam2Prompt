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
"""
Turnkey Construction Project Cost Estimator for Bismillah Traders Construction Management Services.
This script calculates the total cost estimation based on materials, labor, and equipment costs.
"""

class ConstructionCostEstimator:
    """
    A class to estimate the total cost of a turnkey construction project.
    """
    
    def __init__(self):
        """
        Initialize the estimator with default cost factors.
        """
        self.material_cost = 0.0
        self.labor_cost = 0.0
        self.equipment_cost = 0.0
        self.contingency_percentage = 0.1  # 10% contingency by default
        self.profit_margin = 0.15  # 15% profit margin by default
    
    def set_material_cost(self, cost: float) -> None:
        """
        Set the total material cost.
        
        Args:
            cost (float): Total material cost in currency units.
        """
        if cost < 0:
            raise ValueError("Material cost cannot be negative")
        self.material_cost = cost
    
    def set_labor_cost(self, cost: float) -> None:
        """
        Set the total labor cost.
        
        Args:
            cost (float): Total labor cost in currency units.
        """
        if cost < 0:
            raise ValueError("Labor cost cannot be negative")
        self.labor_cost = cost
    
    def set_equipment_cost(self, cost: float) -> None:
        """
        Set the total equipment cost.
        
        Args:
            cost (float): Total equipment cost in currency units.
        """
        if cost < 0:
            raise ValueError("Equipment cost cannot be negative")
        self.equipment_cost = cost
    
    def set_contingency(self, percentage: float) -> None:
        """
        Set the contingency percentage.
        
        Args:
            percentage (float): Contingency percentage (0 to 1).
        """
        if not 0 <= percentage <= 1:
            raise ValueError("Contingency percentage must be between 0 and 1")
        self.contingency_percentage = percentage
    
    def set_profit_margin(self, percentage: float) -> None:
        """
        Set the profit margin percentage.
        
        Args:
            percentage (float): Profit margin percentage (0 to 1).
        """
        if not 0 <= percentage <= 1:
            raise ValueError("Profit margin must be between 0 and 1")
        self.profit_margin = percentage
    
    def calculate_total_cost(self) -> float:
        """
        Calculate the total estimated cost including contingency and profit margin.
        
        Returns:
            float: Total estimated cost in currency units.
        """
        try:
            base_cost = self.material_cost + self.labor_cost + self.equipment_cost
            contingency = base_cost * self.contingency_percentage
            total_with_contingency = base_cost + contingency
            profit = total_with_contingency * self.profit_margin
            return total_with_contingency + profit
        except Exception as e:
            raise RuntimeError(f"Error calculating total cost: {str(e)}")

# Example usage
if __name__ == "__main__":
    estimator = ConstructionCostEstimator()
    
    try:
        estimator.set_material_cost(500000)
        estimator.set_labor_cost(300000)
        estimator.set_equipment_cost(200000)
        estimator.set_contingency(0.1)  # 10%
        estimator.set_profit_margin(0.15)  # 15%
        
        total_cost = estimator.calculate_total_cost()
        print(f"Total Estimated Cost: {total_cost:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Calculation error: {re}")
```
