"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: "Write a code snippet for a simple calculator to estimate the cost of a cabinetry project, including materials and labor costs."
Generated: DETERMINISTIC_214c86d6411d060d
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CabinetryCalculator:
    """
    A simple calculator to estimate the cost of a cabinetry project.
    Includes material costs (wood, hardware, finishes) and labor costs.
    """
    
    def __init__(self):
        # Default cost rates (per unit)
        self.material_rates = {
            'wood': 5.00,        # per square foot
            'hardware': 2.50,    # per piece
            'finish': 1.75       # per square foot
        }
        self.labor_rate = 45.00  # per hour
        self.tax_rate = 0.08     # 8%
    
    def calculate_material_cost(self, wood_area, hardware_count, finish_area):
        """
        Calculate total material cost based on quantities and rates.
        
        Args:
            wood_area (float): Area of wood needed in sq ft
            hardware_count (int): Number of hardware pieces needed
            finish_area (float): Area to be finished in sq ft
            
        Returns:
            float: Total material cost
        """
        try:
            wood_cost = wood_area * self.material_rates['wood']
            hardware_cost = hardware_count * self.material_rates['hardware']
            finish_cost = finish_area * self.material_rates['finish']
            return wood_cost + hardware_cost + finish_cost
        except (TypeError, KeyError) as e:
            raise ValueError(f"Invalid input for material calculation: {e}")
    
    def calculate_labor_cost(self, hours):
        """
        Calculate total labor cost based on hours worked.
        
        Args:
            hours (float): Hours of labor needed
            
        Returns:
            float: Total labor cost
        """
        try:
            return hours * self.labor_rate
        except TypeError as e:
            raise ValueError(f"Invalid input for labor calculation: {e}")
    
    def calculate_total_cost(self, wood_area, hardware_count, finish_area, labor_hours):
        """
        Calculate total project cost including materials, labor, and tax.
        
        Args:
            wood_area (float): Area of wood needed in sq ft
            hardware_count (int): Number of hardware pieces needed
            finish_area (float): Area to be finished in sq ft
            labor_hours (float): Hours of labor needed
            
        Returns:
            dict: Dictionary containing cost breakdown
        """
        try:
            material_cost = self.calculate_material_cost(wood_area, hardware_count, finish_area)
            labor_cost = self.calculate_labor_cost(labor_hours)
            subtotal = material_cost + labor_cost
            tax = subtotal * self.tax_rate
            total = subtotal + tax
            
            return {
                'material_cost': round(material_cost, 2),
                'labor_cost': round(labor_cost, 2),
                'subtotal': round(subtotal, 2),
                'tax': round(tax, 2),
                'total': round(total, 2)
            }
        except ValueError as e:
            raise ValueError(f"Error in total cost calculation: {e}")
    
    def update_rates(self, wood_rate=None, hardware_rate=None, finish_rate=None, labor_rate=None, tax_rate=None):
        """
        Update any of the cost rates.
        
        Args:
            wood_rate (float): New wood rate per sq ft
            hardware_rate (float): New hardware rate per piece
            finish_rate (float): New finish rate per sq ft
            labor_rate (float): New labor rate per hour
            tax_rate (float): New tax rate (decimal)
        """
        if wood_rate is not None:
            self.material_rates['wood'] = wood_rate
        if hardware_rate is not None:
            self.material_rates['hardware'] = hardware_rate
        if finish_rate is not None:
            self.material_rates['finish'] = finish_rate
        if labor_rate is not None:
            self.labor_rate = labor_rate
        if tax_rate is not None:
            self.tax_rate = tax_rate


# Example usage
if __name__ == "__main__":
    calculator = CabinetryCalculator()
    
    try:
        # Sample project: 50 sq ft wood, 20 hardware pieces, 50 sq ft finish, 10 labor hours
        cost_breakdown = calculator.calculate_total_cost(
            wood_area=50,
            hardware_count=20,
            finish_area=50,
            labor_hours=10
        )
        
        print("Cost Breakdown:")
        for key, value in cost_breakdown.items():
            print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
            
    except ValueError as e:
        print(f"Error calculating costs: {e}")
```
