"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: Write Python code to automate the segmentation of a database using ActiveCampaign, as described in Gisela Bravo's marketing automation services.
Generated: DETERMINISTIC_38007228b5184576
Batch ID: 20250612_154958
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://youraccount.api-us1.com/api/3": {
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

class ActiveCampaignSegmenter:
    """
    A class to interact with ActiveCampaign API for database segmentation.
    """
    
    def __init__(self, api_url: str, api_key: str):
        """
        Initialize the ActiveCampaignSegmenter instance.
        
        :param api_url: The base URL of the ActiveCampaign API (e.g., "https://youraccount.api-us1.com/api/3").
        :param api_key: Your ActiveCampaign API key.
        """
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_contacts(self):
        """
        Retrieve contacts from ActiveCampaign.
        
        :return: A list of contacts (each contact is represented as a dictionary).
        """
        try:
            endpoint = f"{self.api_url}/contacts"
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json().get("contacts", [])
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving contacts: {e}")
            return []

    def create_tag(self, tag_name: str):
        """
        Create a new tag in ActiveCampaign.
        
        :param tag_name: The name of the tag to create.
        :return: The ID of the newly created tag, or None if creation failed.
        """
        try:
            endpoint = f"{self.api_url}/tags"
            data = {
                "tag": {
                    "tag": tag_name,
                    "tagType": "contact"
                }
            }
            response = requests.post(endpoint, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()
            return response.json().get("tag", {}).get("id")
        except requests.exceptions.RequestException as e:
            print(f"Error creating tag: {e}")
            return None

    def assign_tag_to_contact(self, contact_id: int, tag_id: int):
        """
        Assign a tag to a contact in ActiveCampaign.
        
        :param contact_id: The ID of the contact.
        :param tag_id: The ID of the tag to assign.
        """
        try:
            endpoint = f"{self.api_url}/contactTags"
            data = {
                "contactTag": {
                    "contact": contact_id,
                    "tag": tag_id
                }
            }
            response = requests.post(endpoint, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error assigning tag to contact: {e}")

    def segment_contacts_by_criteria(self, criteria_function):
        """
        Segment contacts based on a custom criteria function.
        
        :param criteria_function: A function that takes a contact (dictionary) as input
                                  and returns True if the contact matches the segmentation criteria.
        """
        contacts = self.get_contacts()
        if not contacts:
            print("No contacts retrieved; segmentation aborted.")
            return

        tag_name = "Segmented"
        tag_id = self.create_tag(tag_name)
        if not tag_id:
            print("Failed to create tag; segmentation aborted.")
            return

        for contact in contacts:
            try:
                contact_id = contact.get("id")
                if contact_id and criteria_function(contact):
                    self.assign_tag_to_contact(contact_id, tag_id)
            except Exception as e:
                print(f"Error processing contact {contact.get('id')}: {e}")


# Example usage

def sample_criteria(contact):
    """
    Example criteria function to segment contacts.
    Segments contacts whose email address contains 'example.com'.
    
    :param contact: A dictionary representing a contact.
    :return: True if the contact matches the criteria, False otherwise.
    """
    email = contact.get("email", "")
    return "example.com" in email

if __name__ == "__main__":
    # Replace with your ActiveCampaign API credentials
    API_URL = "https://youraccount.api-us1.com/api/3"
    API_KEY = "your_api_key"

    segmenter = ActiveCampaignSegmenter(API_URL, API_KEY)
    segmenter.segment_contacts_by_criteria(sample_criteria)
```
