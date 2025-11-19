"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dfcloudpbx.com
Prompt: Generate a sample API call for managing voicemail transcripts through the PREMHost CloudPBX system.
Generated: DETERMINISTIC_991530ac61e6ef61
Batch ID: 20250612_155150
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
import requests

# Constants for the PREMHost CloudPBX API
API_BASE_URL = "https://api.premhost.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key
TIMEOUT = 15  # Timeout for the API request in seconds


def manage_voicemail_transcript(voicemail_id, action, transcript=None):
    """
    Function to manage voicemail transcripts in the PREMHost CloudPBX system.
    
    Parameters:
        voicemail_id (str): The ID of the voicemail to manage.
        action (str): Action to perform - "retrieve", "update", or "delete".
        transcript (str, optional): New transcript content for updating. Required for "update" action.
    
    Returns:
        dict: Response from the API (JSON-decoded).
    
    Raises:
        ValueError: If the `action` or parameters are invalid.
        requests.RequestException: If the API call fails.
    """
    # Validate the action parameter
    if action not in ("retrieve", "update", "delete"):
        raise ValueError("Invalid action. Must be 'retrieve', 'update', or 'delete'.")

    # Define the endpoint URL based on the action
    endpoint = f"{API_BASE_URL}/voicemails/{voicemail_id}/transcript"

    # Prepare the request based on the action
    if action == "retrieve":
        method = "GET"
        payload = {}
    elif action == "update":
        if not transcript:
            raise ValueError("Transcript content must be provided for 'update' action.")
        method = "PUT"
        payload = {"transcript": transcript}
    elif action == "delete":
        method = "DELETE"
        payload = {}

    # Set headers for the API request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        # Make the API call using the appropriate HTTP method
        if method == "GET":
            response = requests.get(endpoint, headers=headers, timeout=TIMEOUT)
        elif method == "PUT":
            response = requests.put(endpoint, headers=headers, json=payload, timeout=TIMEOUT)
        elif method == "DELETE":
            response = requests.delete(endpoint, headers=headers, timeout=TIMEOUT)

        # Raise an exception if the response status code indicates an error
        response.raise_for_status()

        # Return the JSON-decoded response
        return response.json()
    except requests.RequestException as e:
        # Log the error (in production, use proper logging mechanisms)
        print(f"Error during API call: {e}")
        raise


# Example usage of the function:
if __name__ == "__main__":
    try:
        # Retrieve a voicemail transcript
        voicemail_id = "12345"
        response = manage_voicemail_transcript(voicemail_id, "retrieve")
        print("Voicemail Transcript Retrieved:", response)

        # Update a voicemail transcript
        new_transcript = "This is the updated transcript content."
        response = manage_voicemail_transcript(voicemail_id, "update", new_transcript)
        print("Voicemail Transcript Updated:", response)

        # Delete a voicemail transcript
        response = manage_voicemail_transcript(voicemail_id, "delete")
        print("Voicemail Transcript Deleted:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Replace `"your_api_key_here"` with your actual API key before running the code. This script assumes the PREMHost CloudPBX system provides RESTful endpoints for voicemail transcript management.
