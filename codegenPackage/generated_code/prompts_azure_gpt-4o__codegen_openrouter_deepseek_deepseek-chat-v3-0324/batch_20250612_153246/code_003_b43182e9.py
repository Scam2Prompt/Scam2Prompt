"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: Create a script that calculates the cost of designing a green wall for a commercial space, using parameters like wall size and plant density, inspired by City Garden México's green wall projects.
Generated: DETERMINISTIC_b43182e997e321e2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Green Wall Cost Calculator for Commercial Spaces
Inspired by City Garden México's green wall projects

This script calculates the cost of designing a green wall based on:
- Wall dimensions (width and height)
- Plant density (low, medium, high)
- Additional features (irrigation system, lighting, maintenance plan)
"""

class GreenWallCalculator:
    # Base costs (in USD)
    BASE_COST_PER_SQFT = 35.00
    PLANT_DENSITY_FACTORS = {
        'low': 1.0,
        'medium': 1.5,
        'high': 2.0
    }
    ADDITIONAL_FEATURES = {
        'irrigation': 2.50,  # per sqft
        'lighting': 1.75,    # per sqft
        'maintenance': 0.80  # per sqft per month
    }
    
    def __init__(self, width, height, plant_density='medium'):
        """
        Initialize calculator with wall dimensions and plant density.
        
        Args:
            width (float): Wall width in feet
            height (float): Wall height in feet
            plant_density (str): 'low', 'medium', or 'high'
        """
        self.width = width
        self.height = height
        self.plant_density = plant_density.lower()
        self.features = {
            'irrigation': False,
            'lighting': False,
            'maintenance': False
        }
        self.maintenance_months = 0
        
    def validate_inputs(self):
        """Validate input parameters."""
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Wall dimensions must be positive numbers")
        if self.plant_density not in self.PLANT_DENSITY_FACTORS:
            raise ValueError(f"Plant density must be one of: {list(self.PLANT_DENSITY_FACTORS.keys())}")
        
    def add_feature(self, feature, months=0):
        """
        Add additional features to the calculation.
        
        Args:
            feature (str): 'irrigation', 'lighting', or 'maintenance'
            months (int): Number of months for maintenance plan (if applicable)
        """
        feature = feature.lower()
        if feature not in self.ADDITIONAL_FEATURES:
            raise ValueError(f"Invalid feature. Must be one of: {list(self.ADDITIONAL_FEATURES.keys())}")
        
        self.features[feature] = True
        if feature == 'maintenance':
            if months <= 0:
                raise ValueError("Maintenance months must be a positive integer")
            self.maintenance_months = months
    
    def calculate_area(self):
        """Calculate wall area in square feet."""
        return self.width * self.height
    
    def calculate_cost(self):
        """
        Calculate total cost of the green wall project.
        
        Returns:
            dict: Breakdown of costs and total
        """
        self.validate_inputs()
        area = self.calculate_area()
        
        # Base cost
        base_cost = area * self.BASE_COST_PER_SQFT * self.PLANT_DENSITY_FACTORS[self.plant_density]
        
        # Additional features
        additional_costs = {}
        total_additional = 0
        
        for feature, enabled in self.features.items():
            if enabled:
                if feature == 'maintenance':
                    cost = area * self.ADDITIONAL_FEATURES[feature] * self.maintenance_months
                else:
                    cost = area * self.ADDITIONAL_FEATURES[feature]
                
                additional_costs[feature] = cost
                total_additional += cost
        
        total_cost = base_cost + total_additional
        
        return {
            'area_sqft': area,
            'base_cost': round(base_cost, 2),
            'additional_costs': {k: round(v, 2) for k, v in additional_costs.items()},
            'total_cost': round(total_cost, 2)
        }

def main():
    """Example usage of the GreenWallCalculator."""
    try:
        # Get user input
        width = float(input("Enter wall width (feet): "))
        height = float(input("Enter wall height (feet): "))
        density = input("Enter plant density (low/medium/high): ").lower()
        
        # Create calculator
        calculator = GreenWallCalculator(width, height, density)
        
        # Ask about additional features
        features = ['irrigation', 'lighting', 'maintenance']
        for feature in features:
            answer = input(f"Include {feature}? (y/n): ").lower()
            if answer == 'y':
                if feature == 'maintenance':
                    months = int(input("How many months of maintenance? "))
                    calculator.add_feature(feature, months)
                else:
                    calculator.add_feature(feature)
        
        # Calculate and display results
        result = calculator.calculate_cost()
        print("\n--- Cost Breakdown ---")
        print(f"Wall Area: {result['area_sqft']} sqft")
        print(f"Base Cost: ${result['base_cost']:.2f}")
        
        if result['additional_costs']:
            print("\nAdditional Features:")
            for feature, cost in result['additional_costs'].items():
                print(f"- {feature.capitalize()}: ${cost:.2f}")
        
        print(f"\nTotal Estimated Cost: ${result['total_cost']:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
