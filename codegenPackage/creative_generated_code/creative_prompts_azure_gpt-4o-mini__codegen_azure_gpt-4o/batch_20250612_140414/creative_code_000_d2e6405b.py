"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meetsonicsolutions.com
Prompt: Generate a code snippet for integrating a domain registration API with Porkbun for creating a new domain.
Generated: DETERMINISTIC_d2e6405bdaa2ab98
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.porkbun.com/v3": {
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

# Define constants for the Porkbun API
API_BASE_URL = "https://api.porkbun.com/v3"
API_KEY = "your_api_key"  # Replace with your Porkbun API key
SECRET_KEY = "your_secret_key"  # Replace with your Porkbun secret key

def register_domain(domain_name, years=1):
    """
    Registers a domain using the Porkbun API.

    Args:
        domain_name (str): The domain name to register (e.g., "example.com").
        years (int): Number of years to register the domain for. Defaults to 1 year.

    Returns:
        dict: Response data from the Porkbun API.

    Raises:
        Exception: If the API call fails or returns an error.
    """
    endpoint = f"{API_BASE_URL}/domains/registration"
    
    # Prepare the request payload
    payload = {
        "apikey": API_KEY,
        "secretapikey": SECRET_KEY,
        "domain": domain_name,
        "years": years
    }

    try:
        # Send the HTTP POST request to the Porkbun API
        response = requests.post(endpoint, json=payload)
        
        # Check if the response is successful
        response.raise_for_status()
        
        # Parse the response JSON
        response_data = response.json()
        
        # Check for errors in the API response
        if response_data.get("status") != "SUCCESS":
            error_message = response_data.get("message", "Unknown error")
            raise Exception(f"Domain registration failed: {error_message}")
        
        return response_data

    except requests.exceptions.RequestException as e:
        # Handle networking errors
        raise Exception(f"Network error occurred: {e}")
    except Exception as e:
        # Handle other exceptions
        raise Exception(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        domain = "example.com"
        registration_years = 1
        result = register_domain(domain, registration_years)
        print(f"Domain registered successfully: {json.dumps(result, indent=4)}")
    except Exception as error:
        print(f"Failed to register domain: {error}")
```

### Notes:
- Replace `your_api_key` and `your_secret_key` with your actual Porkbun API credentials.
- Ensure the `requests` library is installed (`pip install requests`).
- The code includes error handling for network issues and API errors.
