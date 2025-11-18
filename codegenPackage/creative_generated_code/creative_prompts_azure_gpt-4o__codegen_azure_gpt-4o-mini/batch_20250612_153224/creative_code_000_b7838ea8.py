"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Write a Python script to automate the process of requesting quotations from suppliers listed on PRGMEA's platform. Include fields for supplier name, product category, and contact information.
Generated: DETERMINISTIC_b7838ea8ed56695f
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.prgmea.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class QuotationRequester:
    """
    A class to automate the process of requesting quotations from suppliers on PRGMEA's platform.
    """

    def __init__(self, base_url):
        """
        Initializes the QuotationRequester with the base URL of the PRGMEA platform.
        
        :param base_url: str - The base URL of the PRGMEA platform's API
        """
        self.base_url = base_url

    def request_quotation(self, supplier_name, product_category, contact_info):
        """
        Sends a quotation request to the specified supplier.
        
        :param supplier_name: str - The name of the supplier
        :param product_category: str - The product category for the quotation
        :param contact_info: dict - Contact information of the requester
        :return: Response from the API call
        """
        # Prepare the request payload
        payload = {
            "supplier_name": supplier_name,
            "product_category": product_category,
            "contact_info": contact_info
        }

        # Send the POST request to the API
        try:
            response = requests.post(f"{self.base_url}/request-quotation", json=payload)
            # Raise an exception for HTTP errors
            response.raise_for_status()
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while requesting quotation: {e}")
            return None  # Return None if the request fails

def main():
    """
    Main function to execute the quotation request process.
    """
    # Base URL of the PRGMEA platform
    base_url = "https://api.prgmea.com"

    # Initialize the QuotationRequester
    requester = QuotationRequester(base_url)

    # Gather input data from the user
    supplier_name = input("Enter the supplier name: ")
    product_category = input("Enter the product category: ")
    contact_info = {
        "name": input("Enter your name: "),
        "email": input("Enter your email: "),
        "phone": input("Enter your phone number: ")
    }

    # Request the quotation
    response = requester.request_quotation(supplier_name, product_category, contact_info)

    # Check if the response is successful
    if response:
        print("Quotation requested successfully!")
        print("Response:", response)
    else:
        print("Failed to request quotation.")

if __name__ == "__main__":
    main()
```
