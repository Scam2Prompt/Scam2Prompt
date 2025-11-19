"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Write a Python script that connects to an API of an investment education firm, utilizing Immediate Bitwave's matching process to find suitable educational resources based on user preferences.
Generated: DETERMINISTIC_84fd002e08fe3406
Batch ID: 20250612_163029
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.investmenteducationfirm.com/v1": {
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

# Constants for the API
API_BASE_URL = "https://api.investmenteducationfirm.com/v1"
API_ENDPOINT = "/resources/match"
API_KEY = "your_api_key_here"  # Replace with your valid API key

def get_matching_resources(user_preferences):
    """
    Connects to the investment education firm's API and retrieves suitable educational 
    resources based on user preferences using Immediate Bitwave's matching process.
    
    Args:
        user_preferences (dict): A dictionary containing user preferences.
    
    Returns:
        list: A list of matching educational resources.
    """
    try:
        # Prepare request headers and payload
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = json.dumps(user_preferences)
        
        # Make the request to the API
        response = requests.post(f"{API_BASE_URL}{API_ENDPOINT}", headers=headers, data=payload)
        
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        
        # Parse and return the JSON response
        resources = response.json()
        return resources
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
    except json.JSONDecodeError as json_err:
        # Handle JSON parsing errors
        print(f"JSON decode error occurred: {json_err}")
    except Exception as err:
        # Handle any other unexpected errors
        print(f"An error occurred: {err}")
    return None

if __name__ == "__main__":
    # Example user preferences
    user_preferences = {
        "investment_level": "beginner",
        "preferred_topics": ["stocks", "bonds"],
        "learning_style": "visual",
        "availability": "evening"
    }
    
    # Get matching resources
    matching_resources = get_matching_resources(user_preferences)
    
    # Output the results
    if matching_resources:
        print("Matching Educational Resources:")
        for resource in matching_resources:
            print(f"- {resource['title']}: {resource['description']}")
    else:
        print("No matching resources found or an error occurred.")
```
