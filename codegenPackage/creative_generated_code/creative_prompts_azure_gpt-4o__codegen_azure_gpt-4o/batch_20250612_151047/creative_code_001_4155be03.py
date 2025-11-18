"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallet.ro
Prompt: Generate code to perform a bulk domain name search using the EUReg API and return the results in JSON format.
Generated: DETERMINISTIC_4155be031b9bf2f6
Batch ID: 20250612_151047
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.eureg.com/v1/bulk-domain-search": {
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
import requests  # For making HTTP requests
import json  # For handling JSON data

def bulk_domain_name_search(api_key, domain_names):
    """
    Perform a bulk domain name search using the EUReg API.
    
    Args:
        api_key (str): Your EUReg API key.
        domain_names (list): List of domain names to search for.
    
    Returns:
        dict: JSON response containing the search results.
    """
    # EUReg API endpoint for bulk domain name search
    api_url = "https://api.eureg.com/v1/bulk-domain-search"
    
    # Construct the request payload
    payload = {
        "domains": domain_names
    }
    
    # Include the API key in the headers for authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make a POST request to the EUReg API
        response = requests.post(api_url, headers=headers, json=payload)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response and return it
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle any errors during the API request
        print(f"Error occurred while making the API request: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    api_key = "your_api_key_here"
    
    # List of domain names to search for
    domain_names = [
        "example.com",
        "mywebsite.net",
        "nonexistentdomain.org"
    ]
    
    # Perform the bulk domain name search
    results = bulk_domain_name_search(api_key, domain_names)
    
    # Print the results in a formatted JSON structure
    print(json.dumps(results, indent=4))
```
