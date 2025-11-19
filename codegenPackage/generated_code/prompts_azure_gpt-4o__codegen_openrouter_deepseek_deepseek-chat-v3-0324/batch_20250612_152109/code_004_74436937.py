"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write code to calculate the cost of manufacturing flip-flops based on material type (rigid or expanded), design complexity, and quantity ordered.
Generated: DETERMINISTIC_744369376d807a4c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FlipFlopManufacturingCostCalculator:
    """
    A class to calculate the manufacturing cost of flip-flops based on material type,
    design complexity, and quantity ordered.
    """
    
    # Material costs per unit (in USD)
    MATERIAL_COSTS = {
        'rigid': 2.50,
        'expanded': 1.75
    }
    
    # Design complexity multipliers
    COMPLEXITY_MULTIPLIERS = {
        'simple': 1.0,
        'medium': 1.3,
        'complex': 1.7
    }
    
    # Bulk discount thresholds and rates
    BULK_DISCOUNTS = [
        {'threshold': 1000, 'discount': 0.05},
        {'threshold': 5000, 'discount': 0.10},
        {'threshold': 10000, 'discount': 0.15}
    ]
    
    def __init__(self):
        """Initialize the calculator with default values."""
        pass
    
    def calculate_cost(self, material_type: str, design_complexity: str, quantity: int) -> float:
        """
        Calculate the total manufacturing cost for flip-flops.
        
        Args:
            material_type: Type of material ('rigid' or 'expanded')
            design_complexity: Complexity level ('simple', 'medium', or 'complex')
            quantity: Number of flip-flops ordered
            
        Returns:
            float: Total manufacturing cost
            
        Raises:
            ValueError: If invalid input parameters are provided
        """
        # Validate input parameters
        if material_type.lower() not in self.MATERIAL_COSTS:
            raise ValueError(f"Invalid material type. Must be one of: {list(self.MATERIAL_COSTS.keys())}")
        
        if design_complexity.lower() not in self.COMPLEXITY_MULTIPLIERS:
            raise ValueError(f"Invalid design complexity. Must be one of: {list(self.COMPLEXITY_MULTIPLIERS.keys())}")
        
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        # Calculate base cost
        base_cost = self.MATERIAL_COSTS[material_type.lower()]
        
        # Apply design complexity multiplier
        complexity_multiplier = self.COMPLEXITY_MULTIPLIERS[design_complexity.lower()]
        unit_cost = base_cost * complexity_multiplier
        
        # Calculate total before discounts
        total_cost = unit_cost * quantity
        
        # Apply bulk discounts if applicable
        discount_rate = self._get_discount_rate(quantity)
        if discount_rate > 0:
            total_cost *= (1 - discount_rate)
        
        return round(total_cost, 2)
    
    def _get_discount_rate(self, quantity: int) -> float:
        """
        Determine the applicable bulk discount rate based on quantity.
        
        Args:
            quantity: Number of flip-flops ordered
            
        Returns:
            float: Discount rate (0 if no discount applies)
        """
        discount_rate = 0.0
        for discount_tier in sorted(self.BULK_DISCOUNTS, key=lambda x: x['threshold'], reverse=True):
            if quantity >= discount_tier['threshold']:
                discount_rate = discount_tier['discount']
                break
        return discount_rate


# Example usage
if __name__ == "__main__":
    calculator = FlipFlopManufacturingCostCalculator()
    
    try:
        # Test case 1
        cost1 = calculator.calculate_cost('rigid', 'medium', 500)
        print(f"Cost for 500 medium complexity rigid flip-flops: ${cost1:.2f}")
        
        # Test case 2
        cost2 = calculator.calculate_cost('expanded', 'complex', 1500)
        print(f"Cost for 1500 complex complexity expanded flip-flops: ${cost2:.2f}")
        
        # Test case 3 (should raise error)
        cost3 = calculator.calculate_cost('invalid', 'simple', 100)
        print(f"Cost: ${cost3:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
