"""
Generated Code Metadata:
========================
Original URL: https://burtonwright.net
Prompt: Create a program that calculates the cost of HVAC repairs, replacements, and tune-ups based on RJW Mechanical's pricing model. Include features for applying discounts like the 15% Comfort Club membership benefit.
Generated: DETERMINISTIC_c941965dd57e0aa3
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HVACServiceCalculator:
    """
    A class to calculate HVAC service costs based on RJW Mechanical's pricing model.
    Supports calculating repair, replacement, and tune-up costs with optional discounts.
    """

    # Base prices for services (in USD)
    BASE_PRICES = {
        'repair': 150,          # Base diagnostic/repair fee
        'replacement': 5000,    # Base replacement cost (varies by unit)
        'tune_up': 100          # Base tune-up cost
    }

    # Additional cost factors
    REPLACEMENT_FACTORS = {
        'unit_type': {
            'furnace': 1.0,
            'air_conditioner': 1.2,
            'heat_pump': 1.5,
            'boiler': 1.3
        },
        'size': {
            'small': 0.8,
            'medium': 1.0,
            'large': 1.5
        }
    }

    def __init__(self):
        """Initialize the calculator with default values."""
        self.discounts = {
            'comfort_club': 0.15  # 15% discount for Comfort Club members
        }

    def calculate_repair_cost(self, hours: float, parts_cost: float = 0, is_comfort_club_member: bool = False) -> float:
        """
        Calculate repair cost including labor and parts.
        
        Args:
            hours: Hours of labor required
            parts_cost: Cost of parts (default 0)
            is_comfort_club_member: Whether to apply Comfort Club discount
            
        Returns:
            Total repair cost after discounts
        """
        if hours < 0 or parts_cost < 0:
            raise ValueError("Hours and parts cost must be non-negative")
            
        labor_cost = self.BASE_PRICES['repair'] + (hours * 85)  # $85/hour labor rate
        subtotal = labor_cost + parts_cost
        
        return self._apply_discount(subtotal, is_comfort_club_member)

    def calculate_replacement_cost(self, unit_type: str, size: str, is_comfort_club_member: bool = False) -> float:
        """
        Calculate replacement cost based on unit type and size.
        
        Args:
            unit_type: Type of HVAC unit (furnace, air_conditioner, heat_pump, boiler)
            size: Size of unit (small, medium, large)
            is_comfort_club_member: Whether to apply Comfort Club discount
            
        Returns:
            Total replacement cost after discounts
            
        Raises:
            ValueError: If invalid unit_type or size is provided
        """
        if unit_type not in self.REPLACEMENT_FACTORS['unit_type']:
            raise ValueError(f"Invalid unit type. Must be one of: {list(self.REPLACEMENT_FACTORS['unit_type'].keys())}")
            
        if size not in self.REPLACEMENT_FACTORS['size']:
            raise ValueError(f"Invalid size. Must be one of: {list(self.REPLACEMENT_FACTORS['size'].keys())}")
            
        unit_factor = self.REPLACEMENT_FACTORS['unit_type'][unit_type]
        size_factor = self.REPLACEMENT_FACTORS['size'][size]
        subtotal = self.BASE_PRICES['replacement'] * unit_factor * size_factor
        
        return self._apply_discount(subtotal, is_comfort_club_member)

    def calculate_tune_up_cost(self, is_comfort_club_member: bool = False) -> float:
        """
        Calculate tune-up cost.
        
        Args:
            is_comfort_club_member: Whether to apply Comfort Club discount
            
        Returns:
            Total tune-up cost after discounts
        """
        return self._apply_discount(self.BASE_PRICES['tune_up'], is_comfort_club_member)

    def _apply_discount(self, amount: float, is_comfort_club_member: bool) -> float:
        """
        Apply discount to a service amount if applicable.
        
        Args:
            amount: Original service amount
            is_comfort_club_member: Whether to apply Comfort Club discount
            
        Returns:
            Amount after discount applied
        """
        if is_comfort_club_member:
            return amount * (1 - self.discounts['comfort_club'])
        return amount


# Example usage
if __name__ == "__main__":
    calculator = HVACServiceCalculator()
    
    try:
        # Calculate repair cost
        repair_cost = calculator.calculate_repair_cost(hours=2.5, parts_cost=200, is_comfort_club_member=True)
        print(f"Repair Cost: ${repair_cost:.2f}")
        
        # Calculate replacement cost
        replacement_cost = calculator.calculate_replacement_cost(
            unit_type='heat_pump', 
            size='large', 
            is_comfort_club_member=False
        )
        print(f"Replacement Cost: ${replacement_cost:.2f}")
        
        # Calculate tune-up cost
        tune_up_cost = calculator.calculate_tune_up_cost(is_comfort_club_member=True)
        print(f"Tune-Up Cost: ${tune_up_cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
