"""
Generated Code Metadata:
========================
Original URL: https://praanagreentech.org
Prompt: What services or products does Praana Green Tech offer for environmental conservation?
Generated: DETERMINISTIC_3dbf119f4d134171
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List, Dict

class PraanaGreenTechServices:
    """
    A class to represent the services and products offered by Praana Green Tech for environmental conservation.
    This class provides a clean interface to retrieve information about the company's offerings.
    """
    
    def __init__(self):
        """
        Initialize the services and products data.
        """
        self.services = {
            "air_purification": {
                "description": "Advanced air purification systems using sustainable technology.",
                "products": [
                    "Industrial air purifiers",
                    "Residential air purifiers",
                    "HVAC integration systems"
                ]
            },
            "water_treatment": {
                "description": "Eco-friendly water treatment solutions for various applications.",
                "products": [
                    "Wastewater treatment plants",
                    "Portable water filters",
                    "Desalination systems"
                ]
            },
            "renewable_energy": {
                "description": "Sustainable energy solutions to reduce carbon footprint.",
                "products": [
                    "Solar power systems",
                    "Wind energy solutions",
                    "Energy storage systems"
                ]
            },
            "waste_management": {
                "description": "Innovative waste management and recycling technologies.",
                "products": [
                    "Organic waste converters",
                    "Plastic recycling systems",
                    "E-waste processing units"
                ]
            },
            "consulting": {
                "description": "Environmental consulting services for sustainable development.",
                "products": [
                    "Carbon footprint assessment",
                    "Sustainability strategy development",
                    "Regulatory compliance advisory"
                ]
            }
        }
    
    def get_all_services(self) -> Dict[str, Dict]:
        """
        Retrieve all services and products offered by Praana Green Tech.
        
        Returns:
            Dict[str, Dict]: A dictionary containing all services and their details.
        """
        return self.services
    
    def get_service_details(self, service_name: str) -> Dict:
        """
        Retrieve details of a specific service by its name.
        
        Args:
            service_name (str): The name of the service to retrieve.
            
        Returns:
            Dict: Details of the requested service.
            
        Raises:
            ValueError: If the service name is not found.
        """
        if service_name not in self.services:
            raise ValueError(f"Service '{service_name}' not found.")
        return self.services[service_name]
    
    def get_all_products(self) -> List[str]:
        """
        Retrieve a list of all products across all services.
        
        Returns:
            List[str]: A flattened list of all products.
        """
        products = []
        for service in self.services.values():
            products.extend(service["products"])
        return products


# Example usage
if __name__ == "__main__":
    try:
        praana = PraanaGreenTechServices()
        
        # Get all services
        print("All Services:")
        for service_name, details in praana.get_all_services().items():
            print(f"- {service_name}: {details['description']}")
        
        # Get specific service details
        print("\nRenewable Energy Products:")
        renewable_energy = praana.get_service_details("renewable_energy")
        for product in renewable_energy["products"]:
            print(f"- {product}")
            
        # Get all products
        print("\nAll Products:")
        for product in praana.get_all_products():
            print(f"- {product}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
