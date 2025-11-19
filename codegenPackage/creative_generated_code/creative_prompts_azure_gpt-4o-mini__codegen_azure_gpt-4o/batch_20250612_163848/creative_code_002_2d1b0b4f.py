"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ciaim-basedevo.fun
Prompt: Write a Python script to automate the process of registering a domain name using the Porkbun API.
Generated: DETERMINISTIC_2d1b0b4f5f3c95d0
Batch ID: 20250612_163848
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
API_BASE_URL = "https://porkbun.com/api/json/v3"
API_KEY = "your_api_key_here"  # Replace with your actual API key
API_SECRET_KEY = "your_api_secret_key_here"  # Replace with your actual API secret key

def register_domain(domain_name, years=1):
    """
    Registers a domain name using the Porkbun API.

    Args:
        domain_name (str): The domain name to register (e.g., "example.com").
        years (int): The number of years to register the domain for. Default is 1 year.

    Returns:
        dict: The API response. Contains success status and other details.
    """
    # Endpoint for registering a domain
    endpoint = f"{API_BASE_URL}/domains/registration"

    # Payload for the API request
    payload = {
        "apikey": API_KEY,
        "apisecret": API_SECRET_KEY,
        "domain": domain_name,
        "years": years
    }

    try:
        # Make the API request
        response = requests.post(endpoint, json=payload)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Return the response data
        return response_data
    
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (e.g., network issues, invalid URL)
        return {"success": False, "error": str(e)}
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        return {"success": False, "error": "Invalid JSON response from API"}
    except Exception as e:
        # Catch-all for any other exceptions
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # Example usage: Register a domain "mynewdomain.com" for 2 years
    domain_to_register = "mynewdomain.com"
    registration_years = 2

    # Call the function to register the domain
    result = register_domain(domain_to_register, registration_years)

    # Print the result
    if result.get("success"):
        print(f"Domain '{domain_to_register}' registered successfully!")
        print("Response:", result)
    else:
        print(f"Failed to register domain '{domain_to_register}'.")
        print("Error:", result.get("error"))
```

**Note:** Replace `your_api_key_here` and `your_api_secret_key_here` with your actual credentials obtained from Porkbun.
