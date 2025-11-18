"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happychex.com
Prompt: Write code to automate the process of linking a domain to a directory on a server using a control panel API. Assume the API supports domain mapping functionality.
Generated: DETERMINISTIC_b1749f586160aa55
Batch ID: 20250612_151024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://controlpanel.example.com/api/v1": {
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

# Configuration constants
API_BASE_URL = "https://controlpanel.example.com/api/v1"  # Base URL for the control panel API
API_KEY = "your-api-key-here"  # API key for authenticating requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def link_domain_to_directory(domain_name, directory_path):
    """
    Automates the process of linking a domain to a directory on a server using the control panel API.

    Args:
        domain_name (str): The domain name to link (e.g., "example.com").
        directory_path (str): The absolute path to the directory (e.g., "/var/www/example").

    Returns:
        dict: The API response. Contains status and details of the operation.

    Raises:
        Exception: Raises an exception if the API request fails or returns an error response.
    """
    # Validate input
    if not domain_name or not directory_path:
        raise ValueError("Both 'domain_name' and 'directory_path' must be provided.")
    
    # Prepare payload for the API request
    payload = {
        "domain": domain_name,
        "directory": directory_path
    }

    try:
        # Send POST request to the control panel API
        response = requests.post(
            f"{API_BASE_URL}/domain-map",
            headers=HEADERS,
            data=json.dumps(payload)
        )
        
        # Raise an HTTPError for bad responses
        response.raise_for_status()
        
        # Parse and return the API response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle network and HTTP errors
        raise Exception(f"Failed to link domain '{domain_name}' to directory '{directory_path}': {str(e)}")
    
    except json.JSONDecodeError as e:
        # Handle errors in decoding the API response
        raise Exception(f"Invalid response from API: {str(e)}")


if __name__ == "__main__":
    # Example usage
    domain = "example.com"
    directory = "/var/www/example"
    
    try:
        result = link_domain_to_directory(domain, directory)
        print("Domain mapping successful:", result)
    except Exception as error:
        print("Error occurred:", error)
```
