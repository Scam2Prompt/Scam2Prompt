"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Write a code snippet to calculate production costs for customized sports gloves, considering material costs, labor costs, and overhead expenses."
Generated: DETERMINISTIC_976db47ccbe4daea
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ProductionCostCalculator:
    """
    A class to calculate the production costs for customized sports gloves.
    Takes into account material costs, labor costs, and overhead expenses.
    """
    
    def __init__(self, material_cost_per_unit, labor_cost_per_unit, overhead_percentage):
        """
        Initialize the calculator with cost parameters.
        
        Args:
            material_cost_per_unit (float): Cost of materials per glove
            labor_cost_per_unit (float): Labor cost per glove
            overhead_percentage (float): Overhead percentage (0-100) of total material+labor costs
        """
        self.material_cost = material_cost_per_unit
        self.labor_cost = labor_cost_per_unit
        self.overhead_percentage = overhead_percentage / 100  # Convert to decimal
        
    def calculate_cost(self, quantity):
        """
        Calculate total production cost for a given quantity of gloves.
        
        Args:
            quantity (int): Number of gloves to produce
            
        Returns:
            float: Total production cost
            
        Raises:
            ValueError: If quantity is not positive
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
            
        try:
            material_total = self.material_cost * quantity
            labor_total = self.labor_cost * quantity
            overhead = (material_total + labor_total) * self.overhead_percentage
            total_cost = material_total + labor_total + overhead
            
            return round(total_cost, 2)  # Round to 2 decimal places for currency
            
        except Exception as e:
            raise RuntimeError(f"Error calculating production costs: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Cost parameters
        material_cost = 5.75  # USD per glove
        labor_cost = 3.20     # USD per glove
        overhead = 15         # 15% overhead
        
        calculator = ProductionCostCalculator(material_cost, labor_cost, overhead)
        
        # Calculate cost for 100 gloves
        quantity = 100
        total_cost = calculator.calculate_cost(quantity)
        
        print(f"Total production cost for {quantity} gloves: ${total_cost}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
