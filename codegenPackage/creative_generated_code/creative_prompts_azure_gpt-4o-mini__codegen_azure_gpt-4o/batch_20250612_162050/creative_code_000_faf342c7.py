"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Write a Python script that utilizes the Silver Seals API to retrieve information about their oil seals and their applications in various industries.
Generated: DETERMINISTIC_faf342c7745dec84
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.silverseals.com/v1": {
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

# Constants
API_BASE_URL = "https://api.silverseals.com/v1"  # Replace with the actual Silver Seals API base URL
API_ENDPOINT = "/oil_seals"  # Endpoint to retrieve oil seals information
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_oil_seal_data():
    """
    Fetches oil seal data from the Silver Seals API.
    
    Returns:
        list: A list of dictionaries containing oil seal information.
    """
    try:
        # Construct the API request headers
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Make the API request
        response = requests.get(API_BASE_URL + API_ENDPOINT, headers=headers)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        return data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Log other request errors
    except Exception as err:
        print(f"An unexpected error occurred: {err}")  # Catch-all for unexpected errors
    return None

def display_oil_seal_info(oil_seals):
    """
    Displays oil seal information in a user-friendly format.
    
    Args:
        oil_seals (list): A list of dictionaries containing oil seal data.
    """
    if not oil_seals:
        print("No oil seal data to display.")
        return
    
    print("\nOil Seal Information:")
    print("-" * 40)
    for seal in oil_seals:
        # Display relevant details for each oil seal
        print(f"Name: {seal.get('name', 'N/A')}")
        print(f"Description: {seal.get('description', 'N/A')}")
        print(f"Material: {seal.get('material', 'N/A')}")
        print(f"Industry Applications: {', '.join(seal.get('applications', []))}")
        print("-" * 40)

def main():
    """
    Main function to retrieve and display oil seal information.
    """
    print("Fetching oil seal data from Silver Seals API...")
    oil_seal_data = fetch_oil_seal_data()
    
    if oil_seal_data:
        display_oil_seal_info(oil_seal_data)
    else:
        print("Failed to retrieve oil seal data.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `API_BASE_URL` and `API_KEY` with actual values from Silver Seals API documentation or credentials.
2. Ensure the `requests` library is installed (`pip install requests`).
3. Add additional validation if the API response structure is complex.
