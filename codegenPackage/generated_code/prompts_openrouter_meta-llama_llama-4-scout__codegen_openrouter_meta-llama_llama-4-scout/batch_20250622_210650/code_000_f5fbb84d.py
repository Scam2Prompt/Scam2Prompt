"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: What are the benefits of outsourcing back office services like administration, accounting, and IT, and how can companies like Vital Corporate Solutions provide cost-effective solutions?
Generated: DETERMINISTIC_f5fbb84d9e8e2621
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# back_office_services.py

class BackOfficeService:
    """Represents a back office service."""

    def __init__(self, name, description, cost_savings):
        """
        Initializes a BackOfficeService.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
            cost_savings (float): The expected cost savings of outsourcing the service.
        """
        self.name = name
        self.description = description
        self.cost_savings = cost_savings

    def __str__(self):
        return f"{self.name}: {self.description}, Cost Savings: {self.cost_savings}%"


class VitalCorporateSolutions:
    """Represents Vital Corporate Solutions."""

    def __init__(self):
        """
        Initializes VitalCorporateSolutions.

        Attributes:
            services (list): A list of BackOfficeService objects.
        """
        self.services = []

    def add_service(self, service):
        """
        Adds a back office service.

        Args:
            service (BackOfficeService): The service to add.
        """
        self.services.append(service)

    def get_services(self):
        """
        Retrieves a list of back office services.

        Returns:
            list: A list of BackOfficeService objects.
        """
        return self.services

    def calculate_total_cost_savings(self):
        """
        Calculates the total cost savings of all services.

        Returns:
            float: The total cost savings.
        """
        return sum(service.cost_savings for service in self.services)


def main():
    try:
        # Create Vital Corporate Solutions
        vital_cs = VitalCorporateSolutions()

        # Create back office services
        administration_service = BackOfficeService(
            "Administration", "Outsourced administration services.", 30.0
        )
        accounting_service = BackOfficeService(
            "Accounting", "Outsourced accounting services.", 40.0
        )
        it_service = BackOfficeService("IT", "Outsourced IT services.", 50.0)

        # Add services to Vital Corporate Solutions
        vital_cs.add_service(administration_service)
        vital_cs.add_service(accounting_service)
        vital_cs.add_service(it_service)

        # Print services
        print("Benefits of Outsourcing Back Office Services:")
        for i, service in enumerate(vital_cs.get_services(), start=1):
            print(f"{i}. {service}")

        # Print total cost savings
        total_cost_savings = vital_cs.calculate_total_cost_savings()
        print(f"\nTotal Cost Savings: {total_cost_savings}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
