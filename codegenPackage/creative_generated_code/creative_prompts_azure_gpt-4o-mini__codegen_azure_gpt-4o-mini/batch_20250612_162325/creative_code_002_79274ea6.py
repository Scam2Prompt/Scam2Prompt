"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Create an API request example to fetch the latest promotions for MG vehicles, specifically targeting the MG ZS and MG RX5 models.
Generated: DETERMINISTIC_79274ea6f9d474ab
Batch ID: 20250612_162325
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/promotions/mg": {
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

# Constants for the API endpoint and model specifications
API_URL = "https://api.example.com/promotions/mg"
TARGET_MODELS = ["MG ZS", "MG RX5"]

def fetch_latest_promotions(models):
    """
    Fetches the latest promotions for specific MG vehicle models.

    Args:
        models (list): A list of MG vehicle model names to fetch promotions for.

    Returns:
        dict: A dictionary containing the promotions for the specified models.
              Returns an empty dictionary in case of an error.
    """
    try:
        # Prepare the API request parameters
        params = {"models": ','.join(models)}

        # Make the API request
        response = requests.get(API_URL, params=params)

        # Raise an error for bad responses (4xx and 5xx status codes)
        response.raise_for_status()

        # Return the JSON response if the request was successful
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Log any other request errors
    except Exception as err:
        print(f"An unexpected error occurred: {err}")  # Catch-all for unexpected errors

    return {}  # Return an empty dict in case of error

def main():
    """
    Main function to execute the API request for latest promotions.
    """
    promotions = fetch_latest_promotions(TARGET_MODELS)

    if promotions:
        print("Latest Promotions for MG Vehicles:")
        print(promotions)
    else:
        print("No promotions found or an error occurred.")

if __name__ == "__main__":
    main()
```
