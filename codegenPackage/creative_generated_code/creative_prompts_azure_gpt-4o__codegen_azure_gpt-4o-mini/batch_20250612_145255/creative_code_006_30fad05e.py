"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Develop an automation workflow in ActiveCampaign to convert leads into loyal customers, using the methods outlined by Sales Studios.
Generated: DETERMINISTIC_30fad05e52503500
Batch ID: 20250612_145255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_account.api.activecampaign.com/api/3": {
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

class ActiveCampaignAPI:
    def __init__(self, api_url, api_key):
        """
        Initializes the ActiveCampaignAPI instance with the provided API URL and key.
        
        :param api_url: str - The URL for the ActiveCampaign API.
        :param api_key: str - The API key for authenticating requests.
        """
        self.api_url = api_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes an HTTP request to the ActiveCampaign API.
        
        :param endpoint: str - The endpoint for the API request.
        :param method: str - The HTTP method to use (GET, POST, etc.).
        :param data: dict - The data to send with the request, if applicable.
        :return: dict - The response from the API as a JSON object.
        """
        headers = {
            'Content-Type': 'application/json',
            'Api-Token': self.api_key
        }
        
        url = f"{self.api_url}/{endpoint}"
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            else:
                response = requests.post(url, headers=headers, data=json.dumps(data))

            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None

    def create_contact(self, email, first_name, last_name):
        """
        Creates a new contact in ActiveCampaign.
        
        :param email: str - The email address of the contact.
        :param first_name: str - The first name of the contact.
        :param last_name: str - The last name of the contact.
        :return: dict - The created contact's details or None on failure.
        """
        endpoint = "contacts"
        data = {
            "contact": {
                "email": email,
                "firstName": first_name,
                "lastName": last_name
            }
        }
        return self._make_request(endpoint, method='POST', data=data)

    def add_contact_to_list(self, contact_id, list_id):
        """
        Adds an existing contact to a specified list in ActiveCampaign.
        
        :param contact_id: int - The ID of the contact to add.
        :param list_id: int - The ID of the list to add the contact to.
        :return: dict - The response confirming the addition or None on failure.
        """
        endpoint = "contactLists"
        data = {
            "contactList": {
                "list": list_id,
                "contact": contact_id,
                "status": 1  # Status 1 means 'Subscribed'
            }
        }
        return self._make_request(endpoint, method='POST', data=data)

    def create_deal(self, contact_id, deal_name):
        """
        Creates a new deal associated with a contact.
        
        :param contact_id: int - The ID of the contact associated with the deal.
        :param deal_name: str - The name of the deal.
        :return: dict - The created deal's details or None on failure.
        """
        endpoint = "deals"
        data = {
            "deal": {
                "contact": contact_id,
                "title": deal_name,
                "value": 1000,  # Example value; adjust as needed
                "currency": "USD"
            }
        }
        return self._make_request(endpoint, method='POST', data=data)

def main():
    # Replace with your ActiveCampaign API credentials
    API_URL = "https://your_account.api.activecampaign.com/api/3"
    API_KEY = "your_api_key"

    # Initialize the ActiveCampaign API client
    ac_api = ActiveCampaignAPI(API_URL, API_KEY)

    # Example data for the workflow
    email = "lead@example.com"
    first_name = "John"
    last_name = "Doe"
    list_id = 1  # Replace with your specific list ID
    deal_name = "First Purchase"

    # Step 1: Create a new contact
    contact = ac_api.create_contact(email, first_name, last_name)
    if contact:
        contact_id = contact.get("contact", {}).get("id")
        print(f"Contact created with ID: {contact_id}")

        # Step 2: Add contact to list
        if ac_api.add_contact_to_list(contact_id, list_id):
            print(f"Contact {contact_id} added to list {list_id}.")

            # Step 3: Create a deal for the contact
            if ac_api.create_deal(contact_id, deal_name):
                print(f"Deal '{deal_name}' created for contact {contact_id}.")
            else:
                print("Failed to create deal.")
        else:
            print("Failed to add contact to list.")
    else:
        print("Failed to create contact.")

if __name__ == "__main__":
    main()
```
