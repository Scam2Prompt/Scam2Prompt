"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-networks-app.vercel.app
Prompt: Provide an example of using The Graph Networks Registry v0.0.0 to perform a search query for graph networks matching specific criteria.
Generated: DETERMINISTIC_8eb0b38f1bccbcf4
Batch ID: 20250612_154737
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.graphnetworks.io/v0.0.0": {
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
# Import required libraries
import requests

# Define the base URL for The Graph Networks Registry API
BASE_URL = "https://api.graphnetworks.io/v0.0.0"

# Function to perform a search query for graph networks
def search_graph_networks(query_params):
    """
    Searches The Graph Networks Registry for graph networks matching specific criteria.

    Args:
        query_params (dict): A dictionary containing search query parameters.

    Returns:
        list: A list of graph networks matching the criteria.
    """
    # Construct the endpoint URL for the search query
    search_endpoint = f"{BASE_URL}/networks/search"
    
    try:
        # Make the GET request with the query parameters
        response = requests.get(search_endpoint, params=query_params)
        
        # Raise an exception if the request was not successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Return the list of matching networks
        return data.get("networks", [])
    except requests.exceptions.RequestException as e:
        # Log the error and raise an exception
        print(f"Error occurred while querying graph networks: {e}")
        raise
    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error occurred while parsing response: {e}")
        raise

# Example usage of the function
if __name__ == "__main__":
    # Define the search criteria
    criteria = {
        "name": "example-network",  # Search for networks with this name
        "tags": ["blockchain", "finance"],  # Filter by tags (optional)
        "status": "active",  # Filter by status (e.g., active or inactive, optional)
    }

    try:
        # Perform the search query
        matching_networks = search_graph_networks(criteria)
        
        # Print the results
        print("Matching Networks:")
        for network in matching_networks:
            print(f"- Name: {network['name']}, Tags: {network['tags']}, Status: {network['status']}")
    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")
```

This code assumes that The Graph Networks Registry API exists at the specified URL and adheres to the `/networks/search` endpoint format. Be sure to adjust the endpoint and API specification to match the actual implementation.
