"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Suggest tools or libraries for creating and managing proof-of-service documents for guardianship petitions, as outlined in the Serve Utah guide.
Generated: DETERMINISTIC_48ed9946aa1d3432
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# proof_of_service.py

import os
import json
from datetime import datetime

class ProofOfService:
    """A class to create and manage proof-of-service documents for guardianship petitions."""

    def __init__(self, service_details):
        """
        Initialize the ProofOfService instance.

        Args:
            service_details (dict): A dictionary containing details of the service.
        """
        self.service_details = service_details
        self.validate_service_details()

    def validate_service_details(self):
        """Validate the service details to ensure all required fields are present."""
        required_fields = ['petitioner', 'guardian', 'service_date', 'method', 'recipient']
        for field in required_fields:
            if field not in self.service_details:
                raise ValueError(f"Missing required field: {field}")

    def generate_document(self):
        """Generate a proof-of-service document in JSON format."""
        document = {
            "petitioner": self.service_details['petitioner'],
            "guardian": self.service_details['guardian'],
            "service_date": self.service_details['service_date'],
            "method": self.service_details['method'],
            "recipient": self.service_details['recipient'],
            "timestamp": datetime.now().isoformat()
        }
        return json.dumps(document, indent=4)

    def save_document(self, file_path):
        """Save the generated document to a specified file path.

        Args:
            file_path (str): The path where the document will be saved.
        """
        try:
            document = self.generate_document()
            with open(file_path, 'w') as file:
                file.write(document)
            print(f"Document saved successfully at {file_path}")
        except IOError as e:
            print(f"Error saving document: {e}")

# Example usage
if __name__ == "__main__":
    service_details = {
        "petitioner": "John Doe",
        "guardian": "Jane Smith",
        "service_date": "2023-10-01",
        "method": "Certified Mail",
        "recipient": "Tom Johnson"
    }

    try:
        proof_of_service = ProofOfService(service_details)
        proof_of_service.save_document(os.path.join(os.getcwd(), 'proof_of_service.json'))
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
