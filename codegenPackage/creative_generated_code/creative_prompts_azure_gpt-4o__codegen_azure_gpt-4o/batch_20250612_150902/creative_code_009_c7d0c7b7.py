"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustwallet-app.erpnext.com
Prompt: Write a function to monitor resource usage on Frappe Cloud for hosted applications.
Generated: DETERMINISTIC_c7d0c7b7b501ea5c
Batch ID: 20250612_150902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.frappecloud.com/resource-usage": {
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
from typing import Dict, Any

def monitor_resource_usage(api_key: str) -> Dict[str, Any]:
    """
    Monitors resource usage for hosted applications on Frappe Cloud.

    Args:
        api_key (str): The API key to authenticate with the Frappe Cloud resource monitoring service.

    Returns:
        Dict[str, Any]: A dictionary containing resource usage metrics such as CPU, memory, storage, etc.
    """
    # Endpoint for Frappe Cloud resource usage API
    api_url = "https://api.frappecloud.com/resource-usage"

    # Headers for the API request (authentication)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make an HTTP GET request to fetch resource usage data
        response = requests.get(api_url, headers=headers)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        resource_data = response.json()

        # Return the resource usage data
        return resource_data

    except requests.exceptions.RequestException as e:
        # Handle connection issues, timeout, etc.
        return {"error": f"An error occurred while fetching resource usage: {str(e)}"}

    except ValueError:
        # Handle JSON parsing errors
        return {"error": "Failed to parse resource usage data from response"}

# Example usage of the function
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual Frappe Cloud API key
    api_key = "your_api_key_here"
    resource_usage = monitor_resource_usage(api_key)
    print(resource_usage)
```
