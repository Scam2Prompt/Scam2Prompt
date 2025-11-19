"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Generate code to validate and store customer repair requests for BPL appliances, specifically for out-of-warranty cases in Noida, Gurgaon, and Faridabad.
Generated: DETERMINISTIC_10dc23080e02a2f2
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_repair_request.py

import logging
from enum import Enum
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class City(Enum):
    """Enum for supported cities"""
    NOIDA = "Noida"
    GURGAON = "Gurgaon"
    FARIDABAD = "Faridabad"

class ApplianceStatus(Enum):
    """Enum for appliance status"""
    OUT_OF_WARRANTY = "Out of Warranty"

class RepairRequest:
    """Class to represent a customer repair request"""

    def __init__(self, customer_name: str, appliance_type: str, city: City, 
                 appliance_serial_number: str, issue_description: str):
        """
        Initialize a RepairRequest object.

        Args:
        - customer_name (str): Name of the customer
        - appliance_type (str): Type of BPL appliance
        - city (City): City where the customer is located
        - appliance_serial_number (str): Serial number of the appliance
        - issue_description (str): Description of the issue
        """
        self.customer_name = customer_name
        self.appliance_type = appliance_type
        self.city = city
        self.appliance_serial_number = appliance_serial_number
        self.issue_description = issue_description
        self.status = ApplianceStatus.OUT_OF_WARRANTY

    def __str__(self):
        return f"Customer Name: {self.customer_name}\nAppliance Type: {self.appliance_type}\nCity: {self.city.value}\n" \
               f"Appliance Serial Number: {self.appliance_serial_number}\nIssue Description: {self.issue_description}\n" \
               f"Status: {self.status.value}"

class RepairRequestValidator:
    """Class to validate customer repair requests"""

    def __init__(self):
        self.supported_cities = [city.value for city in City]

    def validate(self, request: RepairRequest) -> bool:
        """
        Validate a repair request.

        Args:
        - request (RepairRequest): The repair request to validate

        Returns:
        - bool: True if the request is valid, False otherwise
        """
        if not request.customer_name:
            logging.error("Customer name is required")
            return False
        if not request.appliance_type:
            logging.error("Appliance type is required")
            return False
        if request.city.value not in self.supported_cities:
            logging.error("Unsupported city")
            return False
        if not request.appliance_serial_number:
            logging.error("Appliance serial number is required")
            return False
        if not request.issue_description:
            logging.error("Issue description is required")
            return False

        return True

class RepairRequestStore:
    """Class to store customer repair requests"""

    def __init__(self):
        self.requests: Dict[str, RepairRequest] = {}

    def store(self, request: RepairRequest):
        """
        Store a repair request.

        Args:
        - request (RepairRequest): The repair request to store
        """
        request_id = len(self.requests) + 1
        self.requests[str(request_id)] = request
        logging.info(f"Repair request stored with ID: {request_id}")

def main():
    validator = RepairRequestValidator()
    store = RepairRequestStore()

    try:
        request = RepairRequest(
            customer_name="John Doe",
            appliance_type="BPL Refrigerator",
            city=City.NOIDA,
            appliance_serial_number="BPL12345",
            issue_description="Not cooling properly"
        )

        if validator.validate(request):
            store.store(request)
            print(request)
        else:
            logging.error("Invalid repair request")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
