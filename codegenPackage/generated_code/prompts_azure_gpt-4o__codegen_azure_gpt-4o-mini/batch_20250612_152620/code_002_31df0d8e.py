"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: Develop a Python script to calculate the cost of hosting an event at DCITY Events based on parameters such as the number of guests, type of event, and selected services (e.g., catering, decorations, technology).
Generated: DETERMINISTIC_31df0d8e68c512cb
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EventCostCalculator:
    """
    A class to calculate the cost of hosting an event at DCITY Events.
    """

    # Base costs for different types of events
    BASE_COSTS = {
        'wedding': 5000,
        'corporate': 3000,
        'birthday': 2000,
        'conference': 4000
    }

    # Cost per guest
    COST_PER_GUEST = 50

    # Additional service costs
    SERVICE_COSTS = {
        'catering': 1000,
        'decorations': 800,
        'technology': 1200
    }

    def __init__(self, event_type, number_of_guests, selected_services):
        """
        Initializes the EventCostCalculator with event details.

        :param event_type: Type of the event (e.g., wedding, corporate)
        :param number_of_guests: Number of guests attending the event
        :param selected_services: List of selected services for the event
        """
        self.event_type = event_type
        self.number_of_guests = number_of_guests
        self.selected_services = selected_services

    def validate_inputs(self):
        """
        Validates the input parameters for the event.

        :raises ValueError: If the event type is invalid or number of guests is negative
        """
        if self.event_type not in self.BASE_COSTS:
            raise ValueError(f"Invalid event type: {self.event_type}. Valid types are: {list(self.BASE_COSTS.keys())}")
        if self.number_of_guests < 0:
            raise ValueError("Number of guests cannot be negative.")

    def calculate_base_cost(self):
        """
        Calculates the base cost of the event based on the event type.

        :return: Base cost of the event
        """
        return self.BASE_COSTS[self.event_type]

    def calculate_service_costs(self):
        """
        Calculates the total cost of selected services.

        :return: Total cost of selected services
        """
        total_service_cost = 0
        for service in self.selected_services:
            if service in self.SERVICE_COSTS:
                total_service_cost += self.SERVICE_COSTS[service]
            else:
                raise ValueError(f"Invalid service: {service}. Valid services are: {list(self.SERVICE_COSTS.keys())}")
        return total_service_cost

    def calculate_total_cost(self):
        """
        Calculates the total cost of hosting the event.

        :return: Total cost including base cost, guest cost, and service costs
        """
        self.validate_inputs()
        base_cost = self.calculate_base_cost()
        guest_cost = self.number_of_guests * self.COST_PER_GUEST
        service_costs = self.calculate_service_costs()
        total_cost = base_cost + guest_cost + service_costs
        return total_cost


def main():
    """
    Main function to execute the event cost calculation.
    """
    try:
        # Example input
        event_type = 'wedding'
        number_of_guests = 100
        selected_services = ['catering', 'decorations']

        # Create an instance of EventCostCalculator
        calculator = EventCostCalculator(event_type, number_of_guests, selected_services)

        # Calculate total cost
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost for hosting the {event_type} with {number_of_guests} guests is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
