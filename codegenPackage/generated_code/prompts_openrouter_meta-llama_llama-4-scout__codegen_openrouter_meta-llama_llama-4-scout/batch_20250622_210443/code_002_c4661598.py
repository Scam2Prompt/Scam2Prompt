"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Write a code snippet to simulate a 24/7 helpdesk service for plumbing emergencies, similar to ERA ENGINEERING's support system."
Generated: DETERMINISTIC_c4661598a44507a9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random

class HelpdeskService:
    """
    Simulates a 24/7 helpdesk service for plumbing emergencies.
    """

    def __init__(self):
        """
        Initializes the helpdesk service with a list of available technicians.
        """
        self.technicians = [
            {"name": "John Doe", "availability": True},
            {"name": "Jane Smith", "availability": True},
            {"name": "Bob Johnson", "availability": True},
        ]

    def request_assistance(self, customer_name, emergency_description):
        """
        Requests assistance for a plumbing emergency.

        Args:
            customer_name (str): The name of the customer requesting assistance.
            emergency_description (str): A description of the plumbing emergency.

        Returns:
            str: A confirmation message with the assigned technician's name.
        """
        try:
            available_technician = self._get_available_technician()
            if available_technician:
                self._assign_request(customer_name, emergency_description, available_technician["name"])
                return f"Assistance requested. Technician {available_technician['name']} assigned to your case."
            else:
                return "No technicians available at this time. Please try again later."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def _get_available_technician(self):
        """
        Retrieves an available technician.

        Returns:
            dict: A dictionary containing the available technician's information.
        """
        available_technicians = [tech for tech in self.technicians if tech["availability"]]
        if available_technicians:
            return random.choice(available_technicians)
        return None

    def _assign_request(self, customer_name, emergency_description, technician_name):
        """
        Assigns the request to a technician.

        Args:
            customer_name (str): The name of the customer requesting assistance.
            emergency_description (str): A description of the plumbing emergency.
            technician_name (str): The name of the assigned technician.
        """
        print(f"Request assigned to {technician_name}:")
        print(f"Customer: {customer_name}")
        print(f"Emergency Description: {emergency_description}")
        print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)

    def update_technician_availability(self, technician_name, availability):
        """
        Updates a technician's availability.

        Args:
            technician_name (str): The name of the technician.
            availability (bool): The updated availability status.
        """
        for tech in self.technicians:
            if tech["name"] == technician_name:
                tech["availability"] = availability
                break


def main():
    helpdesk = HelpdeskService()

    while True:
        print("1. Request Assistance")
        print("2. Update Technician Availability")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            customer_name = input("Enter your name: ")
            emergency_description = input("Describe your emergency: ")
            print(helpdesk.request_assistance(customer_name, emergency_description))
        elif choice == "2":
            technician_name = input("Enter technician's name: ")
            availability = input("Enter availability (yes/no): ")
            helpdesk.update_technician_availability(technician_name, availability.lower() == "yes")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
