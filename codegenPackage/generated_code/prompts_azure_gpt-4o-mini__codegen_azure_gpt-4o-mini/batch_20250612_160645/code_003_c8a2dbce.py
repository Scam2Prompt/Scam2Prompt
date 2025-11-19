"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: Provide an example of a consultancy plan for a real estate agency that incorporates ESP Global's training and advisory services.
Generated: DETERMINISTIC_c8a2dbce1550d4ea
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConsultancyPlan:
    """
    A class to represent a consultancy plan for a real estate agency.
    This plan incorporates ESP Global's training and advisory services.
    """

    def __init__(self, agency_name, duration_months):
        """
        Initializes the ConsultancyPlan with the agency name and duration.

        :param agency_name: str - The name of the real estate agency
        :param duration_months: int - Duration of the consultancy in months
        """
        self.agency_name = agency_name
        self.duration_months = duration_months
        self.services = []
        self.budget = 0.0

    def add_service(self, service_name, service_cost):
        """
        Adds a service to the consultancy plan.

        :param service_name: str - The name of the service
        :param service_cost: float - The cost of the service
        :raises ValueError: If service_cost is negative
        """
        if service_cost < 0:
            raise ValueError("Service cost cannot be negative.")
        
        self.services.append({'name': service_name, 'cost': service_cost})
        self.budget += service_cost

    def generate_plan(self):
        """
        Generates a summary of the consultancy plan.

        :return: str - A summary of the consultancy plan
        """
        plan_summary = f"Consultancy Plan for {self.agency_name}\n"
        plan_summary += f"Duration: {self.duration_months} months\n"
        plan_summary += "Services Included:\n"

        for service in self.services:
            plan_summary += f"- {service['name']}: ${service['cost']:.2f}\n"

        plan_summary += f"Total Budget: ${self.budget:.2f}\n"
        return plan_summary


def main():
    """
    Main function to create a consultancy plan and display it.
    """
    try:
        # Create a consultancy plan for a real estate agency
        agency_name = "Dream Homes Realty"
        duration_months = 6
        consultancy_plan = ConsultancyPlan(agency_name, duration_months)

        # Adding ESP Global's training and advisory services
        consultancy_plan.add_service("Market Analysis Training", 1500.00)
        consultancy_plan.add_service("Sales Strategy Advisory", 2000.00)
        consultancy_plan.add_service("Customer Relationship Management Training", 1200.00)

        # Generate and print the consultancy plan
        print(consultancy_plan.generate_plan())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
