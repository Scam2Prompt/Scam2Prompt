"""
Generated Code Metadata:
========================
Original URL: https://arbitrum24market.ru
Prompt: Write a Python script that automates the process of fetching and displaying contact information from a legal service API, inspired by the contact details on the Arbitrum site.
Generated: DETERMINISTIC_948de487a7fa6470
Batch ID: 20250612_164152
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.legalservice.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

# Constants
API_BASE_URL = "https://api.legalservice.com/v1"  # Replace with the actual API base URL
CONTACT_ENDPOINT = "/contacts"  # Endpoint for fetching contact information
TIMEOUT = 10  # Timeout for API requests in seconds

def fetch_contact_information():
    """
    Fetches contact information from the legal service API.

    Returns:
        list: A list of dictionaries containing contact information.
    """
    try:
        # Make a GET request to the contact endpoint
        response = requests.get(f"{API_BASE_URL}{CONTACT_ENDPOINT}", timeout=TIMEOUT)
        
        # Raise an HTTPError if the response status code indicates an error
        response.raise_for_status()
        
        # Parse the JSON response
        contact_data = response.json()
        
        # Validate the structure of the response
        if not isinstance(contact_data, list):
            raise ValueError("Unexpected response format: Expected a list of contacts.")
        
        return contact_data
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching contact information: {e}")
        return []
    except ValueError as ve:
        # Handle unexpected response format
        print(f"Error processing contact information: {ve}")
        return []

def display_contact_information(contacts):
    """
    Displays contact information in a user-friendly format.

    Args:
        contacts (list): A list of dictionaries containing contact information.
    """
    if not contacts:
        print("No contact information available.")
        return
    
    print("Contact Information:")
    print("-" * 50)
    for contact in contacts:
        # Extract and display relevant fields
        name = contact.get("name", "N/A")
        email = contact.get("email", "N/A")
        phone = contact.get("phone", "N/A")
        address = contact.get("address", "N/A")
        
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")
        print("-" * 50)

def main():
    """
    Main function to orchestrate the fetching and displaying of contact information.
    """
    print("Fetching contact information...")
    contacts = fetch_contact_information()
    display_contact_information(contacts)

if __name__ == "__main__":
    main()
```
