"""
Generated Code Metadata:
========================
Original URL: https://elchallao.com.ar
Prompt: Develop a code snippet that lists the services provided at El Challao, such as WiFi, air conditioning, and cable TV.
Generated: DETERMINISTIC_649cb6d9fa0c257d
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services.py

class Service:
    """Represents a service provided at El Challao."""

    def __init__(self, name, description):
        """
        Initializes a Service object.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """Returns a string representation of the service."""
        return f"{self.name}: {self.description}"


class ElChallaoServices:
    """Lists the services provided at El Challao."""

    def __init__(self):
        """Initializes a list of services provided at El Challao."""
        self.services = [
            Service("WiFi", "High-speed internet access"),
            Service("Air Conditioning", "Cooling system for comfortable stay"),
            Service("Cable TV", "Access to various TV channels"),
            # Add more services as needed
        ]

    def list_services(self):
        """
        Prints a list of services provided at El Challao.

        Returns:
            None
        """
        if not self.services:
            print("No services available.")
            return

        print("Services at El Challao:")
        for i, service in enumerate(self.services, start=1):
            print(f"{i}. {service}")

    def add_service(self, name, description):
        """
        Adds a new service to the list.

        Args:
            name (str): The name of the service.
            description (str): A brief description of the service.

        Returns:
            None
        """
        if not name or not description:
            print("Error: Service name and description are required.")
            return

        new_service = Service(name, description)
        self.services.append(new_service)
        print(f"Service '{name}' added successfully.")

    def remove_service(self, name):
        """
        Removes a service from the list.

        Args:
            name (str): The name of the service to remove.

        Returns:
            None
        """
        if not name:
            print("Error: Service name is required.")
            return

        for service in self.services:
            if service.name.lower() == name.lower():
                self.services.remove(service)
                print(f"Service '{name}' removed successfully.")
                return

        print(f"Error: Service '{name}' not found.")


def main():
    try:
        el_challao_services = ElChallaoServices()
        while True:
            print("\nEl Challao Services Menu:")
            print("1. List Services")
            print("2. Add Service")
            print("3. Remove Service")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                el_challao_services.list_services()
            elif choice == "2":
                name = input("Enter service name: ")
                description = input("Enter service description: ")
                el_challao_services.add_service(name, description)
            elif choice == "3":
                name = input("Enter service name to remove: ")
                el_challao_services.remove_service(name)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
