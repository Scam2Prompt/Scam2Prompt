"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Develop an API request to fetch details about Yanmar miniexcavadoras, focusing on their applications in construction and agriculture.
Generated: DETERMINISTIC_871a008b118d24c3
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/machinery/details": {
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

# Define a function to fetch details about Yanmar miniexcavadoras
def fetch_yanmar_miniexcavadoras_details():
    """
    Fetch details about Yanmar miniexcavadoras, focusing on their applications
    in construction and agriculture using an external API.

    Returns:
        dict: A dictionary containing the fetched data or an error message.
    """
    # Base URL for the API endpoint
    api_url = "https://api.example.com/machinery/details"

    # Query parameters to refine the search
    params = {
        "brand": "Yanmar",
        "type": "miniexcavadoras",
        "applications": "construction,agriculture"
    }

    # Headers for the API request (e.g., authentication token, content type)
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params, headers=headers)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Return the fetched data
        return data

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        return {"error": f"Request error occurred: {req_err}"}
    except Exception as err:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {err}"}

# Example usage of the function
if __name__ == "__main__":
    # Fetch and print the details about Yanmar miniexcavadoras
    details = fetch_yanmar_miniexcavadoras_details()
    print(details)
```
