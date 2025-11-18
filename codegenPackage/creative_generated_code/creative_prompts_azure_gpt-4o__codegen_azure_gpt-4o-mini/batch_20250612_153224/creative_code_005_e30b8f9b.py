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
  "https://www.superiortitlemt.com/counties": {
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
from typing import List, Dict, Any

# Define the URL for the county data source
COUNTY_DATA_URL = "https://www.superiortitlemt.com/counties"

def fetch_county_data() -> List[str]:
    """
    Fetch the list of counties in Montana from the Superior Title website.

    Returns:
        List[str]: A list of county names.

    Raises:
        requests.RequestException: If there is an error while fetching the data.
    """
    try:
        response = requests.get(COUNTY_DATA_URL)
        response.raise_for_status()
        # Assuming the response contains a JSON array of counties
        return response.json()
    except requests.RequestException as e:
        # Handle errors from the requests library
        print(f"Error fetching county data: {e}")
        return []

def validate_property_request(request: Dict[str, Any]) -> bool:
    """
    Validate the property information request.

    Args:
        request (Dict[str, Any]): The request dictionary containing property info.

    Returns:
        bool: True if valid; False otherwise.
    """
    # Basic validation rules
    required_keys = ['county', 'property_id', 'requester_name']
    for key in required_keys:
        if key not in request:
            print(f"Missing required field: {key}")
            return False
        
    if request['county'] not in counties:
        print(f"Invalid county: {request['county']}")
        return False

    return True

def process_property_request(request: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process the validated property information request.

    Args:
        request (Dict[str, Any]): The validated property request.

    Returns:
        Dict[str, Any]: A dictionary containing the response information.
    """
    # Here we would normally interact with a database or an external service
    # Simulating a response for demonstration purposes
    response = {
        "status": "success",
        "data": {
            "property_id": request['property_id'],
            "county": request['county'],
            "owner": "John Doe",  # Simulated data
            "value": 350000  # Simulated data
        }
    }
    return response

# Main execution flow
if __name__ == "__main__":
    # Step 1: Fetch county data
    counties = fetch_county_data()
    
    # Example property request
    example_request = {
        "county": "Gallatin",
        "property_id": "123456",
        "requester_name": "Alice Smith"
    }

    # Step 2: Validate the property request
    if validate_property_request(example_request):
        # Step 3: Process the request if valid
        result = process_property_request(example_request)
        print(result)
    else:
        print("Invalid property request.")
```
