"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: Provide an example of a consultancy plan for a real estate agency that incorporates ESP Global's training and advisory services.
Generated: DETERMINISTIC_c8a2dbce1550d4ea
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConsultancyPlan:
    """
    A class to represent a consultancy plan for a real estate agency incorporating ESP Global's training 
    and advisory services.
    """
    
    def __init__(self, agency_name, duration_months):
        """
        Initialize the ConsultancyPlan with the agency's name and the duration of the plan in months.
        
        Args:
            agency_name (str): The name of the real estate agency.
            duration_months (int): The total duration of the consultancy plan in months.
        """
        if not isinstance(agency_name, str) or not agency_name:
            raise ValueError("Agency name must be a non-empty string.")
        if not isinstance(duration_months, int) or duration_months <= 0:
            raise ValueError("Duration must be a positive integer.")

        self.agency_name = agency_name
        self.duration_months = duration_months
        self.services = []
    
    def add_service(self, service_name, description, cost):
        """
        Add a service to the consultancy plan.
        
        Args:
            service_name (str): The name of the service.
            description (str): A brief description of the service.
            cost (float): The cost of the service.

        Raises:
            ValueError: If service_name is empty or cost is not a positive number.
        """
        if not isinstance(service_name, str) or not service_name:
            raise ValueError("Service name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(cost, (int, float)) or cost <= 0:
            raise ValueError("Cost must be a positive number.")
        
        service = {
            "name": service_name,
            "description": description,
            "cost": cost
        }
        self.services.append(service)
    
    def total_cost(self):
        """
        Calculate the total cost of the consultancy plan.
        
        Returns:
            float: The total cost of all services included in the plan.
        """
        return sum(service['cost'] for service in self.services)
    
    def generate_plan_summary(self):
        """
        Generate a summary of the consultancy plan including agency name, duration, 
        services provided, and total cost.
        
        Returns:
            str: A summary of the consultancy plan.
        """
        summary_lines = [
            f"Consultancy Plan for: {self.agency_name}",
            f"Duration: {self.duration_months} months",
            "Services included:"
        ]
        
        for service in self.services:
            summary_lines.append(f"- {service['name']}: {service['description']} (${service['cost']})")
        
        summary_lines.append(f"Total Cost: ${self.total_cost()}")
        return "\n".join(summary_lines)

# Example usage:
if __name__ == "__main__":
    try:
        # Create a consultancy plan for a real estate agency
        plan = ConsultancyPlan("Dream Homes Agency", 12)

        # Add services to the plan
        plan.add_service("Market Analysis", "In-depth analysis of current market trends.", 1500.00)
        plan.add_service("Sales Training", "Training for sales team on effective selling techniques.", 2000.00)
        plan.add_service("Client Management Advisory", "Advisory on best client management practices.", 1800.00)

        # Generate and print the plan summary
        print(plan.generate_plan_summary())
        
    except ValueError as e:
        print(f"Error: {e}")
```
