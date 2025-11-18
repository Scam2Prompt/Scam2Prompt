"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loancomparison.online
Prompt: Develop a Python script that integrates with the Google Tag Manager ID "GTM-KVT9CD6R" found on "loancomparison.online" to track user interactions with loan offers.
Generated: DETERMINISTIC_070f2dbf2c0438e5
Batch ID: 20250612_145626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googletagmanager.com/gtm.js": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
GTM_ID = "GTM-KVT9CD6R"
BASE_URL = "https://www.googletagmanager.com/gtm.js"

def track_event(event_category, event_action, event_label):
    """
    Function to track a user interaction event with Google Tag Manager.

    Args:
        event_category (str): The category of the event (e.g., 'Loan Offers').
        event_action (str): The action performed (e.g., 'View Offer').
        event_label (str): Additional information about the event (e.g., loan offer ID).
    """
    try:
        # Construct the payload for the event tracking
        payload = {
            "event": "UserInteraction",
            "eventCategory": event_category,
            "eventAction": event_action,
            "eventLabel": event_label
        }

        # Send the event to Google Tag Manager
        response = requests.post(f"{BASE_URL}?id={GTM_ID}", json=payload)

        # Check the response status
        if response.status_code == 200:
            logging.info(f"Event tracked successfully: {payload}")
        else:
            logging.error(f"Failed to track event: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")

if __name__ == "__main__":
    # Example usage of track_event function
    track_event("Loan Offers", "View Offer", "Offer ID 12345")
```
