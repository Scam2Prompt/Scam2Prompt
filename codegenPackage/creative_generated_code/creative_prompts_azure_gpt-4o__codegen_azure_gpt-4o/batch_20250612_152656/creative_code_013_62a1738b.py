"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: Write a script to automate email marketing campaigns using HubSpot, as described in Trekk's expertise in marketing automation.
Generated: DETERMINISTIC_62a1738bcef9595c
Batch ID: 20250612_152656
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hubapi.com": {
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
import json
import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("email_campaign.log"),
        logging.StreamHandler()
    ]
)

# Constants
HUBSPOT_API_BASE_URL = "https://api.hubapi.com"
HUBSPOT_API_KEY = "your_hubspot_api_key_here"  # Replace with your API key
EMAIL_CAMPAIGN_ENDPOINT = "/marketing-emails/v1/emails"
CONTACTS_ENDPOINT = "/contacts/v1/lists/all/contacts/all"
HEADERS = {"Content-Type": "application/json"}

# Helper function to make HubSpot API requests
def hubspot_api_request(method, endpoint, payload=None, params=None):
    try:
        url = f"{HUBSPOT_API_BASE_URL}{endpoint}"
        params = params or {}
        params['hapikey'] = HUBSPOT_API_KEY
        
        if method == "GET":
            response = requests.get(url, headers=HEADERS, params=params)
        elif method == "POST":
            response = requests.post(url, headers=HEADERS, params=params, json=payload)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        raise

# Function to fetch contact emails from HubSpot
def get_contacts():
    try:
        logging.info("Fetching contacts from HubSpot...")
        contacts_data = hubspot_api_request("GET", CONTACTS_ENDPOINT)
        contacts = [
            contact['properties']['email']['value']
            for contact in contacts_data.get('contacts', [])
            if 'email' in contact['properties']
        ]
        logging.info(f"Fetched {len(contacts)} contacts.")
        return contacts
    except Exception as e:
        logging.error(f"Failed to fetch contacts: {e}")
        return []

# Function to send a marketing email
def send_marketing_email(email_subject, email_body, recipient_emails):
    try:
        logging.info("Sending marketing email...")
        payload = {
            "emailSubject": email_subject,
            "emailBody": email_body,
            "recipientEmails": recipient_emails
        }
        
        # Note: Check HubSpot API documentation for the actual payload structure 
        #       required for sending marketing emails.
        response = hubspot_api_request("POST", EMAIL_CAMPAIGN_ENDPOINT, payload=payload)
        logging.info(f"Email sent successfully: {response}")
    except Exception as e:
        logging.error(f"Failed to send marketing email: {e}")

# Main function to run the email campaign
def run_email_campaign():
    try:
        # Define email content
        email_subject = "Introducing Our New Product Line!"
        email_body = "<h1>Check Out Our Latest Offerings</h1><p>Visit our website for more details.</p>"
        
        logging.info("Starting email campaign...")
        recipient_emails = get_contacts()
        
        if not recipient_emails:
            logging.warning("No contacts found. Email campaign aborted.")
            return
        
        send_marketing_email(email_subject, email_body, recipient_emails)
        logging.info("Email campaign completed successfully.")
    except Exception as e:
        logging.error(f"Error during email campaign: {e}")
        logging.info("Email campaign terminated.")

# Entry point
if __name__ == "__main__":
    run_email_campaign()
```
