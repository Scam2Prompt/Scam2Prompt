"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://authplay.io
Prompt: Generate a Python function to validate OAuth 2.0 tokens and debug the process using AuthPlay.io.
Generated: DETERMINISTIC_12f25d4813792161
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_auth_server.com/introspect": {
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

def validate_oauth_token(token: str, client_id: str, client_secret: str, auth_server_url: str) -> dict:
    """
    Validate an OAuth 2.0 token against the authorization server.

    Parameters:
        token (str): The access token to validate.
        client_id (str): The client ID for the OAuth application.
        client_secret (str): The client secret for the OAuth application.
        auth_server_url (str): The URL of the authorization server's token introspection endpoint.

    Returns:
        dict: A dictionary containing the validation result and any relevant data from the response.

    Raises:
        ValueError: If the token is empty or if the response is invalid.
        requests.RequestException: For any issues with the HTTP request.
    """
    
    # Check if the token is provided
    if not token:
        raise ValueError("Token must not be empty.")

    # Prepare the request payload for token introspection
    payload = {
        'token': token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    try:
        # Send a POST request to the authorization server for token validation
        response = requests.post(auth_server_url, data=payload)

        # Raise an exception for HTTP error codes
        response.raise_for_status()

        # Parse the JSON response
        validation_response = response.json()

        # Check if the response is valid and contains expected data
        if 'active' in validation_response:
            return validation_response
        else:
            raise ValueError("Invalid response from the authorization server.")

    except requests.RequestException as e:
        # Handle HTTP request-related errors
        raise RuntimeError(f"HTTP request failed: {e}")
    except ValueError as ve:
        # Handle invalid data errors
        raise RuntimeError(f"Token validation error: {ve}")

# Example usage (uncomment and replace with actual values to use):
# result = validate_oauth_token("your_access_token", "your_client_id", "your_client_secret", "https://your_auth_server.com/introspect")
# print(result)
```
