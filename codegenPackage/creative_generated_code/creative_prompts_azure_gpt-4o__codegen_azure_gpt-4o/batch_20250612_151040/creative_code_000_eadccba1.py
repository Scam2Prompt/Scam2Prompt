"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ultranetgh.com
Prompt: Write code using Ultranet's Configurable Messaging API to send SMS notifications with custom sender IDs and message templates.
Generated: DETERMINISTIC_eadccba1f7cab863
Batch ID: 20250612_151040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ultranet.com/v1/messages": {
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
# Import necessary libraries
import requests

# Define constants for the API
API_BASE_URL = "https://api.ultranet.com/v1/messages"
API_KEY = "your_api_key_here"  # Replace with your Ultranet API key

def send_sms(sender_id, recipient_number, message_template, template_params):
    """
    Sends an SMS message using Ultranet's Configurable Messaging API.

    Args:
        sender_id (str): The custom sender ID for the SMS.
        recipient_number (str): The recipient's phone number in E.164 format.
        message_template (str): The message template with placeholders.
        template_params (dict): A dictionary of placeholder values to fill the template.

    Returns:
        dict: The response from the API, including status and message ID.
    """
    try:
        # Format the message using the provided template and parameters
        message_content = message_template.format(**template_params)
        
        # Prepare the payload for the API request
        payload = {
            "sender_id": sender_id,
            "recipient": recipient_number,
            "message": message_content,
        }
        
        # Set headers for authentication
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }
        
        # Make the API call
        response = requests.post(API_BASE_URL, json=payload, headers=headers)
        
        # Raise an HTTP error if the response indicates a failure
        response.raise_for_status()
        
        # Parse and return the JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        # Handle API request exceptions
        return {"error": str(e), "status": "failure"}
    except KeyError as e:
        # Handle template formatting errors
        return {"error": f"Missing template parameter: {str(e)}", "status": "failure"}

# Example usage
if __name__ == "__main__":
    # Define sender ID, recipient number, and message template
    sender_id = "MyBusiness"
    recipient_number = "+1234567890"
    message_template = "Hello {name}, your order #{order_id} is on the way!"
    
    # Define template parameters
    template_params = {
        "name": "John",
        "order_id": "98765",
    }
    
    # Send the SMS
    response = send_sms(sender_id, recipient_number, message_template, template_params)
    
    # Print the response
    print(response)
```

Make sure to replace `your_api_key_here` with your actual Ultranet API key, and verify that the recipient's phone number and sender ID meet Ultranet's requirements.
