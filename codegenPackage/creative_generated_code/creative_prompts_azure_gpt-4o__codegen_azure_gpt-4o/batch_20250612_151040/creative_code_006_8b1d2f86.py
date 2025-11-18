"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ultranetgh.com
Prompt: Create a solution using Ultranet's SMS Management Platform to schedule and send enterprise SMS messages with delivery reports.
Generated: DETERMINISTIC_8b1d2f86bd8d807e
Batch ID: 20250612_151040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ultranet-sms.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is clean, efficient, and well-documented Python code to interact with Ultranet's SMS Management Platform. Ensure you have the necessary API key and access credentials for the platform.

```python
import requests
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ultranet API configuration
API_BASE_URL = "https://api.ultranet-sms.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to schedule an SMS
def schedule_sms(recipient_phone, message, schedule_time):
    """
    Schedule an SMS using Ultranet's SMS Management API.

    Parameters:
        recipient_phone (str): The recipient's phone number.
        message (str): The message content to send.
        schedule_time (str): The scheduled time in ISO 8601 format (YYYY-MM-DDTHH:mm:ss).

    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/sms/schedule"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "recipient": recipient_phone,
        "message": message,
        "schedule_time": schedule_time
    }

    try:
        # Send the request to schedule the SMS
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad HTTP response codes
        logging.info("SMS successfully scheduled.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error scheduling SMS: {e}")
        raise

# Function to fetch SMS delivery reports
def fetch_delivery_reports():
    """
    Fetch SMS delivery reports from Ultranet's SMS Management API.

    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/sms/reports"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        # Send the request to retrieve the delivery reports
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad HTTP response codes
        logging.info("Successfully fetched delivery reports.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching delivery reports: {e}")
        raise

# Example usage of the functions
if __name__ == "__main__":
    # Example: Schedule an SMS
    recipient = "+1234567890"  # Replace with the recipient's actual phone number
    message = "Hello! This is a scheduled message."
    scheduled_time = (datetime.now().isoformat())  # Schedule for the current time
    try:
        schedule_response = schedule_sms(recipient, message, scheduled_time)
        logging.info(f"Scheduled SMS Response: {schedule_response}")
    except Exception as e:
        logging.error(f"Failed to schedule SMS: {e}")

    # Example: Fetch delivery reports
    try:
        reports = fetch_delivery_reports()
        logging.info(f"Delivery Reports: {reports}")
    except Exception as e:
        logging.error(f"Failed to fetch delivery reports: {e}")
```

Note:
- Replace `API_BASE_URL` and `API_KEY` with the correct values provided by Ultranet's SMS Management Platform.
- Ensure the proper phone number format (`recipient`) is used based on Ultranet's requirements.
- Add more specific error handling as needed for your use case.
