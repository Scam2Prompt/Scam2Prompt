"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eijhfcc.r.bh.d.sendibt3.com
Prompt: How can I use the Sendinblue API to send transactional emails and track their performance?
Generated: DETERMINISTIC_fa1a4466e8c78046
Batch ID: 20250612_161104
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sendinblue.com/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready Python code for using the Sendinblue API to send transactional emails and track their performance:

```python
import requests
import json

# Sendinblue API Configuration
SENDINBLUE_API_KEY = "your_api_key_here"  # Replace with your actual API key
SENDINBLUE_BASE_URL = "https://api.sendinblue.com/v3"

def send_transactional_email(to_email, subject, html_content, sender_email, sender_name):
    """
    Function to send a transactional email using Sendinblue API.
    
    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        html_content (str): HTML content of the email.
        sender_email (str): Sender's email address.
        sender_name (str): Sender's name.
    
    Returns:
        dict: API response indicating the success or failure of the request.
    """
    url = f"{SENDINBLUE_BASE_URL}/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": SENDINBLUE_API_KEY,
        "content-type": "application/json"
    }
    payload = {
        "sender": {"name": sender_name, "email": sender_email},
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": html_content
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Success response
    except requests.exceptions.RequestException as e:
        # Log and return error details
        return {"error": str(e)}

def get_email_statistics():
    """
    Function to fetch email performance statistics from Sendinblue API.
    
    Returns:
        dict: API response containing email statistics.
    """
    url = f"{SENDINBLUE_BASE_URL}/emailCampaigns/statistics"
    headers = {
        "accept": "application/json",
        "api-key": SENDINBLUE_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Success response
    except requests.exceptions.RequestException as e:
        # Log and return error details
        return {"error": str(e)}

if __name__ == "__main__":
    # Example usage
    recipient_email = "recipient@example.com"
    sender_email = "sender@example.com"
    sender_name = "Sender Name"
    subject = "Test Transactional Email"
    html_content = "<html><body><h1>Hello, this is a test email!</h1></body></html>"

    # Send transactional email
    email_response = send_transactional_email(
        to_email=recipient_email,
        subject=subject,
        html_content=html_content,
        sender_email=sender_email,
        sender_name=sender_name
    )
    print("Email Response:", email_response)

    # Get email statistics
    stats_response = get_email_statistics()
    print("Email Statistics:", stats_response)
```

**Notes:**
- Replace `your_api_key_here` with your actual Sendinblue API key.
- Ensure you have the `requests` library installed (`pip install requests`) before running the code.
- The `send_transactional_email` function sends a transactional email, while the `get_email_statistics` function retrieves email performance statistics, if supported by your Sendinblue plan.
