"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Write a program to calculate storage costs for outsourced warehousing, referencing Uniair Cargo's tips on warehouse outsourcing.
Generated: DETERMINISTIC_f6ba040f60da94c8
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Warehouse Storage Cost Calculator

This program calculates the storage costs for outsourced warehousing based on:
- Storage duration (in months)
- Volume of goods (in cubic meters)
- Special handling requirements (e.g., refrigeration, hazardous materials)

References:
- Uniair Cargo's warehouse outsourcing tips
- Industry standard storage pricing models
"""

class WarehouseCostCalculator:
    """
    A class to calculate warehouse storage costs based on various parameters.
    """
    
    def __init__(self):
        """
        Initialize the calculator with base rates and factors.
        """
        # Base storage rate per cubic meter per month (USD)
        self.base_rate = 5.00  
        
        # Special handling surcharges (percentage of base rate)
        self.special_handling_rates = {
            'refrigeration': 0.5,    # 50% surcharge
            'hazardous': 0.75,       # 75% surcharge
            'fragile': 0.3,          # 30% surcharge
            'standard': 0.0          # No surcharge
        }
        
        # Volume discount thresholds and rates
        self.volume_discounts = [
            {'threshold': 100, 'discount': 0.05},   # 5% discount for 100+ m³
            {'threshold': 500, 'discount': 0.1},    # 10% discount for 500+ m³
            {'threshold': 1000, 'discount': 0.15}   # 15% discount for 1000+ m³
        ]
        
        # Long-term storage discounts
        self.duration_discounts = [
            {'threshold': 6, 'discount': 0.0},      # No discount for <6 months
            {'threshold': 12, 'discount': 0.1},     # 10% discount for 6-12 months
            {'threshold': 24, 'discount': 0.15},    # 15% discount for 12-24 months
            {'threshold': float('inf'), 'discount': 0.2}  # 20% discount for 24+ months
        ]
    
    def calculate_cost(self, duration_months, volume_m3, handling_type='standard'):
        """
        Calculate the total storage cost.
        
        Args:
            duration_months (int/float): Storage duration in months
            volume_m3 (int/float): Volume of goods in cubic meters
            handling_type (str): Type of special handling required
            
        Returns:
            float: Total storage cost in USD
            
        Raises:
            ValueError: If invalid inputs are provided
        """
        # Input validation
        if not isinstance(duration_months, (int, float)) or duration_months <= 0:
            raise ValueError("Duration must be a positive number")
        if not isinstance(volume_m3, (int, float)) or volume_m3 <= 0:
            raise ValueError("Volume must be a positive number")
        if handling_type not in self.special_handling_rates:
            raise ValueError(f"Invalid handling type. Must be one of: {list(self.special_handling_rates.keys())}")
        
        # Calculate base cost
        base_cost = self.base_rate * volume_m3 * duration_months
        
        # Apply special handling surcharge
        handling_surcharge = self.special_handling_rates[handling_type]
        cost_with_handling = base_cost * (1 + handling_surcharge)
        
        # Apply volume discount
        volume_discount = 0.0
        for discount in sorted(self.volume_discounts, key=lambda x: x['threshold']):
            if volume_m3 >= discount['threshold']:
                volume_discount = discount['discount']
        cost_with_volume_discount = cost_with_handling * (1 - volume_discount)
        
        # Apply duration discount
        duration_discount = 0.0
        for discount in sorted(self.duration_discounts, key=lambda x: x['threshold']):
            if duration_months <= discount['threshold']:
                duration_discount = discount['discount']
                break
        total_cost = cost_with_volume_discount * (1 - duration_discount)
        
        return round(total_cost, 2)

# Example usage
if __name__ == "__main__":
    calculator = WarehouseCostCalculator()
    
    try:
        # Get user input
        duration = float(input("Enter storage duration (months): "))
        volume = float(input("Enter volume (cubic meters): "))
        print("Available handling types:")
        for i, handling_type in enumerate(calculator.special_handling_rates.keys(), 1):
            print(f"{i}. {handling_type}")
        handling = input("Select handling type: ")
        
        # Calculate and display cost
        cost = calculator.calculate_cost(duration, volume, handling)
        print(f"\nTotal storage cost: ${cost:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
