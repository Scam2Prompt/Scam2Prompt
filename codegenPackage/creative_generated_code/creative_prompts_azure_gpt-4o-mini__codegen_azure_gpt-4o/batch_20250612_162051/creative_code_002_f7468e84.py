"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Create a sample API call for a service that provides emergency electrical support, similar to the 24/7 service mentioned on the Space Technologies website.
Generated: DETERMINISTIC_f7468e8465ed6275
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.spacetechnologies.com/emergency_support": {
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

def request_emergency_support(api_url, api_key, customer_info):
    """
    Makes an API call to request emergency electrical support.

    Parameters:
    - api_url (str): The URL of the emergency support service API.
    - api_key (str): The API key for authentication.
    - customer_info (dict): Dictionary containing customer details.

        Example customer_info:
        {
            "name": "John Doe",
            "phone": "+123456789",
            "address": "123 Main St, Springfield, USA",
            "issue_description": "Power outage affecting the entire house."
        }

    Returns:
    - dict: Response data from the API. If an error occurs, returns a dictionary with the error message.
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the API
        response = requests.post(api_url, json=customer_info, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Return the JSON response
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        # Handle general request errors
        return {"error": f"Request error occurred: {req_err}"}
    except Exception as err:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}

# Example usage of the function:
if __name__ == "__main__":
    # Replace with actual API URL and API key
    API_URL = "https://api.spacetechnologies.com/emergency_support"
    API_KEY = "your_api_key_here"
    
    # Example customer information
    customer_details = {
        "name": "Jane Smith",
        "phone": "+19876543210",
        "address": "456 Elm St, Gotham City, USA",
        "issue_description": "Sudden electrical short circuit in the kitchen."
    }
    
    # Request emergency support
    result = request_emergency_support(API_URL, API_KEY, customer_details)
    print(result)
```
