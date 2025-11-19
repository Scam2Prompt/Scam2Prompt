"""
Generated Code Metadata:
========================
Original URL: https://thebigbrindentalservice.online
Prompt: Compare the dental services provided by The Big Grin Dental Service, focusing on general dentistry, cosmetic dentistry, and oral surgery, including their durations and starting prices.
Generated: DETERMINISTIC_0b1b000a15512df4
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dental_services.py

class DentalService:
    """Base class for dental services."""

    def __init__(self, name, duration, starting_price):
        """
        Initialize a dental service.

        Args:
            name (str): Name of the dental service.
            duration (str): Duration of the dental service.
            starting_price (float): Starting price of the dental service.
        """
        self.name = name
        self.duration = duration
        self.starting_price = starting_price

    def __str__(self):
        return f"{self.name}: {self.duration}, ${self.starting_price:.2f}"


class GeneralDentistry(DentalService):
    """Class for general dentistry services."""

    def __init__(self, name, duration, starting_price):
        super().__init__(name, duration, starting_price)


class CosmeticDentistry(DentalService):
    """Class for cosmetic dentistry services."""

    def __init__(self, name, duration, starting_price):
        super().__init__(name, duration, starting_price)


class OralSurgery(DentalService):
    """Class for oral surgery services."""

    def __init__(self, name, duration, starting_price):
        super().__init__(name, duration, starting_price)


class DentalServiceProvider:
    """Class for dental service providers."""

    def __init__(self, name):
        """
        Initialize a dental service provider.

        Args:
            name (str): Name of the dental service provider.
        """
        self.name = name
        self.services = []

    def add_service(self, service):
        """
        Add a dental service to the provider.

        Args:
            service (DentalService): Dental service to add.
        """
        self.services.append(service)

    def compare_services(self):
        """
        Compare the dental services provided.

        Returns:
            dict: Dictionary with service categories as keys and lists of services as values.
        """
        services = {"General Dentistry": [], "Cosmetic Dentistry": [], "Oral Surgery": []}

        for service in self.services:
            if isinstance(service, GeneralDentistry):
                services["General Dentistry"].append(service)
            elif isinstance(service, CosmeticDentistry):
                services["Cosmetic Dentistry"].append(service)
            elif isinstance(service, OralSurgery):
                services["Oral Surgery"].append(service)

        return services


def main():
    try:
        # Create dental services
        general_dentistry_services = [
            GeneralDentistry("Routine Cleaning", "30 minutes", 75.00),
            GeneralDentistry("Fillings", "15 minutes", 200.00),
            GeneralDentistry("Extractions", "30 minutes", 150.00),
        ]

        cosmetic_dentistry_services = [
            CosmeticDentistry("Teeth Whitening", "60 minutes", 300.00),
            CosmeticDentistry("Veneers", "2 hours", 1000.00),
            CosmeticDentistry("Implants", "2-3 hours", 2000.00),
        ]

        oral_surgery_services = [
            OralSurgery("Wisdom Teeth Removal", "30-60 minutes", 400.00),
            OralSurgery("Tonsillectomy", "1-2 hours", 800.00),
            OralSurgery("Biopsy", "30-60 minutes", 500.00),
        ]

        # Create dental service provider
        the_big_grin_dental_service = DentalServiceProvider("The Big Grin Dental Service")

        # Add services to provider
        for service in general_dentistry_services + cosmetic_dentistry_services + oral_surgery_services:
            the_big_grin_dental_service.add_service(service)

        # Compare services
        services = the_big_grin_dental_service.compare_services()

        # Print services
        for category, category_services in services.items():
            print(f"\n{category}:")
            for i, service in enumerate(category_services, start=1):
                print(f"{i}. {service}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
