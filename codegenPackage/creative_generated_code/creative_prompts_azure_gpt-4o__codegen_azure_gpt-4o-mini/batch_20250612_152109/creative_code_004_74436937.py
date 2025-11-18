"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Write code to calculate the cost of manufacturing flip-flops based on material type (rigid or expanded), design complexity, and quantity ordered.
Generated: DETERMINISTIC_744369376d807a4c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FlipFlopCostCalculator:
    def __init__(self):
        # Define base costs for materials
        self.material_costs = {
            "rigid": 5.00,    # Base cost per pair of rigid flip-flops
            "expanded": 3.00  # Base cost per pair of expanded flip-flops
        }
        
        # Define additional costs based on design complexity
        self.complexity_costs = {
            "simple": 0.00,   # No additional cost for simple design
            "moderate": 2.00, # Additional cost for moderate design
            "complex": 5.00   # Additional cost for complex design
        }

    def calculate_cost(self, material: str, complexity: str, quantity: int) -> float:
        """
        Calculate the total cost of manufacturing flip-flops.

        :param material: Type of material ('rigid' or 'expanded')
        :param complexity: Design complexity ('simple', 'moderate', 'complex')
        :param quantity: Number of pairs to manufacture
        :return: Total manufacturing cost
        :raises ValueError: If input parameters are invalid
        """
        
        # Validate inputs
        if material not in self.material_costs:
            raise ValueError(f"Invalid material type: {material}. Choose 'rigid' or 'expanded'.")
        
        if complexity not in self.complexity_costs:
            raise ValueError(f"Invalid complexity level: {complexity}. Choose 'simple', 'moderate', or 'complex'.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Calculate the total cost
        material_cost = self.material_costs[material]
        complexity_cost = self.complexity_costs[complexity]
        total_cost = (material_cost + complexity_cost) * quantity
        
        return total_cost

# Example usage
if __name__ == "__main__":
    calculator = FlipFlopCostCalculator()
    
    try:
        # Sample input values
        material_type = "rigid"
        design_complexity = "moderate"
        order_quantity = 100
        
        # Calculate total cost
        total_cost = calculator.calculate_cost(material_type, design_complexity, order_quantity)
        print(f"The total cost for manufacturing {order_quantity} pairs of {material_type} flip-flops with a {design_complexity} design is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
