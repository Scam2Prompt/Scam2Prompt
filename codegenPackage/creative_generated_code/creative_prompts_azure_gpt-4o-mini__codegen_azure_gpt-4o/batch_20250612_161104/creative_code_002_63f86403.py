"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Create an API request to fetch data on Krajkovac's attractions, including the church and monastery, and how they reflect the village's heritage.
Generated: DETERMINISTIC_63f8640300424c30
Batch ID: 20250612_161104
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/krajkovac/attractions": {
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

def fetch_krajkovac_attractions(api_url, timeout=10):
    """
    Fetch data about Krajkovac's attractions from the provided API endpoint.

    Args:
        api_url (str): The URL of the API endpoint.
        timeout (int): Timeout for the API request in seconds. Defaults to 10 seconds.

    Returns:
        dict: Parsed JSON data containing information about Krajkovac's attractions.

    Raises:
        ValueError: If the response status is not 200 or the API returns an error.
        requests.exceptions.RequestException: For errors during the HTTP request.
    """
    try:
        # Sending GET request to fetch data from the API
        response = requests.get(api_url, timeout=timeout)

        # Check if the response status code is OK (200)
        if response.status_code != 200:
            raise ValueError(f"Error fetching data: HTTP Status Code {response.status_code}")

        # Attempting to parse the response content as JSON
        data = response.json()

        # Ensure the response contains the expected data structure
        if 'attractions' not in data or not isinstance(data['attractions'], list):
            raise ValueError("Unexpected response structure: 'attractions' not found or invalid format.")

        return data

    except requests.exceptions.RequestException as e:
        # Catching any request-related errors
        raise RuntimeError(f"Failed to fetch data due to a network error: {e}")

    except ValueError as ve:
        # Catching errors related to invalid response content
        raise RuntimeError(f"Failed to process the API response: {ve}")

# Example usage
if __name__ == "__main__":
    # Replace with the actual API URL
    API_URL = "https://api.example.com/krajkovac/attractions"

    try:
        attractions_data = fetch_krajkovac_attractions(API_URL)
        print("Successfully fetched Krajkovac attractions:")
        print(attractions_data)
    except RuntimeError as error:
        print(f"Error: {error}")
```
