"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Provide an example of how to configure call park functionality in a cloud-based phone system.
Generated: DETERMINISTIC_438ad5c993af3be8
Batch ID: 20250612_155150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudphonesystem.com/v1": {
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
Call Park Configuration Example in a Cloud-Based Phone System

This script demonstrates how to configure call parking functionality 
for a cloud-based phone system using a hypothetical API. The script 
assumes the use of a RESTful API provided by the phone system service 
provider.
"""

import requests
import json

# Base URL for the cloud phone system API
BASE_URL = "https://api.cloudphonesystem.com/v1"

# API Token for authentication (replace with a secure method of storing/retrieving keys)
API_TOKEN = "your_api_token_here"

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_call_park_group(group_name, extension_range):
    """
    Creates a call park group with the specified name and extension range.

    Args:
        group_name (str): The name of the call park group.
        extension_range (list): A list of extensions available for call parking (e.g., ["1001", "1002"]).

    Returns:
        dict: Response from the API.
    """
    # Endpoint to configure call park groups
    endpoint = f"{BASE_URL}/call-park-groups"

    # Payload with call park group configuration
    payload = {
        "name": group_name,
        "extensions": extension_range,
        "enabled": True  # Enable call parking for this group
    }

    try:
        # Send HTTP POST request to create the call park group
        response = requests.post(endpoint, headers=HEADERS, data=json.dumps(payload))

        # Check if the response is successful
        if response.status_code == 201:
            return response.json()  # Successfully created
        else:
            # Log error and return response
            print(f"Error creating call park group: {response.status_code} - {response.text}")
            return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(f"An exception occurred while creating the call park group: {e}")
        return {"error": str(e)}

def get_call_park_groups():
    """
    Retrieves the list of all call park groups.

    Returns:
        list: List of call park groups.
    """
    # Endpoint to fetch call park groups
    endpoint = f"{BASE_URL}/call-park-groups"

    try:
        # Send HTTP GET request to fetch call park groups
        response = requests.get(endpoint, headers=HEADERS)

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()  # Successfully retrieved
        else:
            # Log error and return response
            print(f"Error fetching call park groups: {response.status_code} - {response.text}")
            return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors
        print(f"An exception occurred while fetching call park groups: {e}")
        return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    # Configure a new call park group
    group_name = "Support Team Call Park"
    extension_range = ["1001", "1002", "1003"]

    print("Creating Call Park Group...")
    create_response = create_call_park_group(group_name, extension_range)
    print("Response:", create_response)

    print("\nFetching Call Park Groups...")
    groups = get_call_park_groups()
    print("Call Park Groups:", groups)
```

This code is designed to be easily adapted for a real-world cloud-based phone system API by replacing the placeholder `BASE_URL` and `API_TOKEN` values with valid ones.
