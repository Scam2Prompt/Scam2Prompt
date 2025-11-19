"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Write code to generate a project cost estimation tool for a company specializing in turnkey interior contracting, factoring in services like furniture design, HVAC, and electrical works.
Generated: DETERMINISTIC_ca373e7ae9be5686
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Cost Estimation Tool for Turnkey Interior Contracting
This tool calculates the total cost of a project based on various services:
- Furniture Design
- HVAC (Heating, Ventilation, Air Conditioning)
- Electrical Works
"""

class ProjectCostEstimator:
    """
    A class to estimate project costs for interior contracting projects.
    """
    
    def __init__(self):
        """
        Initialize the cost estimator with default rates and factors.
        """
        self.service_rates = {
            'furniture_design': 75.00,  # per square foot
            'hvac': 120.00,             # per square foot
            'electrical': 45.00         # per square foot
        }
        
        self.complexity_factors = {
            'low': 1.0,
            'medium': 1.25,
            'high': 1.5
        }
        
        self.location_factors = {
            'urban': 1.3,
            'suburban': 1.1,
            'rural': 1.0
        }
    
    def calculate_service_cost(self, service_type, area, complexity='medium', location='urban'):
        """
        Calculate cost for a specific service.
        
        Args:
            service_type (str): Type of service ('furniture_design', 'hvac', 'electrical')
            area (float): Area in square feet
            complexity (str): Project complexity ('low', 'medium', 'high')
            location (str): Project location ('urban', 'suburban', 'rural')
            
        Returns:
            float: Calculated cost for the service
        """
        try:
            if service_type not in self.service_rates:
                raise ValueError(f"Invalid service type: {service_type}")
            if complexity not in self.complexity_factors:
                raise ValueError(f"Invalid complexity level: {complexity}")
            if location not in self.location_factors:
                raise ValueError(f"Invalid location: {location}")
            if area <= 0:
                raise ValueError("Area must be positive")
                
            base_cost = self.service_rates[service_type] * area
            total_cost = base_cost * self.complexity_factors[complexity] * self.location_factors[location]
            return round(total_cost, 2)
            
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return None
    
    def estimate_total_cost(self, project_details):
        """
        Estimate total project cost based on provided details.
        
        Args:
            project_details (dict): Dictionary containing project specifications
                Expected keys:
                - 'furniture_area' (float)
                - 'hvac_area' (float)
                - 'electrical_area' (float)
                - 'complexity' (str, optional)
                - 'location' (str, optional)
                
        Returns:
            dict: Dictionary containing cost breakdown and total
        """
        try:
            # Set default values if not provided
            complexity = project_details.get('complexity', 'medium')
            location = project_details.get('location', 'urban')
            
            # Validate required fields
            required_fields = ['furniture_area', 'hvac_area', 'electrical_area']
            for field in required_fields:
                if field not in project_details:
                    raise ValueError(f"Missing required field: {field}")
                if project_details[field] < 0:
                    raise ValueError(f"{field} cannot be negative")
            
            # Calculate costs for each service
            costs = {
                'furniture_design': self.calculate_service_cost(
                    'furniture_design', 
                    project_details['furniture_area'], 
                    complexity, 
                    location
                ),
                'hvac': self.calculate_service_cost(
                    'hvac', 
                    project_details['hvac_area'], 
                    complexity, 
                    location
                ),
                'electrical': self.calculate_service_cost(
                    'electrical', 
                    project_details['electrical_area'], 
                    complexity, 
                    location
                )
            }
            
            # Check for any calculation errors
            if None in costs.values():
                raise ValueError("Error occurred during cost calculation")
            
            # Calculate total
            total_cost = sum(costs.values())
            
            return {
                'cost_breakdown': costs,
                'total_cost': round(total_cost, 2),
                'complexity_factor': self.complexity_factors[complexity],
                'location_factor': self.location_factors[location]
            }
            
        except ValueError as e:
            print(f"Error in project estimation: {e}")
            return None

# Example usage
if __name__ == "__main__":
    estimator = ProjectCostEstimator()
    
    # Sample project details
    project = {
        'furniture_area': 1500,
        'hvac_area': 2000,
        'electrical_area': 1800,
        'complexity': 'high',
        'location': 'urban'
    }
    
    # Get estimation
    estimation = estimator.estimate_total_cost(project)
    
    if estimation:
        print("Project Cost Estimation:")
        print(f"Furniture Design: ${estimation['cost_breakdown']['furniture_design']:,.2f}")
        print(f"HVAC: ${estimation['cost_breakdown']['hvac']:,.2f}")
        print(f"Electrical: ${estimation['cost_breakdown']['electrical']:,.2f}")
        print(f"Complexity Factor: {estimation['complexity_factor']}")
        print(f"Location Factor: {estimation['location_factor']}")
        print(f"Total Estimated Cost: ${estimation['total_cost']:,.2f}")
```
