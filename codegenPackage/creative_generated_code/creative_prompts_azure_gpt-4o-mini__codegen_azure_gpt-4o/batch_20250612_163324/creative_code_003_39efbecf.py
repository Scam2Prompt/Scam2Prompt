"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiilama.com
Prompt: Create a code snippet that uses the DeFi Llama API to get historical data for a specific DeFi token.
Generated: DETERMINISTIC_39efbecfa6e99b23
Batch ID: 20250612_163324
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.llama.fi": {
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
import datetime


def fetch_defi_token_historical_data(token_name: str, start_date: str, end_date: str):
    """
    Fetch historical data for a specific DeFi token using the DeFi Llama API.

    :param token_name: The name of the DeFi token (e.g., "bitcoin", "ethereum").
    :param start_date: The start date for the historical data in the format 'YYYY-MM-DD'.
    :param end_date: The end date for the historical data in the format 'YYYY-MM-DD'.
    :return: A list of historical data for the specified token within the date range.
    :raises ValueError: If the date format is invalid or the API request fails.
    """
    # Validate date format
    try:
        start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    # Validate date range
    if end_date_obj < start_date_obj:
        raise ValueError("End date cannot be earlier than start date.")

    # DeFi Llama historical data endpoint
    base_url = "https://api.llama.fi"
    endpoint = f"{base_url}/charts/{token_name}"

    try:
        # Make a GET request to fetch data
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the response JSON
        data = response.json()

        # Filter the data within the date range
        filtered_data = [
            entry
            for entry in data
            if start_date <= entry["date"] <= end_date
        ]

        return filtered_data

    except requests.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"Failed to fetch data from DeFi Llama API: {e}")

    except KeyError:
        # Handle missing keys in the API response
        raise RuntimeError("Unexpected response format from DeFi Llama API.")


# Example usage
if __name__ == "__main__":
    token = "ethereum"
    start = "2023-01-01"
    end = "2023-01-31"

    try:
        historical_data = fetch_defi_token_historical_data(token, start, end)
        print(f"Historical data for {token} between {start} and {end}:")
        for entry in historical_data:
            print(entry)
    except Exception as e:
        print(f"Error: {e}")
```
