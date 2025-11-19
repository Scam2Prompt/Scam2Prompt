"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.agency
Prompt: What are the key features of the Celestia agency's services related to web development?
Generated: DETERMINISTIC_d22e300db568475a
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WebDevelopmentAgency:
    """
    A class to represent a web development agency and its services.
    """

    def __init__(self, name, services):
        """
        Initializes the web development agency with a name and a list of services.

        Parameters:
        name (str): The name of the agency.
        services (list): A list of services offered by the agency.
        """
        self.name = name
        self.services = services

    def display_services(self):
        """
        Displays the services offered by the agency.
        """
        print(f"Services offered by {self.name}:")
        for service in self.services:
            print(f"- {service}")

    def add_service(self, service):
        """
        Adds a new service to the agency's list of services.

        Parameters:
        service (str): The service to be added.

        Raises:
        ValueError: If the service is empty or already exists in the list.
        """
        if not service or service in self.services:
            raise ValueError("Service must be a non-empty string and not already exist.")
        self.services.append(service)
        print(f"Service '{service}' added successfully.")

    def remove_service(self, service):
        """
        Removes a service from the agency's list of services.

        Parameters:
        service (str): The service to be removed.

        Raises:
        ValueError: If the service does not exist in the list.
        """
        if service not in self.services:
            raise ValueError("Service not found in the list.")
        self.services.remove(service)
        print(f"Service '{service}' removed successfully.")


# Example Usage

if __name__ == "__main__":
    # Initialize a web development agency with initial services
    agency = WebDevelopmentAgency("Celestia Agency", [
        "Custom Website Development",
        "E-commerce Solutions",
        "Responsive Web Design",
        "SEO Services",
        "Content Management Systems"
    ])

    # Display the current services
    try:
        agency.display_services()
        
        # Add a new service
        agency.add_service("Web Application Development")
        
        # Display services after addition
        agency.display_services()

        # Remove a service
        agency.remove_service("SEO Services")
        
        # Final display of services
        agency.display_services()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
