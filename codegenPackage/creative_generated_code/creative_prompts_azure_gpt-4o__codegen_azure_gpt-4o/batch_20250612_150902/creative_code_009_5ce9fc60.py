"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: Write code to fetch and display blog and documentation resources from Zealy's platform using its API.
Generated: DETERMINISTIC_5ce9fc60cc79eedb
Batch ID: 20250612_150902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zealy.io/v1/resources": {
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

def fetch_zealy_resources(api_url, resource_type, api_key):
    """
    Fetch resources from Zealy's platform using its API.
    
    Parameters:
        api_url (str): Base URL of Zealy's API.
        resource_type (str): Type of resource to fetch ('blogs' or 'documentation').
        api_key (str): API key for authentication.
    
    Returns:
        list: A list of resources if successful, or an empty list on failure.
    """
    try:
        # Construct the endpoint URL based on the resource type
        endpoint = f"{api_url}/{resource_type}"
        
        # Define the headers, including the API key for authentication
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Send GET request to the Zealy API
        response = requests.get(endpoint, headers=headers)
        
        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON response and return the resources
            return response.json().get("data", [])
        else:
            # Log the error and return an empty list
            print(f"Error: Failed to fetch {resource_type}. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Exception occurred: {e}")
        return []

def display_resources(resources, resource_type):
    """
    Display resources in a user-friendly format.
    
    Parameters:
        resources (list): List of resources to display.
        resource_type (str): Type of resource ('blogs' or 'documentation').
    """
    print(f"\n--- {resource_type.capitalize()} ---")
    if not resources:
        print(f"No {resource_type} found.")
        return
    
    for index, resource in enumerate(resources, start=1):
        name = resource.get("name", "Unnamed Resource")
        description = resource.get("description", "No description available.")
        print(f"{index}. {name}\n   {description}\n")

def main():
    """
    Main function to fetch and display resources from Zealy's platform.
    """
    # Define base API URL (replace with actual Zealy API URL)
    api_url = "https://api.zealy.io/v1/resources"
    
    # Define authentication API key (replace with your API key)
    api_key = "your_api_key_here"
    
    # Resource types to fetch
    resource_types = ["blogs", "documentation"]
    
    for resource_type in resource_types:
        # Fetch resources from the API
        resources = fetch_zealy_resources(api_url, resource_type, api_key)
        
        # Display the resources in a user-friendly format
        display_resources(resources, resource_type)

if __name__ == "__main__":
    main()
```
