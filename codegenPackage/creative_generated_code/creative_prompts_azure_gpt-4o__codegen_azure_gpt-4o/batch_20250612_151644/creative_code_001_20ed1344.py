"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.pl
Prompt: Generate code to automate the process of checking available domains for purchase on Aftermarket.pl using their API. Ensure the script filters results based on specific criteria like price and domain extension.
Generated: DETERMINISTIC_20ed13440fc87b84
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aftermarket.pl/jsonrpc/": {
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
API_ENDPOINT = "https://api.aftermarket.pl/jsonrpc/"
API_KEY = "your_api_key_here"  # Replace with your Aftermarket.pl API key
PRICE_THRESHOLD = 500  # Maximum price (in PLN) for domain
DESIRED_EXTENSIONS = {".pl", ".com", ".net"}  # Set of desired domain extensions

def check_available_domains(search_query):
    """
    Query Aftermarket.pl API to check for available domains and filter results
    based on price and domain extension criteria.
    
    Args:
        search_query (str): The domain search input or criteria.
    Returns:
        list: A list of filtered domains meeting the criteria.
    """
    try:
        # Prepare the API payload
        payload = {
            "jsonrpc": "2.0",
            "method": "domain.list",
            "params": {
                "filter": {
                    "name_contains": search_query,
                    "status": "available"
                }
            },
            "id": 1
        }

        # Make the API request
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)

        # Raise an HTTPError if the response contains a failure status code
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if API returned an error
        if "error" in data:
            raise Exception(f"API Error: {data['error']['message']}")
        
        # Extract domain results
        domains = data.get("result", {}).get("domains", [])
        
        # Filter domains based on price and extension criteria
        filtered_domains = [
            domain for domain in domains
            if domain["price"] <= PRICE_THRESHOLD and
               any(domain["name"].endswith(ext) for ext in DESIRED_EXTENSIONS)
        ]
        
        # Return filtered results
        return filtered_domains
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP/network-related errors
        print(f"An error occurred while making the API request: {e}")
    
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
    
    return []

# Example usage
if __name__ == "__main__":
    search_query = "example"  # Replace with your desired search criteria
    domains = check_available_domains(search_query)
    
    # Display filtered domains
    if domains:
        print("Filtered domains available for purchase:")
        for domain in domains:
            print(f"- {domain['name']} (Price: {domain['price']} PLN)")
    else:
        print("No domains found matching the criteria.")
```

Replace `your_api_key_here` with your actual Aftermarket.pl API key before running the script. Ensure the `search_query` matches your intended domain search pattern.
