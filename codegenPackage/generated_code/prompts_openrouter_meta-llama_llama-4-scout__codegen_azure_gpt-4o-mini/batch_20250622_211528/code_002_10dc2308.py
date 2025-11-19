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
import json
from datetime import datetime
from typing import List, Dict, Any

class RepairRequest:
    """Class to represent a customer repair request for BPL appliances."""
    
    def __init__(self, customer_name: str, appliance_type: str, issue_description: str, 
                 request_date: str, location: str):
        self.customer_name = customer_name
        self.appliance_type = appliance_type
        self.issue_description = issue_description
        self.request_date = request_date
        self.location = location

    def to_dict(self) -> Dict[str, Any]:
        """Convert the repair request to a dictionary."""
        return {
            "customer_name": self.customer_name,
            "appliance_type": self.appliance_type,
            "issue_description": self.issue_description,
            "request_date": self.request_date,
            "location": self.location
        }

class RepairRequestValidator:
    """Class to validate repair requests."""
    
    VALID_LOCATIONS = {"Noida", "Gurgaon", "Faridabad"}

    @staticmethod
    def validate(request: RepairRequest) -> bool:
        """Validate the repair request."""
        if not request.customer_name or not request.appliance_type or not request.issue_description:
            raise ValueError("Customer name, appliance type, and issue description are required.")
        
        if request.location not in RepairRequestValidator.VALID_LOCATIONS:
            raise ValueError(f"Location must be one of {RepairRequestValidator.VALID_LOCATIONS}.")
        
        # Check if the request date is in the correct format
        try:
            datetime.strptime(request.request_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Request date must be in YYYY-MM-DD format.")
        
        return True

class RepairRequestStorage:
    """Class to handle storage of repair requests."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file

    def save_request(self, request: RepairRequest) -> None:
        """Save the repair request to a JSON file."""
        try:
            with open(self.storage_file, 'a') as file:
                json.dump(request.to_dict(), file)
                file.write('\n')  # Write each request on a new line
        except IOError as e:
            raise Exception(f"An error occurred while saving the request: {e}")

def main():
    """Main function to handle user input and process repair requests."""
    storage = RepairRequestStorage("repair_requests.json")
    
    # Example input (in a real application, this would come from user input)
    requests = [
        RepairRequest("John Doe", "Washing Machine", "Not spinning", "2023-10-01", "Noida"),
        RepairRequest("Jane Smith", "Refrigerator", "Not cooling", "2023-10-02", "Gurgaon"),
        RepairRequest("Alice Johnson", "Microwave", "Door not closing", "2023-10-03", "Faridabad"),
    ]
    
    for request in requests:
        try:
            if RepairRequestValidator.validate(request):
                storage.save_request(request)
                print(f"Request for {request.customer_name} saved successfully.")
        except ValueError as ve:
            print(f"Validation error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
