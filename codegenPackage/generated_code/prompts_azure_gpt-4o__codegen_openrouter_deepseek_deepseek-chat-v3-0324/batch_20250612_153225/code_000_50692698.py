"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Write Python code to calculate the price of custom printing services using AI, incorporating variables like material type (e.g., acrylic, plaswood, composite), dimensions, and quantity, as described on ThePrintNan website.
Generated: DETERMINISTIC_50692698f85a22e5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PrintingServiceCalculator:
    """
    A class to calculate the price of custom printing services based on various parameters.
    """
    
    # Material costs per square inch (base prices)
    MATERIAL_COSTS = {
        'acrylic': 0.15,
        'plaswood': 0.10,
        'composite': 0.12
    }
    
    # Quantity discount thresholds and percentages
    QUANTITY_DISCOUNTS = {
        10: 0.05,    # 5% discount for 10+ items
        50: 0.10,    # 10% discount for 50+ items
        100: 0.15    # 15% discount for 100+ items
    }
    
    # Minimum order cost
    MIN_ORDER_COST = 5.00
    
    # Setup fee (applied once per order)
    SETUP_FEE = 3.50
    
    def __init__(self):
        """Initialize the calculator with default values."""
        pass
    
    def calculate_area(self, length, width, unit='inches'):
        """
        Calculate the area in square inches.
        
        Args:
            length (float): Length of the item
            width (float): Width of the item
            unit (str): Unit of measurement ('inches' or 'cm')
            
        Returns:
            float: Area in square inches
        """
        if unit.lower() == 'cm':
            # Convert cm to inches (1 inch = 2.54 cm)
            length = length / 2.54
            width = width / 2.54
        
        return length * width
    
    def get_quantity_discount(self, quantity):
        """
        Determine the applicable quantity discount.
        
        Args:
            quantity (int): Number of items ordered
            
        Returns:
            float: Discount percentage (0.0 to 1.0)
        """
        discount = 0.0
        for threshold, disc in sorted(self.QUANTITY_DISCOUNTS.items(), reverse=True):
            if quantity >= threshold:
                discount = disc
                break
        return discount
    
    def calculate_price(self, material, length, width, quantity, unit='inches'):
        """
        Calculate the total price for the printing service order.
        
        Args:
            material (str): Type of material ('acrylic', 'plaswood', 'composite')
            length (float): Length of the item
            width (float): Width of the item
            quantity (int): Number of items ordered
            unit (str): Unit of measurement ('inches' or 'cm')
            
        Returns:
            dict: Dictionary containing price breakdown and total
        """
        try:
            # Validate inputs
            if material.lower() not in self.MATERIAL_COSTS:
                raise ValueError(f"Invalid material type. Must be one of: {list(self.MATERIAL_COSTS.keys())}")
            
            if length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive numbers")
            
            if quantity <= 0:
                raise ValueError("Quantity must be a positive integer")
            
            # Calculate area
            area = self.calculate_area(length, width, unit)
            
            # Get base material cost
            material_cost_per_unit = self.MATERIAL_COSTS[material.lower()] * area
            
            # Calculate quantity discount
            discount = self.get_quantity_discount(quantity)
            
            # Calculate subtotal before discount
            subtotal = material_cost_per_unit * quantity
            
            # Apply discount
            discount_amount = subtotal * discount
            discounted_subtotal = subtotal - discount_amount
            
            # Add setup fee
            total = discounted_subtotal + self.SETUP_FEE
            
            # Ensure minimum order cost
            total = max(total, self.MIN_ORDER_COST)
            
            # Round to 2 decimal places for currency
            total = round(total, 2)
            subtotal = round(subtotal, 2)
            discount_amount = round(discount_amount, 2)
            
            return {
                'material_cost_per_unit': round(material_cost_per_unit, 2),
                'subtotal': subtotal,
                'quantity_discount_percentage': discount * 100,
                'quantity_discount_amount': discount_amount,
                'setup_fee': self.SETUP_FEE,
                'total': total,
                'area_sq_in': round(area, 2),
                'unit_price': round(material_cost_per_unit, 2)
            }
            
        except ValueError as e:
            return {'error': str(e)}
        except Exception as e:
            return {'error': f"An unexpected error occurred: {str(e)}"}

# Example usage
if __name__ == "__main__":
    calculator = PrintingServiceCalculator()
    
    # Calculate price for 5 acrylic items (8x10 inches)
    result = calculator.calculate_price('acrylic', 8, 10, 5)
    print("Price for 5 acrylic items (8x10 inches):")
    print(result)
    
    # Calculate price for 15 plaswood items (20x30 cm)
    result = calculator.calculate_price('plaswood', 20, 30, 15, 'cm')
    print("\nPrice for 15 plaswood items (20x30 cm):")
    print(result)
```
