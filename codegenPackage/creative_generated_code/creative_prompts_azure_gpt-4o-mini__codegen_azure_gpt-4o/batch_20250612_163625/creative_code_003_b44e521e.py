"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://02ip.ru
Prompt: Generate a code example for utilizing the IP Tracker API to retrieve geolocation data based on an IP address.
Generated: DETERMINISTIC_b44e521e626f5425
Batch ID: 20250612_163625
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.iptracker.com/v1/getLocation": {
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

def get_geolocation_by_ip(ip_address: str) -> dict:
    """
    Retrieve geolocation data for a given IP address using the IP Tracker API.

    Args:
        ip_address (str): The IP address to lookup.

    Returns:
        dict: A dictionary containing geolocation data if successful, or an error message.
    """
    # Base URL for the IP Tracker API (replace with actual API endpoint)
    api_url = "https://api.iptracker.com/v1/getLocation"

    # Replace with your API key
    api_key = "your_api_key_here"

    # Define the parameters for the API request
    params = {
        "ip": ip_address,
        "apiKey": api_key
    }

    try:
        # Make the HTTP GET request to the API
        response = requests.get(api_url, params=params)

        # Check if the response status code indicates success
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the API returned an error in the response
        if "error" in data:
            return {"error": data["error"]}

        # Return the geolocation data
        return {"data": data}

    except requests.exceptions.RequestException as e:
        # Handle HTTP request exceptions (e.g., network errors)
        return {"error": f"An error occurred while making the API request: {str(e)}"}

    except ValueError:
        # Handle JSON parsing errors
        return {"error": "An error occurred while parsing the API response. The response may not be valid JSON."}

# Example usage:
if __name__ == "__main__":
    ip = "8.8.8.8"  # Replace with the IP address you want to lookup
    result = get_geolocation_by_ip(ip)
    print(result)
```
