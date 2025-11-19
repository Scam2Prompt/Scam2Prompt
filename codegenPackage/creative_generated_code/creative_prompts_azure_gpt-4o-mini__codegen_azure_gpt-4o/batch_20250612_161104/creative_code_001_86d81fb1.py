"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Write a Python function that retrieves and displays information about the ethno-tourism opportunities in Krajkovac, focusing on local culture and history.
Generated: DETERMINISTIC_86d81fb16f1eff65
Batch ID: 20250612_161104
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example-tourism-api.com/v1/ethno-tourism": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example-tourism-api.com/v1/ethno-tourism`": {
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

def fetch_ethno_tourism_info(location="Krajkovac"):
    """
    Retrieves and displays information about ethno-tourism opportunities in a given location.

    Args:
        location (str): The location for which to fetch ethno-tourism information. 
                        Default is "Krajkovac".

    Returns:
        None
    """
    try:
        # Base URL for the tourism API (Assumed placeholder for demonstration purposes)
        base_url = "https://example-tourism-api.com/v1/ethno-tourism"
        
        # API request parameters
        params = {
            "location": location,
            "category": "culture_history"
        }
        
        # Make a GET request to fetch data
        response = requests.get(base_url, params=params)
        
        # Raise an error if the request was not successful
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if data is available
        if not data or "opportunities" not in data:
            print(f"No ethno-tourism opportunities found for {location}.")
            return
        
        # Display information
        print(f"Ethno-Tourism Opportunities in {location}:")
        for idx, opportunity in enumerate(data["opportunities"], start=1):
            print(f"{idx}. {opportunity['name']}")
            print(f"   Description: {opportunity['description']}")
            print(f"   Address: {opportunity['address']}")
            print(f"   Contact: {opportunity['contact']}")
            print("-" * 40)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
fetch_ethno_tourism_info()  # Fetch information for Krajkovac
```

Note: Replace `https://example-tourism-api.com/v1/ethno-tourism` with a real API endpoint.
