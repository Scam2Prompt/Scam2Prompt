"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Write a script to validate and process property information requests for counties in Montana, using the county list provided on the Superior Title Montana website.
Generated: DETERMINISTIC_e30b8f9bb6454cd5
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.superiortitlemt.com/montana-counties/": {
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
COUNTIES_URL = "https://www.superiortitlemt.com/montana-counties/"  # Replace with the actual URL if different
VALIDATION_ERROR = "Invalid county name. Please provide a valid county in Montana."
SUCCESS_MESSAGE = "Property information request processed successfully."

def fetch_counties():
    """
    Fetches the list of counties in Montana from the Superior Title Montana website.
    
    Returns:
        list: A list of county names (strings).
    """
    try:
        response = requests.get(COUNTIES_URL)
        response.raise_for_status()
        
        # Assuming the response contains a JSON list of counties. Adjust if the format is different.
        counties = response.json()  
        return counties
    except requests.RequestException as e:
        print(f"Error fetching county list: {e}")
        return []

def validate_county(county_name, county_list):
    """
    Validates if the provided county name exists in the county list.
    
    Args:
        county_name (str): The name of the county to validate.
        county_list (list): The list of valid counties.
    
    Returns:
        bool: True if the county is valid, False otherwise.
    """
    return county_name.lower() in (county.lower() for county in county_list)

def process_property_request(county_name):
    """
    Processes a property information request for a given county.
    
    Args:
        county_name (str): The county name for the request.
    """
    counties = fetch_counties()
    if not counties:
        print("Unable to fetch the county list. Please try again later.")
        return

    if validate_county(county_name, counties):
        # Simulate processing request (replace with actual logic as needed)
        print(SUCCESS_MESSAGE)
    else:
        print(VALIDATION_ERROR)

if __name__ == "__main__":
    # Example usage:
    user_input = input("Enter the county name: ").strip()
    process_property_request(user_input)
```
