"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write a Python script to manage a handyman service business, including services like osmosis inversa installation, electrodomestic repair, and fontanería maintenance in Murcia.
Generated: DETERMINISTIC_5c5e9f99e744a0ab
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HandymanService:
    def __init__(self):
        """Initialize the handyman service with an empty service list."""
        self.services: List[Dict[str, Any]] = []

    def add_service(self, name: str, description: str, price: float) -> None:
        """
        Add a new service to the handyman service list.

        :param name: The name of the service.
        :param description: A brief description of the service.
        :param price: The price of the service.
        """
        if price < 0:
            logging.error("Price cannot be negative.")
            raise ValueError("Price cannot be negative.")
        
        service = {
            'name': name,
            'description': description,
            'price': price
        }
        self.services.append(service)
        logging.info(f"Service added: {service}")

    def remove_service(self, name: str) -> None:
        """
        Remove a service from the handyman service list by name.

        :param name: The name of the service to remove.
        """
        for service in self.services:
            if service['name'] == name:
                self.services.remove(service)
                logging.info(f"Service removed: {service}")
                return
        logging.warning(f"Service '{name}' not found.")

    def list_services(self) -> List[Dict[str, Any]]:
        """
        List all available services.

        :return: A list of services.
        """
        logging.info("Listing all services.")
        return self.services

    def save_services(self, filename: str) -> None:
        """
        Save the services to a JSON file.

        :param filename: The name of the file to save the services.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.services, file, indent=4)
            logging.info(f"Services saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save services to {filename}: {e}")

    def load_services(self, filename: str) -> None:
        """
        Load services from a JSON file.

        :param filename: The name of the file to load the services from.
        """
        try:
            with open(filename, 'r') as file:
                self.services = json.load(file)
            logging.info(f"Services loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load services from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    handyman_service = HandymanService()
    
    # Adding services
    handyman_service.add_service("Osmosis Inversa Installation", "Installation of osmosis inversa systems.", 150.0)
    handyman_service.add_service("Electrodomestic Repair", "Repair of household appliances.", 75.0)
    handyman_service.add_service("Fontanería Maintenance", "General plumbing maintenance and repairs.", 100.0)

    # Listing services
    services = handyman_service.list_services()
    print("Available Services:", services)

    # Saving services to a file
    handyman_service.save_services("services.json")

    # Loading services from a file
    handyman_service.load_services("services.json")
```
