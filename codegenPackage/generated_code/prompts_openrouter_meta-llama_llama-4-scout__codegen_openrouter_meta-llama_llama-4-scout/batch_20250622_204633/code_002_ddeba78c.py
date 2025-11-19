"""
Generated Code Metadata:
========================
Original URL: https://freelistingaustralia.com
Prompt: Generate a sample JSON data structure for a business listing on FreeListingAustralia, including fields like business name, description, and contact information.
Generated: DETERMINISTIC_ddeba78c45dd7d14
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BusinessListing:
    def __init__(self, 
                 business_name: str, 
                 description: str, 
                 contact_name: str, 
                 contact_email: str, 
                 contact_phone: str, 
                 address: str, 
                 city: str, 
                 state: str, 
                 postcode: str, 
                 country: str = "Australia"):
        """
        Initialize a BusinessListing object.

        Args:
            business_name (str): The name of the business.
            description (str): A brief description of the business.
            contact_name (str): The name of the contact person.
            contact_email (str): The email address of the contact person.
            contact_phone (str): The phone number of the contact person.
            address (str): The street address of the business.
            city (str): The city where the business is located.
            state (str): The state where the business is located.
            postcode (str): The postcode of the business location.
            country (str, optional): The country where the business is located. Defaults to "Australia".
        """
        self.business_name = business_name
        self.description = description
        self.contact = {
            "name": contact_name,
            "email": contact_email,
            "phone": contact_phone
        }
        self.address = {
            "street": address,
            "city": city,
            "state": state,
            "postcode": postcode,
            "country": country
        }

    def to_json(self) -> str:
        """
        Convert the BusinessListing object to a JSON string.

        Returns:
            str: A JSON string representing the BusinessListing object.
        """
        try:
            business_listing = {
                "businessName": self.business_name,
                "description": self.description,
                "contact": self.contact,
                "address": self.address
            }
            return json.dumps(business_listing, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Example usage
if __name__ == "__main__":
    business_listing = BusinessListing(
        business_name="Sample Business",
        description="This is a sample business listing.",
        contact_name="John Doe",
        contact_email="john.doe@example.com",
        contact_phone="0412 345 678",
        address="123 Main St",
        city="Melbourne",
        state="VIC",
        postcode="3000"
    )

    json_data = business_listing.to_json()
    print(json_data)
```
