"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subscribemenow.com
Prompt: Create a script to automate SMS marketing campaigns using GetResponse's API, including scheduling and advanced segmentation.
Generated: DETERMINISTIC_d560cf6a5eede743
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.getresponse.com/v3": {
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
"""
SMS Marketing Automation Script using GetResponse API

This script automates SMS marketing campaigns using GetResponse's API. It includes:
1. Advanced segmentation of contact lists.
2. Campaign scheduling.
3. Error handling and logging.

Author: [Your Name]
Date: [YYYY-MM-DD]
"""

import requests
import logging
from datetime import datetime, timedelta

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("sms_campaign.log"),  # Logs to file
        logging.StreamHandler()  # Logs to console
    ]
)

# Constants and Configuration
API_BASE_URL = "https://api.getresponse.com/v3"
API_KEY = "your_api_key_here"  # Replace with your GetResponse API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Helper Functions
def fetch_contact_list(segment_id):
    """
    Fetches contacts based on the given segment ID.
    :param segment_id: ID of the segment to fetch contacts from.
    :return: List of contacts in the segment.
    """
    try:
        endpoint = f"{API_BASE_URL}/contacts?query[segmentId]={segment_id}"
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()
        contacts = response.json()
        logging.info(f"Fetched {len(contacts)} contacts from segment {segment_id}.")
        return contacts
    except requests.RequestException as e:
        logging.error(f"Failed to fetch contact list: {e}")
        return []

def schedule_sms_campaign(campaign_name, send_time, message, recipient_ids):
    """
    Schedules an SMS campaign.
    :param campaign_name: Name of the campaign.
    :param send_time: Datetime when the campaign should start.
    :param message: SMS message content.
    :param recipient_ids: List of recipient IDs.
    :return: None
    """
    try:
        endpoint = f"{API_BASE_URL}/campaigns"
        payload = {
            "name": campaign_name,
            "send_date": send_time.isoformat(),  # Convert datetime to ISO format
            "content": {"text": message},
            "recipients": {"contactIds": recipient_ids}
        }
        response = requests.post(endpoint, headers=HEADERS, json=payload)
        response.raise_for_status()
        logging.info(f"Campaign '{campaign_name}' scheduled successfully.")
    except requests.RequestException as e:
        logging.error(f"Failed to schedule SMS campaign: {e}")

def get_segment_id(segment_name):
    """
    Fetches the ID of a segment based on its name.
    :param segment_name: Name of the segment.
    :return: Segment ID.
    """
    try:
        endpoint = f"{API_BASE_URL}/segments"
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()
        segments = response.json()
        for segment in segments:
            if segment["name"] == segment_name:
                logging.info(f"Segment '{segment_name}' found with ID: {segment['id']}.")
                return segment["id"]
        logging.warning(f"Segment '{segment_name}' not found.")
        return None
    except requests.RequestException as e:
        logging.error(f"Failed to fetch segments: {e}")
        return None

# Main Function
def main():
    """
    Main function to run the SMS marketing automation script.
    Includes segment fetching, contact retrieval, and campaign scheduling.
    """
    try:
        # Define campaign parameters
        segment_name = "Premium Customers"
        campaign_name = "Flash Sale Campaign"
        message_content = "Don't miss out on our exclusive flash sale! Shop now!"
        send_time = datetime.now() + timedelta(days=1)  # Schedule 1 day ahead

        # Fetch segment ID
        segment_id = get_segment_id(segment_name)
        if not segment_id:
            logging.error(f"Segment '{segment_name}' could not be processed. Exiting.")
            return

        # Retrieve contacts in the segment
        contacts = fetch_contact_list(segment_id)
        if not contacts:
            logging.error("No contacts found. Exiting.")
            return

        # Extract recipient IDs from contacts
        recipient_ids = [contact["id"] for contact in contacts]
        logging.info(f"Extracted {len(recipient_ids)} recipient IDs.")

        # Schedule SMS campaign
        schedule_sms_campaign(campaign_name, send_time, message_content, recipient_ids)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
```
