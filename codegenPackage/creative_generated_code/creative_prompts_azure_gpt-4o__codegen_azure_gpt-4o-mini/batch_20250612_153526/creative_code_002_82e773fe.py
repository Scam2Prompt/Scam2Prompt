"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Create a program to extract contact information (address, phone number, email) from the AFEBI website and format it into a JSON object.
Generated: DETERMINISTIC_82e773fe8d7af77f
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.afebi.com/contact": {
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
from bs4 import BeautifulSoup
import json

def fetch_afebi_contact_info(url):
    """
    Fetches contact information from the AFEBI website.

    Parameters:
        url (str): The URL of the AFEBI website.

    Returns:
        dict: A dictionary containing the contact information, or an empty dictionary if an error occurs.
    """
    try:
        # Send a GET request to the AFEBI website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract contact information
        contact_info = {
            "address": None,
            "phone": None,
            "email": None
        }

        # Example selectors - adjust these according to the actual HTML structure of the AFEBI website
        address_element = soup.select_one(".address-class")  # Replace with actual class/ID
        phone_element = soup.select_one(".phone-class")      # Replace with actual class/ID
        email_element = soup.select_one(".email-class")      # Replace with actual class/ID

        # Populate the contact_info dictionary
        if address_element:
            contact_info["address"] = address_element.get_text(strip=True)
        if phone_element:
            contact_info["phone"] = phone_element.get_text(strip=True)
        if email_element:
            contact_info["email"] = email_element.get_text(strip=True)

        return contact_info

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {str(e)}")
        return {}

def main():
    # URL of the AFEBI website
    afebi_url = "https://www.afebi.com/contact"  # Replace with the actual contact URL

    # Fetch contact information
    contact_info = fetch_afebi_contact_info(afebi_url)

    # Format the contact information into a JSON object
    contact_info_json = json.dumps(contact_info, indent=4)

    # Print the JSON formatted contact information
    print(contact_info_json)

if __name__ == "__main__":
    main()
```
