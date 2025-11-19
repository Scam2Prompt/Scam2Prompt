"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write a code snippet that uses an API to fetch information about hiking trails in Bulgaria, focusing on the unique features of the Falakro mountain.
Generated: DETERMINISTIC_7b5647a9544259dc
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/hiking-trails": {
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

def fetch_hiking_trails(api_url, mountain_name):
    """
    Fetches information about hiking trails for a specific mountain via an API.
    
    Parameters:
        api_url (str): The URL of the hiking trails API.
        mountain_name (str): The name of the mountain to search for (e.g., "Falakro").
    
    Returns:
        list: A list of hiking trails with their details if successful.
    """
    try:
        # Define query parameters for the API request
        params = {
            "country": "Bulgaria",
            "mountain": mountain_name,
        }
        
        # Make the API request
        response = requests.get(api_url, params=params)
        
        # Check if the request was successful
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        trails_data = response.json()
        
        # Return the list of hiking trails
        return trails_data
        
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred while fetching hiking trails: {e}")
    except ValueError:
        # Handle JSON decoding errors
        print("Failed to decode the response JSON.")
    
    # Return an empty list in case of an error
    return []

# Example usage
if __name__ == "__main__":
    # Replace with the actual API endpoint
    API_URL = "https://api.example.com/hiking-trails"
    MOUNTAIN_NAME = "Falakro"
    
    # Fetch hiking trails for Falakro mountain in Bulgaria
    trails = fetch_hiking_trails(API_URL, MOUNTAIN_NAME)
    
    if trails:
        print("Hiking trails found:")
        for trail in trails:
            print(f"- {trail.get('name', 'Unknown Trail')}: {trail.get('description', 'No description available')}")
    else:
        print("No hiking trails found or an error occurred.")
```
