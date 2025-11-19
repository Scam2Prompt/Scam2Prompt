"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script to calculate the cost of consulting services for architectural projects, factoring in additional services beyond the initial agreement as described by TWM Associates.
Generated: DETERMINISTIC_460576b00c7d6969
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consulting_services_calculator.py

class ConsultingService:
    def __init__(self, name, hourly_rate):
        """
        Initialize a consulting service.

        Args:
            name (str): Name of the service.
            hourly_rate (float): Hourly rate of the service.
        """
        self.name = name
        self.hourly_rate = hourly_rate

class Project:
    def __init__(self, name, initial_agreement_hours):
        """
        Initialize a project.

        Args:
            name (str): Name of the project.
            initial_agreement_hours (float): Initial agreement hours.
        """
        self.name = name
        self.initial_agreement_hours = initial_agreement_hours
        self.additional_services = []

    def add_additional_service(self, service, hours):
        """
        Add an additional service to the project.

        Args:
            service (ConsultingService): Service to add.
            hours (float): Number of hours for the service.
        """
        self.additional_services.append((service, hours))

    def calculate_total_cost(self, initial_agreement_rate):
        """
        Calculate the total cost of the project.

        Args:
            initial_agreement_rate (float): Hourly rate for the initial agreement.

        Returns:
            float: Total cost of the project.
        """
        initial_agreement_cost = self.initial_agreement_hours * initial_agreement_rate
        additional_services_cost = sum(service.hourly_rate * hours for service, hours in self.additional_services)
        return initial_agreement_cost + additional_services_cost

def main():
    try:
        # Define consulting services
        architectural_design = ConsultingService("Architectural Design", 150.0)
        construction_management = ConsultingService("Construction Management", 200.0)

        # Define project
        project = Project("TWM Associates Architectural Project", 100.0)

        # Add additional services
        project.add_additional_service(architectural_design, 20.0)
        project.add_additional_service(construction_management, 30.0)

        # Calculate total cost
        initial_agreement_rate = 120.0
        total_cost = project.calculate_total_cost(initial_agreement_rate)

        # Print result
        print(f"Project: {project.name}")
        print(f"Initial Agreement Hours: {project.initial_agreement_hours} hours")
        print(f"Initial Agreement Rate: ${initial_agreement_rate:.2f}/hour")
        print(f"Initial Agreement Cost: ${project.initial_agreement_hours * initial_agreement_rate:.2f}")
        print("Additional Services:")
        for service, hours in project.additional_services:
            print(f"- {service.name}: {hours:.2f} hours @ ${service.hourly_rate:.2f}/hour = ${service.hourly_rate * hours:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
