"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Create a Python program that estimates the cost of insulating a furnace using Aprisacv's refractory products (e.g., Aprifiber, ApriPaper, Aprick bricks), factoring in product dimensions and required quantities.
Generated: DETERMINISTIC_63e961025282fef4
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class RefractoryProduct:
    """
    Represents a refractory product with its dimensions and cost per unit.
    """
    def __init__(self, name, length, width, thickness, cost_per_unit):
        """
        Initialize a refractory product.
        
        Args:
            name (str): Product name (e.g., Aprifiber, ApriPaper, Aprick bricks)
            length (float): Length in meters
            width (float): Width in meters
            thickness (float): Thickness in meters
            cost_per_unit (float): Cost per unit in currency
        """
        self.name = name
        self.length = length
        self.width = width
        self.thickness = thickness
        self.cost_per_unit = cost_per_unit
    
    def calculate_area(self):
        """Calculate the area of one unit of the product."""
        return self.length * self.width
    
    def calculate_volume(self):
        """Calculate the volume of one unit of the product."""
        return self.length * self.width * self.thickness

class FurnaceInsulationEstimator:
    """
    Estimates the cost of insulating a furnace using refractory products.
    """
    def __init__(self):
        """Initialize the estimator with default products."""
        self.products = {
            'Aprifiber': RefractoryProduct('Aprifiber', 1.0, 0.5, 0.025, 15.0),
            'ApriPaper': RefractoryProduct('ApriPaper', 0.5, 0.5, 0.01, 8.0),
            'AprickBricks': RefractoryProduct('AprickBricks', 0.2, 0.1, 0.05, 5.0)
        }
    
    def add_product(self, name, length, width, thickness, cost_per_unit):
        """
        Add a custom refractory product to the estimator.
        
        Args:
            name (str): Product name
            length (float): Length in meters
            width (float): Width in meters
            thickness (float): Thickness in meters
            cost_per_unit (float): Cost per unit in currency
        """
        self.products[name] = RefractoryProduct(name, length, width, thickness, cost_per_unit)
    
    def estimate_cost(self, product_name, surface_area, required_thickness):
        """
        Estimate the cost of insulating a given surface area with a specified thickness.
        
        Args:
            product_name (str): Name of the refractory product to use
            surface_area (float): Total surface area to cover in square meters
            required_thickness (float): Required insulation thickness in meters
            
        Returns:
            dict: Dictionary containing estimated cost and quantity needed
        """
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' not available.")
        
        product = self.products[product_name]
        
        if required_thickness <= 0 or surface_area <= 0:
            raise ValueError("Surface area and thickness must be positive values.")
        
        # Calculate number of layers needed to achieve required thickness
        layers_needed = math.ceil(required_thickness / product.thickness)
        
        # Calculate total area to cover (accounting for multiple layers)
        total_area = surface_area * layers_needed
        
        # Calculate number of product units needed
        units_needed = math.ceil(total_area / product.calculate_area())
        
        # Calculate total cost
        total_cost = units_needed * product.cost_per_unit
        
        return {
            'product': product_name,
            'units_needed': units_needed,
            'total_cost': round(total_cost, 2),
            'layers_needed': layers_needed,
            'total_area_covered': round(total_area, 2)
        }
    
    def get_available_products(self):
        """Return a list of available product names."""
        return list(self.products.keys())

def main():
    """Main function to demonstrate the estimator."""
    estimator = FurnaceInsulationEstimator()
    
    print("Available products:", estimator.get_available_products())
    
    try:
        # Example estimation
        result = estimator.estimate_cost(
            product_name='Aprifiber',
            surface_area=10.0,  # 10 square meters
            required_thickness=0.05  # 5 cm thickness
        )
        
        print("\nEstimation Results:")
        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
