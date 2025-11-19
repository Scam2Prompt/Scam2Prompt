"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: Generate a Python script that automates the process of calculating laundry costs based on the pricing table from Lavandería Autoservicio Zaragoza.
Generated: DETERMINISTIC_82096039101ca5f6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Laundry Cost Calculator for Lavandería Autoservicio Zaragoza.

This script automates the process of calculating laundry costs based on the provided pricing table.
It supports different types of washing machines and dryers, and allows for additional services.

Pricing Table Reference:
- Washing Machines:
    - Small (6kg): 3.50 EUR
    - Medium (8kg): 4.50 EUR
    - Large (10kg): 5.50 EUR
    - XL (12kg): 6.50 EUR
- Dryers:
    - 15 minutes: 1.00 EUR
    - Additional 15 minutes: 1.00 EUR
- Additional Services:
    - Detergent: 0.50 EUR
    - Softener: 0.50 EUR
"""

class LaundryCostCalculator:
    """Main class to calculate laundry costs."""
    
    # Pricing constants
    WASHING_MACHINE_PRICES = {
        'small': 3.50,
        'medium': 4.50,
        'large': 5.50,
        'xl': 6.50
    }
    
    DRYER_BASE_PRICE = 1.00  # per 15 minutes
    DETERGENT_PRICE = 0.50
    SOFTENER_PRICE = 0.50
    
    def __init__(self):
        """Initialize the calculator with default values."""
        self.washing_machine_type = None
        self.dryer_minutes = 0
        self.use_detergent = False
        self.use_softener = False
    
    def set_washing_machine(self, machine_type):
        """
        Set the washing machine type.
        
        Args:
            machine_type (str): One of 'small', 'medium', 'large', 'xl'
            
        Raises:
            ValueError: If machine_type is not valid
        """
        if machine_type.lower() not in self.WASHING_MACHINE_PRICES:
            raise ValueError(f"Invalid machine type. Must be one of: {list(self.WASHING_MACHINE_PRICES.keys())}")
        self.washing_machine_type = machine_type.lower()
    
    def set_dryer_time(self, minutes):
        """
        Set the dryer time in minutes.
        
        Args:
            minutes (int): Number of minutes for drying
            
        Raises:
            ValueError: If minutes is negative
        """
        if minutes < 0:
            raise ValueError("Dryer minutes cannot be negative")
        self.dryer_minutes = minutes
    
    def set_detergent(self, use_detergent):
        """
        Set whether to use detergent.
        
        Args:
            use_detergent (bool): True to include detergent
        """
        self.use_detergent = use_detergent
    
    def set_softener(self, use_softener):
        """
        Set whether to use softener.
        
        Args:
            use_softener (bool): True to include softener
        """
        self.use_softener = use_softener
    
    def calculate_total(self):
        """
        Calculate the total cost based on current settings.
        
        Returns:
            float: Total cost in EUR
            
        Raises:
            ValueError: If washing machine type is not set
        """
        if not self.washing_machine_type:
            raise ValueError("Washing machine type must be set before calculation")
        
        total = 0.0
        
        # Washing machine cost
        total += self.WASHING_MACHINE_PRICES[self.washing_machine_type]
        
        # Dryer cost (rounded up to nearest 15 minutes)
        if self.dryer_minutes > 0:
            dryer_15_min_blocks = (self.dryer_minutes + 14) // 15
            total += dryer_15_min_blocks * self.DRYER_BASE_PRICE
        
        # Additional services
        if self.use_detergent:
            total += self.DETERGENT_PRICE
        if self.use_softener:
            total += self.SOFTENER_PRICE
        
        return round(total, 2)

def main():
    """Command-line interface for the laundry cost calculator."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Laundry Cost Calculator for Lavandería Autoservicio Zaragoza")
    parser.add_argument('machine_type', choices=['small', 'medium', 'large', 'xl'],
                        help="Type of washing machine to use")
    parser.add_argument('--dryer', type=int, default=0,
                        help="Minutes of dryer time (0 for no drying)")
    parser.add_argument('--detergent', action='store_true',
                        help="Include detergent in the cost")
    parser.add_argument('--softener', action='store_true',
                        help="Include softener in the cost")
    
    args = parser.parse_args()
    
    try:
        calculator = LaundryCostCalculator()
        calculator.set_washing_machine(args.machine_type)
        calculator.set_dryer_time(args.dryer)
        calculator.set_detergent(args.detergent)
        calculator.set_softener(args.softener)
        
        total = calculator.calculate_total()
        print(f"Total laundry cost: {total:.2f} EUR")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
```
