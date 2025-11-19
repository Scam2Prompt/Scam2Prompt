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
import json
from typing import List, Dict

class MeterVerificationService:
    """
    Represents a meter verification service with its details.
    """
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the service details to a dictionary.
        """
        return {
            "name": self.name,
            "phone": self.phone
        }

class VerificationServiceGenerator:
    """
    Generates and manages a list of accredited meter verification services.
    """
    def __init__(self):
        self.services: List[MeterVerificationService] = []

    def add_service(self, name: str, phone: str) -> None:
        """
        Adds a new service to the list.
        
        Args:
            name: Name of the service provider.
            phone: Contact phone number.
        """
        if not name or not phone:
            raise ValueError("Name and phone number must be provided.")
        
        service = MeterVerificationService(name, phone)
        self.services.append(service)

    def get_services(self) -> List[Dict[str, str]]:
        """
        Returns the list of services as dictionaries.
        """
        return [service.to_dict() for service in self.services]

    def save_to_json(self, filename: str) -> None:
        """
        Saves the services to a JSON file.
        
        Args:
            filename: Name of the file to save to.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.get_services(), f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save to file: {e}")

def main():
    """
    Main function to demonstrate the usage of the VerificationServiceGenerator.
    """
    generator = VerificationServiceGenerator()
    
    # Add the example service
    generator.add_service("ИП Семьянинов Сергей Юрьевич", "22-22-10")
    
    # Add more services if needed
    # generator.add_service("Another Service", "33-33-33")
    
    # Print the services
    services = generator.get_services()
    print("Accredited Meter Verification Services in Tambov:")
    for service in services:
        print(f"Name: {service['name']}, Phone: {service['phone']}")
    
    # Save to JSON file
    try:
        generator.save_to_json("tambov_meter_services.json")
        print("Services saved to 'tambov_meter_services.json'")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
```
