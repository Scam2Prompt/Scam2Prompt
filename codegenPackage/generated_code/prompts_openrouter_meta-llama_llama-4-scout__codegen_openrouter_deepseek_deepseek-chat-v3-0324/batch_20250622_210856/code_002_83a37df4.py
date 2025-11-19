"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a code snippet to calculate the cost of production for a custom cosmetic product, considering factors like raw material costs, labor, and packaging, as described in Fabricare Cosmeticos' full-service projects.
Generated: DETERMINISTIC_83a37df4b9b5f758
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CosmeticProductionCostCalculator:
    """
    A class to calculate the production cost of custom cosmetic products.
    Factors considered: raw materials, labor, packaging, and overhead costs.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default cost factors.
        """
        self.raw_material_cost_per_unit = 0.0
        self.labor_cost_per_unit = 0.0
        self.packaging_cost_per_unit = 0.0
        self.overhead_percentage = 0.15  # Default 15% overhead
    
    def set_raw_material_cost(self, cost_per_unit):
        """
        Set the raw material cost per unit.
        
        Args:
            cost_per_unit (float): Cost of raw materials per product unit
        """
        if cost_per_unit < 0:
            raise ValueError("Raw material cost cannot be negative")
        self.raw_material_cost_per_unit = cost_per_unit
    
    def set_labor_cost(self, cost_per_unit):
        """
        Set the labor cost per unit.
        
        Args:
            cost_per_unit (float): Labor cost per product unit
        """
        if cost_per_unit < 0:
            raise ValueError("Labor cost cannot be negative")
        self.labor_cost_per_unit = cost_per_unit
    
    def set_packaging_cost(self, cost_per_unit):
        """
        Set the packaging cost per unit.
        
        Args:
            cost_per_unit (float): Packaging cost per product unit
        """
        if cost_per_unit < 0:
            raise ValueError("Packaging cost cannot be negative")
        self.packaging_cost_per_unit = cost_per_unit
    
    def set_overhead_percentage(self, percentage):
        """
        Set the overhead percentage.
        
        Args:
            percentage (float): Overhead percentage (0-1)
        """
        if not 0 <= percentage <= 1:
            raise ValueError("Overhead percentage must be between 0 and 1")
        self.overhead_percentage = percentage
    
    def calculate_unit_cost(self, quantity=1):
        """
        Calculate the total production cost per unit.
        
        Args:
            quantity (int): Number of units to calculate cost for
            
        Returns:
            float: Total cost per unit including overhead
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        base_cost = (
            self.raw_material_cost_per_unit +
            self.labor_cost_per_unit +
            self.packaging_cost_per_unit
        )
        
        overhead_cost = base_cost * self.overhead_percentage
        total_cost_per_unit = base_cost + overhead_cost
        
        return total_cost_per_unit
    
    def calculate_total_cost(self, quantity):
        """
        Calculate the total production cost for a given quantity.
        
        Args:
            quantity (int): Number of units to produce
            
        Returns:
            float: Total production cost
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        unit_cost = self.calculate_unit_cost()
        return unit_cost * quantity


# Example usage
if __name__ == "__main__":
    try:
        calculator = CosmeticProductionCostCalculator()
        calculator.set_raw_material_cost(2.50)
        calculator.set_labor_cost(1.20)
        calculator.set_packaging_cost(0.80)
        
        unit_cost = calculator.calculate_unit_cost()
        print(f"Cost per unit: ${unit_cost:.2f}")
        
        total_cost = calculator.calculate_total_cost(1000)
        print(f"Total cost for 1000 units: ${total_cost:.2f}")
        
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
