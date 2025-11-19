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
# event_cost_calculator.py

class Event:
    def __init__(self, num_guests, event_type):
        """
        Initialize an Event object.

        Args:
            num_guests (int): The number of guests attending the event.
            event_type (str): The type of event (e.g., wedding, conference, party).
        """
        self.num_guests = num_guests
        self.event_type = event_type
        self.services = {}

    def add_service(self, service_name, service_cost):
        """
        Add a service to the event.

        Args:
            service_name (str): The name of the service (e.g., catering, decorations, technology).
            service_cost (float): The cost of the service.
        """
        self.services[service_name] = service_cost

    def calculate_base_cost(self):
        """
        Calculate the base cost of the event based on the number of guests and event type.

        Returns:
            float: The base cost of the event.
        """
        base_costs = {
            'wedding': 5000,
            'conference': 2000,
            'party': 1000
        }
        base_cost_per_guest = 50

        base_cost = base_costs.get(self.event_type, 0)
        base_cost += self.num_guests * base_cost_per_guest

        return base_cost

    def calculate_total_cost(self):
        """
        Calculate the total cost of the event, including services.

        Returns:
            float: The total cost of the event.
        """
        base_cost = self.calculate_base_cost()
        services_cost = sum(self.services.values())

        return base_cost + services_cost


def main():
    try:
        num_guests = int(input("Enter the number of guests: "))
        event_type = input("Enter the type of event (e.g., wedding, conference, party): ")

        event = Event(num_guests, event_type)

        print("Available services:")
        print("1. Catering ($5000 for 100 guests)")
        print("2. Decorations ($2000)")
        print("3. Technology ($1500)")

        while True:
            choice = input("Enter the number of the service to add (or 'done' to finish): ")
            if choice.lower() == 'done':
                break

            if choice == '1':
                catering_cost = 5000 + (num_guests - 100) * 50 if num_guests > 100 else 5000
                event.add_service('Catering', catering_cost)
            elif choice == '2':
                event.add_service('Decorations', 2000)
            elif choice == '3':
                event.add_service('Technology', 1500)
            else:
                print("Invalid choice. Please try again.")

        base_cost = event.calculate_base_cost()
        total_cost = event.calculate_total_cost()

        print(f"\nEvent Details:")
        print(f"Type: {event.event_type}")
        print(f"Number of Guests: {event.num_guests}")
        print(f"Base Cost: ${base_cost:.2f}")
        print("Services:")
        for service, cost in event.services.items():
            print(f"- {service}: ${cost:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
