"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Generate a Python function to format and display Ashvi Facility Management's service offerings (e.g., housekeeping, carpet cleaning) in a user-friendly interface.
Generated: DETERMINISTIC_69c35cec6dfff841
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class ServiceFormatter:
    """
    A class to format and display Ashvi Facility Management's service offerings.
    """

    def __init__(self, services_data: List[Dict[str, str]] = None):
        """
        Initialize the ServiceFormatter with optional services data.
        
        Args:
            services_data (List[Dict[str, str]], optional): List of service dictionaries. 
                Each dictionary should contain 'name' and 'description' keys.
                Defaults to None (will use default services).
        """
        self.services = services_data or self._get_default_services()

    def _get_default_services(self) -> List[Dict[str, str]]:
        """
        Get the default list of Ashvi Facility Management services.
        
        Returns:
            List[Dict[str, str]]: Default list of services with names and descriptions.
        """
        return [
            {"name": "Housekeeping", "description": "Professional cleaning of residential and commercial spaces."},
            {"name": "Carpet Cleaning", "description": "Deep cleaning and stain removal for all carpet types."},
            {"name": "Window Cleaning", "description": "Interior and exterior window cleaning services."},
            {"name": "Floor Maintenance", "description": "Polishing, waxing, and general floor care."},
            {"name": "Sanitization Services", "description": "Disinfection and sanitization for health and safety."}
        ]

    def display_services(self, format_type: str = "console") -> None:
        """
        Display the services in the specified format.
        
        Args:
            format_type (str, optional): Format to display services ('console', 'json', 'pretty'). 
                Defaults to "console".
        
        Raises:
            ValueError: If an invalid format_type is provided.
        """
        if format_type == "console":
            self._display_console()
        elif format_type == "json":
            self._display_json()
        elif format_type == "pretty":
            self._display_pretty()
        else:
            raise ValueError(f"Invalid format type: {format_type}. Choose 'console', 'json', or 'pretty'.")

    def _display_console(self) -> None:
        """Display services in a simple console format."""
        print("\nAshvi Facility Management Services:")
        print("---------------------------------")
        for service in self.services:
            print(f"\nService: {service['name']}")
            print(f"Description: {service['description']}")
        print("\n")

    def _display_json(self) -> None:
        """Display services in JSON format."""
        print(json.dumps({"services": self.services}, indent=2))

    def _display_pretty(self) -> None:
        """Display services in a visually appealing format."""
        border = "=" * 50
        print(f"\n{border}")
        print(" ASHVI FACILITY MANAGEMENT SERVICE OFFERINGS ".center(50))
        print(f"{border}\n")
        
        for i, service in enumerate(self.services, 1):
            print(f"{i}. {service['name'].upper()}")
            print(f"   {service['description']}\n")
        
        print(f"{border}\n")

    def add_service(self, name: str, description: str) -> None:
        """
        Add a new service to the offerings.
        
        Args:
            name (str): Name of the service.
            description (str): Description of the service.
        """
        if not name or not description:
            raise ValueError("Service name and description cannot be empty.")
        
        self.services.append({"name": name, "description": description})

    def get_services(self) -> List[Dict[str, str]]:
        """
        Get the current list of services.
        
        Returns:
            List[Dict[str, str]]: Current list of services.
        """
        return self.services


# Example usage
if __name__ == "__main__":
    try:
        formatter = ServiceFormatter()
        
        print("Displaying services in console format:")
        formatter.display_services("console")
        
        print("\nDisplaying services in pretty format:")
        formatter.display_services("pretty")
        
        print("\nDisplaying services in JSON format:")
        formatter.display_services("json")
        
        # Adding a new service
        formatter.add_service("Pest Control", "Professional pest elimination and prevention services.")
        
        print("\nDisplaying updated services in pretty format:")
        formatter.display_services("pretty")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
