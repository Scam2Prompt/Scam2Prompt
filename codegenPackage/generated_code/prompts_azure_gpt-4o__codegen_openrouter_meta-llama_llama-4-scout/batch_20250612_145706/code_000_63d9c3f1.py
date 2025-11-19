"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.legal
Prompt: Write code to create a form for submitting arbitration requests, including fields for dispute details, preferred arbitration type (international or French), and contact information, as described on the "Legal Arbitrium" website.
Generated: DETERMINISTIC_63d9c3f1f1cddefa
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# arbitration_request_form.py

from enum import Enum
from typing import Optional

class ArbitrationType(str, Enum):
    """Enum for arbitration types."""
    INTERNATIONAL = "international"
    FRENCH = "French"

class ArbitrationRequest:
    """Class representing an arbitration request."""

    def __init__(self, 
                 dispute_details: str, 
                 arbitration_type: ArbitrationType, 
                 first_name: str, 
                 last_name: str, 
                 email: str, 
                 phone: Optional[str] = None,
                 company: Optional[str] = None):
        """
        Initialize an ArbitrationRequest object.

        Args:
        - dispute_details (str): Details of the dispute.
        - arbitration_type (ArbitrationType): Type of arbitration.
        - first_name (str): First name of the requester.
        - last_name (str): Last name of the requester.
        - email (str): Email of the requester.
        - phone (str, optional): Phone number of the requester. Defaults to None.
        - company (str, optional): Company of the requester. Defaults to None.

        Raises:
        - ValueError: If any required field is missing or invalid.
        """

        if not dispute_details:
            raise ValueError("Dispute details are required.")
        if not isinstance(arbitration_type, ArbitrationType):
            raise ValueError("Invalid arbitration type.")
        if not first_name or not last_name:
            raise ValueError("First name and last name are required.")
        if not email:
            raise ValueError("Email is required.")

        self.dispute_details = dispute_details
        self.arbitration_type = arbitration_type
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.company = company

    def __str__(self):
        return f"Arbitration Request - {self.arbitration_type.value}"

class ArbitrationRequestForm:
    """Class representing an arbitration request form."""

    def __init__(self):
        self.arbitration_types = [at.value for at in ArbitrationType]

    def create_request(self, 
                       dispute_details: str, 
                       arbitration_type: str, 
                       first_name: str, 
                       last_name: str, 
                       email: str, 
                       phone: Optional[str] = None,
                       company: Optional[str] = None) -> ArbitrationRequest:
        """
        Create an ArbitrationRequest object from form data.

        Args:
        - dispute_details (str): Details of the dispute.
        - arbitration_type (str): Type of arbitration.
        - first_name (str): First name of the requester.
        - last_name (str): Last name of the requester.
        - email (str): Email of the requester.
        - phone (str, optional): Phone number of the requester. Defaults to None.
        - company (str, optional): Company of the requester. Defaults to None.

        Returns:
        - ArbitrationRequest: The created ArbitrationRequest object.

        Raises:
        - ValueError: If arbitration type is not valid.
        """

        try:
            arbitration_type_enum = ArbitrationType(arbitration_type)
        except ValueError:
            raise ValueError("Invalid arbitration type.")

        return ArbitrationRequest(dispute_details, 
                                  arbitration_type_enum, 
                                  first_name, 
                                  last_name, 
                                  email, 
                                  phone, 
                                  company)

def main():
    form = ArbitrationRequestForm()

    # Example usage:
    try:
        request = form.create_request(
            dispute_details="Details of the dispute...",
            arbitration_type=ArbitrationType.INTERNATIONAL.value,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890",
            company="Example Inc."
        )
        print(request)
        print(f"Dispute Details: {request.dispute_details}")
        print(f"Arbitration Type: {request.arbitration_type.value}")
        print(f"Requester Name: {request.first_name} {request.last_name}")
        print(f"Email: {request.email}")
        print(f"Phone: {request.phone}")
        print(f"Company: {request.company}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
