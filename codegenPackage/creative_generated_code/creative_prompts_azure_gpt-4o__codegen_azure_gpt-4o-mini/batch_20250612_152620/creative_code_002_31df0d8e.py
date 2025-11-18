"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Develop a Python script to calculate the cost of hosting an event at DCITY Events based on parameters such as the number of guests, type of event, and selected services (e.g., catering, decorations, technology).
Generated: DETERMINISTIC_31df0d8e68c512cb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EventCostCalculator:
    """
    A class to calculate the cost of hosting an event at DCITY Events based on various parameters.
    """

    def __init__(self, base_cost_per_guest=50, service_costs=None):
        """
        Initializes the EventCostCalculator with base costs.
        
        :param base_cost_per_guest: Base cost per guest (default is $50).
        :param service_costs: Dictionary of additional service costs (default is None).
        """
        self.base_cost_per_guest = base_cost_per_guest
        self.service_costs = service_costs if service_costs else {
            'catering': 20,
            'decorations': 15,
            'technology': 30
        }

    def calculate_base_cost(self, num_guests):
        """
        Calculates the base cost based on the number of guests.
        
        :param num_guests: Number of guests attending the event.
        :return: Total base cost for guests.
        """
        if num_guests < 0:
            raise ValueError("Number of guests cannot be negative.")
        return self.base_cost_per_guest * num_guests

    def calculate_services_cost(self, selected_services):
        """
        Calculates the total cost of selected services.
        
        :param selected_services: List of services selected for the event.
        :return: Total cost of selected services.
        """
        total_service_cost = 0
        for service in selected_services:
            service_cost = self.service_costs.get(service)
            if service_cost is None:
                raise ValueError(f"Service '{service}' is not available.")
            total_service_cost += service_cost
        return total_service_cost

    def calculate_total_cost(self, num_guests, selected_services):
        """
        Calculates the total cost of the event including base cost and selected services.
        
        :param num_guests: Number of guests attending the event.
        :param selected_services: List of services selected for the event.
        :return: Total cost of the event.
        """
        base_cost = self.calculate_base_cost(num_guests)
        services_cost = self.calculate_services_cost(selected_services)
        return base_cost + services_cost


def main():
    """
    Main function to execute the event cost calculation.
    """
    try:
        # Input parameters for event cost calculation
        num_guests = int(input("Enter the number of guests: "))
        selected_services = input("Enter selected services (catering, decorations, technology) separated by commas: ")
        selected_services = [service.strip() for service in selected_services.split(',')]

        # Create an instance of EventCostCalculator
        calculator = EventCostCalculator()

        # Calculate total cost
        total_cost = calculator.calculate_total_cost(num_guests, selected_services)

        # Output the total cost
        print(f"The total cost for hosting the event is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
