"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celaroopl.xyz
Prompt: Generate a Python script that retrieves and displays the total loans originated and total value locked from the Clearpool API.
Generated: DETERMINISTIC_d463e53626f090d7
Batch ID: 20250612_162701
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.clearpool.finance/analytics/v1": {
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

def fetch_clearpool_data():
    """
    Fetches Clearpool data from the API and displays total loans originated and total value locked.

    Returns:
        None: Prints the fetched data.
    """
    # Clearpool API endpoint
    api_url = "https://api.clearpool.finance/analytics/v1"

    try:
        # Make a GET request to the Clearpool API
        response = requests.get(api_url)
        # Raise an error if the response status code is not 200 (OK)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract required metrics
        total_loans_originated = data.get("totalLoansOriginated")
        total_value_locked = data.get("totalValueLocked")
        
        # Check if the required data is present
        if total_loans_originated is None or total_value_locked is None:
            raise ValueError("Required data is missing from the API response.")
        
        # Display the results
        print("Total Loans Originated:", total_loans_originated)
        print("Total Value Locked:", total_value_locked)
    
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other types of request-related errors
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        # Handle value errors related to missing or invalid data
        print(f"Data error: {val_err}")
    except Exception as err:
        # Handle any other exceptions
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Run the script and fetch Clearpool data
    fetch_clearpool_data()
```
