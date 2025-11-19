"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Create an API request example for a service that provides instant quotes for dumpster rentals, inspired by the customer interaction model of Junk in The Box ATL.
Generated: DETERMINISTIC_05a56db21af1406d
Batch ID: 20250612_163350
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dumpster-rentals.example.com/quotes": {
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

def get_instant_quote(zip_code, dumpster_size, rental_duration):
    """
    Makes a request to the dumpster rental API to get an instant quote.

    Parameters:
    zip_code (str): The zip code where the dumpster is needed.
    dumpster_size (str): Size of the dumpster (e.g., "10-yard", "20-yard").
    rental_duration (int): Rental duration in days.

    Returns:
    dict: The response from the API containing the rental quote.
    """
    # API URL (replace with the actual API endpoint)
    API_BASE_URL = "https://api.dumpster-rentals.example.com/quotes"

    # Payload for the request
    payload = {
        "zip_code": zip_code,
        "dumpster_size": dumpster_size,
        "rental_duration": rental_duration
    }

    # HTTP headers for the API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_api_key_here"  # Replace with your actual API key
    }

    try:
        # Send a POST request to the API
        response = requests.post(API_BASE_URL, json=payload, headers=headers)

        # Raise an HTTPError if the response contains a client or server error
        response.raise_for_status()

        # Parse and return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log the error and return a message
        print(f"Error making API request: {e}")
        return {"error": "Failed to retrieve quote. Please try again later."}

# Example usage
if __name__ == "__main__":
    # Inputs for the quote
    zip_code = "30301"
    dumpster_size = "20-yard"
    rental_duration = 7

    # Get the quote
    quote = get_instant_quote(zip_code, dumpster_size, rental_duration)

    # Print the result
    print("Quote Response:", quote)
```
