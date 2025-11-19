"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a program that generates a list of accredited meter verification services in Tambov, using the example of ИП Семьянинов Сергей Юрьевич and the phone number "22-22-10".
Generated: DETERMINISTIC_a6f2c517328ac01a
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# accredited_meter_verification_services.py

class AccreditedService:
    """Represents an accredited meter verification service."""

    def __init__(self, name, phone_number):
        """
        Initializes an AccreditedService instance.

        Args:
            name (str): The name of the service.
            phone_number (str): The phone number of the service.
        """
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class AccreditedServiceGenerator:
    """Generates a list of accredited meter verification services."""

    def __init__(self, city):
        """
        Initializes an AccreditedServiceGenerator instance.

        Args:
            city (str): The city for which to generate services.
        """
        self.city = city
        self.services = []

    def add_service(self, name, phone_number):
        """
        Adds an accredited service to the list.

        Args:
            name (str): The name of the service.
            phone_number (str): The phone number of the service.
        """
        self.services.append(AccreditedService(name, phone_number))

    def generate_services(self):
        """
        Generates a list of accredited meter verification services.

        Returns:
            list[AccreditedService]: A list of accredited services.
        """
        # Example service
        self.add_service("ИП Семьянинов Сергей Юрьевич", "22-22-10")

        # In a real-world scenario, this data would likely come from a database or API
        # For demonstration purposes, we'll just add a few more examples
        self.add_service("ООО МетроСервис", "12-34-56")
        self.add_service("ПАО ВымпелКом", "78-90-12")

        return self.services


def main():
    try:
        city = "Tambov"
        generator = AccreditedServiceGenerator(city)
        services = generator.generate_services()

        print(f"Accredited Meter Verification Services in {city}:")
        for i, service in enumerate(services, start=1):
            print(f"{i}. {service}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
