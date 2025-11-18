"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Generate Python code to evaluate facility maintenance tasks such as wastewater treatment plant operation and asbestos abatement, referencing iSi Environmental’s facility support services.
Generated: DETERMINISTIC_34a5107755622718
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class FacilitySupportService:
    """
    A class to evaluate facility maintenance tasks such as wastewater treatment plant operation 
    and asbestos abatement, referencing iSi Environmental’s facility support services.
    """

    def __init__(self):
        """
        Initialize the facility service evaluation system.
        """
        self.services = {
            "Wastewater Treatment Plant Operation": {
                "description": "Manage wastewater treatment processes to ensure compliance with environmental regulations.",
                "complexity": "High",
                "priority": "Critical"
            },
            "Asbestos Abatement": {
                "description": "Safely handle and remove asbestos materials to meet safety and legal requirements.",
                "complexity": "Medium",
                "priority": "High"
            }
        }
    
    def list_services(self) -> List[str]:
        """
        List all available facility maintenance services.
        
        Returns:
            List[str]: A list of service names.
        """
        return list(self.services.keys())
    
    def evaluate_service(self, service_name: str) -> Dict[str, str]:
        """
        Evaluate the details of a specific facility maintenance service.
        
        Args:
            service_name (str): The name of the service to evaluate.
        
        Returns:
            Dict[str, str]: A dictionary containing details about the service.
        
        Raises:
            ValueError: If the service name is not found.
        """
        if service_name not in self.services:
            logging.error(f"Service '{service_name}' not found.")
            raise ValueError(f"Service '{service_name}' is not available in the system.")
        
        logging.info(f"Evaluating service: {service_name}")
        return self.services[service_name]
    
    def add_service(self, service_name: str, description: str, complexity: str, priority: str):
        """
        Add a new service to the system.

        Args:
            service_name (str): Name of the service.
            description (str): Description of the service.
            complexity (str): Complexity level of the service (e.g., Low, Medium, High).
            priority (str): Priority level of the service (e.g., Low, Medium, High, Critical).
        
        Raises:
            ValueError: If the service already exists.
        """
        if service_name in self.services:
            logging.error(f"Service '{service_name}' already exists.")
            raise ValueError(f"Service '{service_name}' already exists in the system.")
        
        self.services[service_name] = {
            "description": description,
            "complexity": complexity,
            "priority": priority
        }
        logging.info(f"Added new service: {service_name}")

# Example usage
if __name__ == "__main__":
    try:
        facility_service = FacilitySupportService()
        
        # List all services
        logging.info("Available Services:")
        for service in facility_service.list_services():
            logging.info(service)
        
        # Evaluate a specific service
        service_name = "Wastewater Treatment Plant Operation"
        details = facility_service.evaluate_service(service_name)
        logging.info(f"Details for '{service_name}': {details}")
        
        # Add a new service
        facility_service.add_service(
            service_name="Hazardous Waste Disposal",
            description="Safely dispose of hazardous materials in compliance with regulations.",
            complexity="High",
            priority="Critical"
        )
        
        # List services after adding a new one
        logging.info("Updated Services List:")
        for service in facility_service.list_services():
            logging.info(service)
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
