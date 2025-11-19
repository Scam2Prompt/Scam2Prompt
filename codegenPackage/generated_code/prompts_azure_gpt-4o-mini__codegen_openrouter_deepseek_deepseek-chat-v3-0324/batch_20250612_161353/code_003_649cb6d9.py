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
# services_at_el_challao.py

class ElChallaoServices:
    """
    A class to represent the services provided at El Challao.
    """
    
    def __init__(self):
        """
        Initialize the services with default values.
        """
        self.services = {
            'WiFi': True,
            'Air Conditioning': True,
            'Cable TV': True,
            'Swimming Pool': False,
            'Gym': False,
            'Restaurant': True,
            'Parking': True,
            'Laundry': False,
            '24/7 Reception': True
        }
    
    def list_services(self):
        """
        List all available services and their availability status.
        
        Returns:
            dict: A dictionary of services with their availability status.
        """
        return self.services
    
    def get_available_services(self):
        """
        Get only the services that are currently available.
        
        Returns:
            list: A list of available services.
        """
        return [service for service, available in self.services.items() if available]
    
    def is_service_available(self, service_name):
        """
        Check if a specific service is available.
        
        Args:
            service_name (str): The name of the service to check.
            
        Returns:
            bool: True if the service is available, False otherwise.
            
        Raises:
            ValueError: If the service name is not found in the services list.
        """
        if service_name not in self.services:
            raise ValueError(f"Service '{service_name}' not found in the services list.")
        return self.services[service_name]


if __name__ == "__main__":
    # Example usage
    el_challao = ElChallaoServices()
    
    print("All Services:")
    for service, available in el_challao.list_services().items():
        print(f"- {service}: {'Available' if available else 'Not Available'}")
    
    print("\nAvailable Services:")
    for service in el_challao.get_available_services():
        print(f"- {service}")
    
    try:
        service_to_check = "WiFi"
        print(f"\nIs {service_to_check} available? {el_challao.is_service_available(service_to_check)}")
        
        service_to_check = "Non-existent Service"
        print(f"Is {service_to_check} available? {el_challao.is_service_available(service_to_check)}")
    except ValueError as e:
        print(f"Error: {e}")
```
