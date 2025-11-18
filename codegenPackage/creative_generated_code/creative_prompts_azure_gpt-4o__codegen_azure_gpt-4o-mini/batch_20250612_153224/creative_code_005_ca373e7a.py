"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivekenterprises.co.in
Prompt: Write code to generate a project cost estimation tool for a company specializing in turnkey interior contracting, factoring in services like furniture design, HVAC, and electrical works.
Generated: DETERMINISTIC_ca373e7ae9be5686
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ProjectCostEstimator:
    """
    A class to estimate the cost of a turnkey interior contracting project.
    """

    def __init__(self):
        # Initialize cost factors
        self.cost_factors = {
            "furniture_design": 100,  # Cost per unit for furniture design
            "hvac": 150,               # Cost per unit for HVAC works
            "electrical": 120,         # Cost per unit for electrical works
        }
        self.total_cost = 0

    def estimate_cost(self, service_type, quantity):
        """
        Estimate the cost for a specific service type based on the quantity required.

        Parameters:
        service_type (str): The type of service (furniture_design, hvac, electrical)
        quantity (int): The number of units required for the service

        Returns:
        float: Estimated cost for the service
        """
        if service_type not in self.cost_factors:
            raise ValueError(f"Invalid service type: {service_type}")
        
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        
        cost = self.cost_factors[service_type] * quantity
        self.total_cost += cost
        return cost

    def get_total_cost(self):
        """
        Get the total estimated cost for all services.

        Returns:
        float: Total estimated cost
        """
        return self.total_cost

    def reset_estimator(self):
        """
        Reset the total cost to zero for a new estimation.
        """
        self.total_cost = 0

    def save_estimation(self, filename):
        """
        Save the current estimation results to a JSON file.

        Parameters:
        filename (str): The name of the file to save the estimation
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "total_cost": self.total_cost,
                    "cost_factors": self.cost_factors
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving estimation to file: {e}")

def main():
    estimator = ProjectCostEstimator()
    
    try:
        # Example service estimations
        furniture_cost = estimator.estimate_cost("furniture_design", 10)
        print(f"Furniture Design Cost: ${furniture_cost:.2f}")

        hvac_cost = estimator.estimate_cost("hvac", 5)
        print(f"HVAC Cost: ${hvac_cost:.2f}")

        electrical_cost = estimator.estimate_cost("electrical", 8)
        print(f"Electrical Works Cost: ${electrical_cost:.2f}")

        total_cost = estimator.get_total_cost()
        print(f"Total Estimated Cost: ${total_cost:.2f}")

        # Save the estimation to a file
        estimator.save_estimation("project_estimation.json")

    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()
```
