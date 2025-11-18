"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.org
Prompt: Provide a step-by-step guide to access the Speedtest Global Index data programmatically using the Ookla API, including code examples in Python.
Generated: DETERMINISTIC_2710146d6718a410
Batch ID: 20250612_150347
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.speedtest.net/api/global-index`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.speedtest.net/api/global-index": {
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

# Step 1: Define the base URL for the Ookla Speedtest Global Index API
BASE_URL = "https://www.speedtest.net/api/global-index"

# Step 2: Define a function to fetch data from the API
def fetch_speedtest_data(region=None, country=None):
    """
    Fetch Speedtest Global Index data from Ookla API.
    
    Parameters:
        region (str): Optional. Specify a region to filter results.
        country (str): Optional. Specify a country to filter results.

    Returns:
        dict: Parsed JSON data from the API response.
    """
    try:
        # Step 3: Build the request parameters
        params = {}
        if region:
            params["region"] = region
        if country:
            params["country"] = country

        # Step 4: Make the GET request to the API
        response = requests.get(BASE_URL, params=params)

        # Step 5: Check if the response is successful
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)

        # Step 6: Parse and return the JSON response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        # Handle timeout errors
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request exceptions
        print(f"An error occurred: {req_err}")
    except Exception as ex:
        # Catch any other exceptions
        print(f"An unexpected error occurred: {ex}")

    # Return None if there is an error
    return None

# Step 7: Example usage of the function
if __name__ == "__main__":
    # Fetch global data
    print("Fetching global Speedtest data...")
    global_data = fetch_speedtest_data()
    if global_data:
        print("Global data retrieved successfully!")
        print(global_data)
    
    # Fetch data for a specific region or country
    print("\nFetching Speedtest data for a specific country...")
    country_data = fetch_speedtest_data(country="US")
    if country_data:
        print("Country-specific data retrieved successfully!")
        print(country_data)
```

This Python script is designed to retrieve data from the Speedtest Global Index API programmatically. Replace `https://www.speedtest.net/api/global-index` with the correct API URL if required, and ensure any necessary authentication headers or API keys are added if the API requires authentication.
