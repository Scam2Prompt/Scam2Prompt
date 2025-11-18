"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: Provide an example of using Porkbun's API to transfer a domain to another registrar programmatically.
Generated: DETERMINISTIC_e01f9e73d835ec84
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3": {
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

# Constants for Porkbun API
BASE_URL = "https://porkbun.com/api/json/v3"
API_KEY = "your_api_key_here"  # Replace with your Porkbun API key
SECRET_KEY = "your_secret_key_here"  # Replace with your Porkbun secret key

# Function to initiate a domain transfer
def transfer_domain(domain_name, auth_code):
    """
    Transfers a domain to another registrar using Porkbun's API.
    
    Args:
        domain_name (str): The domain name to transfer.
        auth_code (str): The authorization code for the domain transfer.
    
    Returns:
        dict: Response from the Porkbun API.
    """
    url = f"{BASE_URL}/domain/transfer"
    headers = {"Content-Type": "application/json"}
    payload = {
        "apikey": API_KEY,
        "secretapikey": SECRET_KEY,
        "domain": domain_name,
        "authcode": auth_code
    }
    
    try:
        # Send POST request to Porkbun API
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the response JSON
        response_data = response.json()
        
        # Check if the transfer was successful
        if response_data.get("status") == "SUCCESS":
            return response_data
        else:
            return {
                "status": "FAILED",
                "message": response_data.get("message", "Unknown error occurred.")
            }
    except requests.exceptions.RequestException as e:
        # Handle potential network or API errors
        return {
            "status": "ERROR",
            "message": str(e)
        }


# Example usage
if __name__ == "__main__":
    # Replace with your actual domain name and authorization code
    DOMAIN_NAME = "example.com"
    AUTH_CODE = "123456789ABCDEF"
    
    # Attempt to transfer the domain
    result = transfer_domain(DOMAIN_NAME, AUTH_CODE)
    
    # Print the result
    print(json.dumps(result, indent=4))
```

Make sure to replace `your_api_key_here` and `your_secret_key_here` with your actual Porkbun API credentials. Also, replace `example.com` and `123456789ABCDEF` with the domain name and authorization code you are working with.
