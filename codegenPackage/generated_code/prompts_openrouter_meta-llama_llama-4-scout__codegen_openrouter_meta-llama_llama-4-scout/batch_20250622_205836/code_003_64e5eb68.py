"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a basic fixed-price services menu for a legal and accounting firm, inspired by Carthew Chau & Co's approach, including services like company and trust setup, tax returns, and superannuation planning.
Generated: DETERMINISTIC_64e5eb6839e8caf4
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services_menu.py

class Service:
    """Represents a service offered by the firm."""

    def __init__(self, name, description, price):
        """
        Initializes a Service instance.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
            price (float): The fixed price of the service.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, Price: ${self.price:.2f}"


class ServicesMenu:
    """Represents the services menu of the firm."""

    def __init__(self):
        """Initializes an empty services menu."""
        self.services = []

    def add_service(self, service):
        """
        Adds a service to the menu.

        Args:
            service (Service): The service to add.
        """
        self.services.append(service)

    def remove_service(self, service_name):
        """
        Removes a service from the menu.

        Args:
            service_name (str): The name of the service to remove.

        Raises:
            ValueError: If the service is not found.
        """
        for service in self.services:
            if service.name == service_name:
                self.services.remove(service)
                return
        raise ValueError(f"Service '{service_name}' not found.")

    def display_menu(self):
        """Displays the services menu."""
        print("Services Menu:")
        for i, service in enumerate(self.services, start=1):
            print(f"{i}. {service}")


class CompanySetup(Service):
    """Represents company setup service."""

    def __init__(self):
        super().__init__("Company Setup", "Setup a new company", 1000.0)


class TrustSetup(Service):
    """Represents trust setup service."""

    def __init__(self):
        super().__init__("Trust Setup", "Setup a new trust", 800.0)


class TaxReturns(Service):
    """Represents tax returns service."""

    def __init__(self):
        super().__init__("Tax Returns", "Prepare and lodge tax returns", 500.0)


class SuperannuationPlanning(Service):
    """Represents superannuation planning service."""

    def __init__(self):
        super().__init__("Superannuation Planning", "Develop a superannuation plan", 1200.0)


def main():
    try:
        menu = ServicesMenu()

        company_setup = CompanySetup()
        trust_setup = TrustSetup()
        tax_returns = TaxReturns()
        superannuation_planning = SuperannuationPlanning()

        menu.add_service(company_setup)
        menu.add_service(trust_setup)
        menu.add_service(tax_returns)
        menu.add_service(superannuation_planning)

        menu.display_menu()

        # Example usage: Remove a service
        menu.remove_service("Tax Returns")
        print("\nUpdated Menu:")
        menu.display_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
