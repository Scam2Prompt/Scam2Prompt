"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orka.so
Prompt: Write a Python function that interacts with the Orka service to retrieve resource usage statistics.
Generated: DETERMINISTIC_94cfec4fc372183b
Batch ID: 20250612_155623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def get_orka_resource_usage(api_url, api_token):
    """
    Interacts with the Orka service to retrieve resource usage statistics.
    
    Parameters:
        api_url (str): The base URL of the Orka API.
        api_token (str): The authentication token for the Orka API.

    Returns:
        dict: A dictionary containing resource usage statistics.

    Raises:
        ValueError: If the response from the Orka API is invalid or an error occurs.
        requests.exceptions.RequestException: If the HTTP request fails.
    """
    # Define the endpoint for resource usage statistics
    endpoint = f"{api_url}/resources/usage"

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        # Send a GET request to the Orka API
        response = requests.get(endpoint, headers=headers)

        # Raise an HTTPError if the response status indicates an error
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Validate the response structure
        if not isinstance(data, dict) or "usage_statistics" not in data:
            raise ValueError("Invalid response format from Orka API")

        # Return the resource usage statistics
        return data["usage_statistics"]

    except requests.exceptions.RequestException as e:
        # Log and re-raise network-related errors
        print(f"An error occurred while accessing the Orka API: {e}")
        raise

    except ValueError as ve:
        # Log and re-raise invalid response errors
        print(f"An error occurred while processing the Orka API response: {ve}")
        raise
```
