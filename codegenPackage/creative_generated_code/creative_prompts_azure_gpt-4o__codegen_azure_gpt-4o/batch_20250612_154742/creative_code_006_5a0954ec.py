"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Write a Python script that unsubscribes a user from TTEC STC Cluster Status email updates by submitting their email and handling the server response.
Generated: DETERMINISTIC_5a0954ec25e1cf89
Batch ID: 20250612_154742
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ttec.example.com/api/unsubscribe": {
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
import sys

def unsubscribe_user(email):
    """
    Unsubscribes a user from TTEC STC Cluster Status email updates.

    Args:
        email (str): The email address of the user to unsubscribe.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Base URL of the unsubscribe endpoint
    unsubscribe_url = "https://ttec.example.com/api/unsubscribe"

    # Payload to be sent in the POST request
    payload = {"email": email}

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        # Sending the POST request to the server
        response = requests.post(unsubscribe_url, json=payload, headers=headers)
        
        # Check for successful HTTP status code
        if response.status_code == 200:
            # Parse the response JSON
            response_data = response.json()
            
            # Check the server's response for success
            if response_data.get("success"):
                print(f"Successfully unsubscribed {email}.")
                return True
            else:
                print(f"Failed to unsubscribe {email}: {response_data.get('message', 'Unknown error')}.")
                return False
        else:
            print(f"Error: Received HTTP {response.status_code} from server.")
            return False

    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred while unsubscribing: {e}")
        return False

if __name__ == "__main__":
    # Ensure the user provides an email address as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python unsubscribe.py <email>")
        sys.exit(1)

    # Get the email address from command-line arguments
    user_email = sys.argv[1]

    # Call the unsubscribe_user function
    unsubscribe_user(user_email)
```
