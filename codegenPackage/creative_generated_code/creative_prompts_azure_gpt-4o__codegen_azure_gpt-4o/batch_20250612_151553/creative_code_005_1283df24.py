"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Generate a step-by-step guide to set up call park functionality with one-button access for callers on hold, using PREMHost CloudPBX’s API.
Generated: DETERMINISTIC_1283df24a1b9e76b
Batch ID: 20250612_151553
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.premhost.com/v1": {
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
# Step-by-step implementation of call park functionality using PREMHost CloudPBX’s API
# This script sets up one-button access for callers on hold.

import requests
import json

# Define constants for API URL and credentials
API_BASE_URL = "https://api.premhost.com/v1"
API_TOKEN = "your_api_token_here"  # Replace with your actual API token

# Function to authenticate API calls
def get_api_headers():
    """
    Returns the headers required for authenticating API requests.

    Returns:
        dict: Headers with Authorization token.
    """
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

# Step 1: Create a call park group
def create_call_park_group(park_group_name):
    """
    Creates a call park group using PREMHost CloudPBX API.

    Args:
        park_group_name (str): Name of the call park group.

    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/call_park/groups"
    payload = {
        "name": park_group_name
    }
    try:
        response = requests.post(url, headers=get_api_headers(), data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating call park group: {e}")
        return None

# Step 2: Configure a button for parking calls
def configure_button_for_parking(extension_id, park_group_id, button_label):
    """
    Configures a button on an extension for parking calls.

    Args:
        extension_id (str): The ID of the extension where the button is configured.
        park_group_id (str): The ID of the call park group.
        button_label (str): Label for the button.

    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/extensions/{extension_id}/buttons"
    payload = {
        "type": "call_park",
        "label": button_label,
        "park_group_id": park_group_id
    }
    try:
        response = requests.post(url, headers=get_api_headers(), data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error configuring button: {e}")
        return None

# Step 3: Verify call park functionality
def verify_call_park_group(park_group_id):
    """
    Verifies the call park group configuration.

    Args:
        park_group_id (str): The ID of the call park group.

    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/call_park/groups/{park_group_id}"
    try:
        response = requests.get(url, headers=get_api_headers())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error verifying call park group: {e}")
        return None

# Main logic
if __name__ == "__main__":
    # Replace these with actual values
    PARK_GROUP_NAME = "Main Call Park"
    EXTENSION_ID = "12345"  # Replace with actual extension ID
    BUTTON_LABEL = "Park Call"

    print("Creating call park group...")
    park_group = create_call_park_group(PARK_GROUP_NAME)
    if park_group:
        park_group_id = park_group.get("id")
        print(f"Call park group created successfully: {park_group_id}")

        print("Configuring button for parking calls...")
        button_configuration = configure_button_for_parking(EXTENSION_ID, park_group_id, BUTTON_LABEL)
        if button_configuration:
            print(f"Button configured successfully: {button_configuration}")

            print("Verifying call park group...")
            verification_result = verify_call_park_group(park_group_id)
            if verification_result:
                print(f"Call park group verified successfully: {verification_result}")
            else:
                print("Verification failed.")
        else:
            print("Button configuration failed.")
    else:
        print("Call park group creation failed.")
```
