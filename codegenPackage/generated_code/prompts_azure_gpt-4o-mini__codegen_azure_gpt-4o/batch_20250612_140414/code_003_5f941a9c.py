"""
Generated Code Metadata:
========================
Original URL: https://onlysonicsolutions.com
Prompt: Generate a script that automates the process of checking domain availability on Porkbun.
Generated: DETERMINISTIC_5f941a9c3fee078b
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3/domain/check": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests

def check_domain_availability(domain_name, api_key):
    """
    Check the availability of a domain name using the Porkbun API.

    Args:
        domain_name (str): The domain name to check (e.g., "example.com").
        api_key (str): Your Porkbun API key.

    Returns:
        str: A message indicating whether the domain is available or not.
    """
    # Porkbun API endpoint for checking domain availability
    url = "https://porkbun.com/api/json/v3/domain/check"

    # Payload for the API request
    payload = {
        "apikey": api_key,
        "domain": domain_name
    }

    try:
        # Send a POST request to the Porkbun API
        response = requests.post(url, json=payload)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check the availability status
        if data.get("status") == "SUCCESS":
            if data.get("available") == "yes":
                return f"The domain '{domain_name}' is available."
            else:
                return f"The domain '{domain_name}' is not available."
        else:
            return f"Error: {data.get('message', 'Unknown error occurred.')}"
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return f"Network error: {str(e)}"
    except Exception as e:
        # Handle other unexpected errors
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    # Example usage
    # Replace 'your_api_key_here' with your actual Porkbun API key
    api_key = "your_api_key_here"
    domain_name = "example.com"

    # Check domain availability
    result = check_domain_availability(domain_name, api_key)
    print(result)
```

**Note:** Replace `"your_api_key_here"` with your actual Porkbun API key before running the script.
