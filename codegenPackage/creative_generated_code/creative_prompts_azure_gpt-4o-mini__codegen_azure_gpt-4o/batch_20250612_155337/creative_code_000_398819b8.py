"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepbook.online
Prompt: Generate a Python script that simulates a plumbing service request system, allowing users to select services like drain cleaning and gas line repairs.
Generated: DETERMINISTIC_398819b806f37f0b
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class PlumbingServiceRequestSystem:
    """
    A simple plumbing service request system allowing users to select various services.
    """

    def __init__(self):
        """
        Initializes the PlumbingServiceRequestSystem with a list of available services and their prices.
        """
        self.services = {
            "1": {"name": "Drain Cleaning", "price": 100},
            "2": {"name": "Gas Line Repairs", "price": 250},
            "3": {"name": "Leak Fixing", "price": 150},
            "4": {"name": "Pipe Replacement", "price": 300},
        }
        self.selected_services = []

    def display_services(self):
        """
        Displays the list of available plumbing services to the user.
        """
        print("\nAvailable Plumbing Services:")
        for key, service in self.services.items():
            print(f"{key}. {service['name']} - ${service['price']}")

    def select_service(self):
        """
        Allows the user to select services by providing the corresponding service number.
        """
        try:
            service_number = input("\nEnter the number of the service you want to select (or 'done' to finish): ")
            if service_number.lower() == "done":
                return False
            elif service_number in self.services:
                service = self.services[service_number]
                self.selected_services.append(service)
                print(f"Service '{service['name']}' added to your request.")
                return True
            else:
                print("Invalid service number. Please try again.")
                return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return True

    def calculate_total(self):
        """
        Calculates the total cost of the selected services.
        """
        total = sum(service["price"] for service in self.selected_services)
        return total

    def display_summary(self):
        """
        Displays a summary of the selected services and the total cost.
        """
        if not self.selected_services:
            print("\nNo services selected.")
            return
        print("\nSummary of Selected Services:")
        for service in self.selected_services:
            print(f"- {service['name']} - ${service['price']}")
        print(f"Total Cost: ${self.calculate_total()}")

def main():
    """
    Main function to run the Plumbing Service Request System.
    """
    print("Welcome to the Plumbing Service Request System!")
    system = PlumbingServiceRequestSystem()

    system.display_services()

    while True:
        continue_selection = system.select_service()
        if not continue_selection:
            break

    system.display_summary()

    print("\nThank you for using the Plumbing Service Request System!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
