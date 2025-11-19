"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "Develop a simple calculator to determine the cost of pigments and additives required for a specific project."
Generated: DETERMINISTIC_d270cf93df6a4cc0
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class PigmentCalculator:
    """
    A simple calculator to determine the cost of pigments and additives for a project.
    """
    
    def __init__(self):
        self.pigments = {}  # Stores pigment names and their costs per unit
        self.additives = {}  # Stores additive names and their costs per unit
        
    def add_pigment(self, name: str, cost_per_unit: float):
        """
        Add a pigment to the calculator.
        
        Args:
            name: Name of the pigment.
            cost_per_unit: Cost per unit of the pigment.
        """
        if cost_per_unit <= 0:
            raise ValueError("Cost per unit must be positive.")
        self.pigments[name] = cost_per_unit
        
    def add_additive(self, name: str, cost_per_unit: float):
        """
        Add an additive to the calculator.
        
        Args:
            name: Name of the additive.
            cost_per_unit: Cost per unit of the additive.
        """
        if cost_per_unit <= 0:
            raise ValueError("Cost per unit must be positive.")
        self.additives[name] = cost_per_unit
        
    def calculate_cost(self, pigment_quantities: dict, additive_quantities: dict) -> float:
        """
        Calculate the total cost based on quantities of pigments and additives.
        
        Args:
            pigment_quantities: Dictionary mapping pigment names to quantities.
            additive_quantities: Dictionary mapping additive names to quantities.
            
        Returns:
            Total cost of the project.
            
        Raises:
            ValueError: If any quantity is negative or if an unknown pigment/additive is provided.
        """
        total_cost = 0.0
        
        # Validate and calculate pigment costs
        for name, quantity in pigment_quantities.items():
            if name not in self.pigments:
                raise ValueError(f"Unknown pigment: {name}")
            if quantity < 0:
                raise ValueError(f"Negative quantity not allowed for pigment: {name}")
            total_cost += self.pigments[name] * quantity
        
        # Validate and calculate additive costs
        for name, quantity in additive_quantities.items():
            if name not in self.additives:
                raise ValueError(f"Unknown additive: {name}")
            if quantity < 0:
                raise ValueError(f"Negative quantity not allowed for additive: {name}")
            total_cost += self.additives[name] * quantity
            
        return total_cost

def main():
    calculator = PigmentCalculator()
    
    # Sample data - in a real application, this would come from user input or a database
    calculator.add_pigment("Titanium White", 5.50)
    calculator.add_pigment("Cadmium Yellow", 7.25)
    calculator.add_additive("Drying Agent", 2.30)
    calculator.add_additive("Texture Gel", 3.75)
    
    try:
        # Example usage
        pigment_quantities = {
            "Titanium White": 2,
            "Cadmium Yellow": 1.5
        }
        additive_quantities = {
            "Drying Agent": 0.5,
            "Texture Gel": 1
        }
        
        total_cost = calculator.calculate_cost(pigment_quantities, additive_quantities)
        print(f"Total project cost: ${total_cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
