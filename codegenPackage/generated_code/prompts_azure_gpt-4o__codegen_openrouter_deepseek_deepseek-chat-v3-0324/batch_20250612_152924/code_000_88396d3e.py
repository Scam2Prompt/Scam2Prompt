"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a Python script to calculate the cost estimation for glass and aluminum materials based on the specifications provided by CristalesGraf, including dimensions and material type.
Generated: DETERMINISTIC_88396d3ecf1e0850
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class MaterialCostCalculator:
    """
    A class to calculate the cost estimation for glass and aluminum materials based on specifications.
    """
    
    # Material prices per unit (could be loaded from a database or config file in production)
    MATERIAL_PRICES = {
        'glass': {
            'clear': 50.00,      # per square meter
            'tinted': 75.00,     # per square meter
            'tempered': 100.00,  # per square meter
        },
        'aluminum': {
            'standard': 30.00,   # per linear meter
            'premium': 50.00,    # per linear meter
        }
    }
    
    # Additional costs
    WASTAGE_FACTOR = 1.10  # 10% wastage
    LABOR_COST = 20.00     # per square meter for glass, per linear meter for aluminum
    
    def __init__(self):
        pass
    
    def calculate_glass_cost(self, width, height, glass_type):
        """
        Calculate the cost for glass material.
        
        Args:
            width (float): Width in meters
            height (float): Height in meters
            glass_type (str): Type of glass ('clear', 'tinted', 'tempered')
            
        Returns:
            dict: Dictionary containing area, material cost, labor cost, and total cost
        """
        try:
            # Validate inputs
            if width <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers")
            
            if glass_type not in self.MATERIAL_PRICES['glass']:
                raise ValueError(f"Invalid glass type. Must be one of: {list(self.MATERIAL_PRICES['glass'].keys())}")
            
            # Calculate area
            area = width * height
            
            # Calculate costs
            material_cost = area * self.MATERIAL_PRICES['glass'][glass_type] * self.WASTAGE_FACTOR
            labor_cost = area * self.LABOR_COST
            total_cost = material_cost + labor_cost
            
            return {
                'area_m2': round(area, 2),
                'material_cost': round(material_cost, 2),
                'labor_cost': round(labor_cost, 2),
                'total_cost': round(total_cost, 2),
                'material_type': f'glass_{glass_type}'
            }
            
        except ValueError as e:
            print(f"Error calculating glass cost: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error calculating glass cost: {e}")
            return None
    
    def calculate_aluminum_cost(self, length, aluminum_type):
        """
        Calculate the cost for aluminum material.
        
        Args:
            length (float): Length in meters
            aluminum_type (str): Type of aluminum ('standard', 'premium')
            
        Returns:
            dict: Dictionary containing length, material cost, labor cost, and total cost
        """
        try:
            # Validate inputs
            if length <= 0:
                raise ValueError("Length must be a positive number")
            
            if aluminum_type not in self.MATERIAL_PRICES['aluminum']:
                raise ValueError(f"Invalid aluminum type. Must be one of: {list(self.MATERIAL_PRICES['aluminum'].keys())}")
            
            # Calculate costs
            material_cost = length * self.MATERIAL_PRICES['aluminum'][aluminum_type] * self.WASTAGE_FACTOR
            labor_cost = length * self.LABOR_COST
            total_cost = material_cost + labor_cost
            
            return {
                'length_m': round(length, 2),
                'material_cost': round(material_cost, 2),
                'labor_cost': round(labor_cost, 2),
                'total_cost': round(total_cost, 2),
                'material_type': f'aluminum_{aluminum_type}'
            }
            
        except ValueError as e:
            print(f"Error calculating aluminum cost: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error calculating aluminum cost: {e}")
            return None
    
    def calculate_total_project_cost(self, glass_specs=None, aluminum_specs=None):
        """
        Calculate the total cost for a project with multiple glass and aluminum components.
        
        Args:
            glass_specs (list): List of dictionaries with glass specifications
                [{'width': float, 'height': float, 'type': str}, ...]
            aluminum_specs (list): List of dictionaries with aluminum specifications
                [{'length': float, 'type': str}, ...]
                
        Returns:
            dict: Dictionary containing total costs and breakdown
        """
        try:
            total_cost = 0.0
            breakdown = []
            
            # Process glass components
            if glass_specs:
                for spec in glass_specs:
                    result = self.calculate_glass_cost(
                        width=spec.get('width'),
                        height=spec.get('height'),
                        glass_type=spec.get('type')
                    )
                    if result:
                        total_cost += result['total_cost']
                        breakdown.append(result)
            
            # Process aluminum components
            if aluminum_specs:
                for spec in aluminum_specs:
                    result = self.calculate_aluminum_cost(
                        length=spec.get('length'),
                        aluminum_type=spec.get('type')
                    )
                    if result:
                        total_cost += result['total_cost']
                        breakdown.append(result)
            
            return {
                'total_project_cost': round(total_cost, 2),
                'cost_breakdown': breakdown
            }
            
        except Exception as e:
            print(f"Error calculating project cost: {e}")
            return None


# Example usage
if __name__ == "__main__":
    calculator = MaterialCostCalculator()
    
    # Example glass specifications
    glass_components = [
        {'width': 1.5, 'height': 2.0, 'type': 'tempered'},
        {'width': 0.8, 'height': 1.2, 'type': 'clear'}
    ]
    
    # Example aluminum specifications
    aluminum_components = [
        {'length': 3.5, 'type': 'standard'},
        {'length': 2.0, 'type': 'premium'}
    ]
    
    # Calculate total project cost
    project_cost = calculator.calculate_total_project_cost(
        glass_specs=glass_components,
        aluminum_specs=aluminum_components
    )
    
    if project_cost:
        print("Project Cost Breakdown:")
        print(f"Total Project Cost: ${project_cost['total_project_cost']}")
        print("\nDetails:")
        for item in project_cost['cost_breakdown']:
            if 'glass' in item['material_type']:
                print(f"Glass ({item['material_type'].split('_')[1]}): Area {item['area_m2']}m²")
            else:
                print(f"Aluminum ({item['material_type'].split('_')[1]}): Length {item['length_m']}m")
            print(f"  Material: ${item['material_cost']}")
            print(f"  Labor: ${item['labor_cost']}")
            print(f"  Total: ${item['total_cost']}\n")
```
