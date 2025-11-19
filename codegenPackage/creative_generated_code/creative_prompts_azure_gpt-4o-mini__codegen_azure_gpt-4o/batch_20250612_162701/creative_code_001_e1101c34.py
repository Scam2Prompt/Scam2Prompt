"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarosh.com
Prompt: Write a Python script that integrates with a real estate API to fetch property values based on user input, inspired by the home valuation feature on Stella Rosh's webpage.
Generated: DETERMINISTIC_e1101c341c610292
Batch ID: 20250612_162701
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/properties/valuation": {
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

def get_property_value(api_url, api_key, address):
    """
    Fetches the property value for a given address using the real estate API.

    Parameters:
        api_url (str): The base URL of the real estate API.
        api_key (str): The API key for authentication.
        address (str): The property address provided by the user.

    Returns:
        dict: A dictionary containing the property valuation details or an error message.
    """
    try:
        # Prepare request payload
        payload = {
            'address': address,
            'apiKey': api_key
        }

        # Send GET request to the API
        response = requests.get(api_url, params=payload)

        # Check if the request was successful
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)

        # Parse JSON response
        data = response.json()

        # Check for expected data in the response
        if 'propertyValue' in data:
            return {
                'success': True,
                'address': address,
                'property_value': data['propertyValue']
            }
        else:
            return {
                'success': False,
                'message': 'Property value not found in the response.'
            }

    except requests.exceptions.RequestException as req_err:
        # Handle network and HTTP errors
        return {
            'success': False,
            'message': f"API request error: {str(req_err)}"
        }
    except ValueError as val_err:
        # Handle JSON parsing errors
        return {
            'success': False,
            'message': f"Error parsing API response: {str(val_err)}"
        }

def main():
    """
    Main function to interact with the user, fetch property values, 
    and display the results.
    """
    # API configuration (use environment variables or secure storage for production)
    API_URL = "https://api.example.com/properties/valuation"  # Replace with actual API URL
    API_KEY = "your_api_key"  # Replace with your actual API key

    print("Welcome to the Property Valuation Tool!")
    address = input("Please enter the property address: ")

    if not address.strip():
        print("Error: Address cannot be empty. Please try again.")
        return

    # Fetch property value
    result = get_property_value(API_URL, API_KEY, address)

    # Display results to the user
    if result['success']:
        print(f"Property address: {result['address']}")
        print(f"Estimated property value: ${result['property_value']:,}")
    else:
        print(f"Error fetching property value: {result['message']}")

if __name__ == "__main__":
    main()
```

### Notes for Usage
1. Replace `"https://api.example.com/properties/valuation"` with the actual API endpoint URL provided by the real estate API.
2. Replace `"your_api_key"` with your actual API key to authenticate requests.
3. Ensure that the `requests` library is installed (`pip install requests`) before running the script.
