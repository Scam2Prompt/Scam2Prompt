"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Create a Python function that uses the Source-Connect API to establish a live connection for remote voice recording, referencing Eric Navarro's setup details.
Generated: DETERMINISTIC_91b9830ffc5de860
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.source-connect.com/v1": {
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

class SourceConnectAPIError(Exception):
    """Custom exception for errors related to the Source-Connect API."""
    pass

def establish_live_connection(api_url, auth_token, connection_details):
    """
    Establishes a live connection for remote voice recording using the Source-Connect API.

    Parameters:
    api_url (str): The base URL for the Source-Connect API.
    auth_token (str): The authentication token for accessing the API.
    connection_details (dict): A dictionary containing connection parameters.

    Returns:
    dict: The response from the API if the connection is successful.

    Raises:
    SourceConnectAPIError: If there is an error with the API request or response.
    """

    # Set the headers for the API request
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    # Attempt to make the API call to establish the connection
    try:
        response = requests.post(f"{api_url}/connections", headers=headers, data=json.dumps(connection_details))
        
        # Check if the response indicates a successful connection
        if response.status_code != 200:
            raise SourceConnectAPIError(f"Failed to establish connection: {response.text}")

        # Parse the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        raise SourceConnectAPIError(f"Request error: {str(e)}")
    except json.JSONDecodeError:
        # Handle JSON decoding errors
        raise SourceConnectAPIError("Failed to decode JSON response from the API.")

# Example usage (ensure to replace with actual API URL and auth token)
if __name__ == "__main__":
    API_URL = "https://api.source-connect.com/v1"
    AUTH_TOKEN = "your_auth_token"
    CONNECTION_DETAILS = {
        "audio_format": "WAV",
        "sample_rate": 44100,
        "channels": 2,
        "bit_rate": 16
    }

    try:
        connection_response = establish_live_connection(API_URL, AUTH_TOKEN, CONNECTION_DETAILS)
        print("Connection established successfully:", connection_response)
    except SourceConnectAPIError as e:
        print("Error:", e)
```
