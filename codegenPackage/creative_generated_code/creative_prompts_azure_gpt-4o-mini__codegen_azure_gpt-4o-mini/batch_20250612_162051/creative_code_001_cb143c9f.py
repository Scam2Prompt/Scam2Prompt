"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Write a Python script that integrates with a roofing service API to fetch quotes for residential roofing projects, specifically for shingles and tile roofs.
Generated: DETERMINISTIC_cb143c9f74e547d5
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.roofingservice.com/v1/quotes": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for API integration
API_URL = "https://api.roofingservice.com/v1/quotes"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_roofing_quotes(roof_type, dimensions):
    """
    Fetch quotes for residential roofing projects.

    Args:
        roof_type (str): The type of roof ('shingles' or 'tiles').
        dimensions (dict): The dimensions of the roof in square feet, e.g. {'length': 40, 'width': 30}.

    Returns:
        dict: The quote details returned by the API.

    Raises:
        ValueError: If an invalid roof_type is provided.
        Exception: If there is an issue with the API request.
    """

    # Validate roof type
    if roof_type not in ['shingles', 'tiles']:
        logging.error("Invalid roof type: %s. Must be 'shingles' or 'tiles'.", roof_type)
        raise ValueError("Invalid roof type. Must be 'shingles' or 'tiles'.")

    # Prepare the request payload
    payload = {
        "roof_type": roof_type,
        "dimensions": dimensions,
        "api_key": API_KEY
    }

    try:
        # Send GET request to the roofing service API
        response = requests.get(API_URL, params=payload)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse JSON response
        quote_data = response.json()
        logging.info("Successfully fetched quote for %s roof.", roof_type)
        return quote_data

    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTP error occurred: %s", http_err)
        raise
    except requests.exceptions.RequestException as req_err:
        logging.error("Request exception occurred: %s", req_err)
        raise
    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise

if __name__ == "__main__":
    # Example usage
    roof_type = "shingles"  # Change to 'tiles' for tile roofs
    dimensions = {"length": 40, "width": 30}  # Example dimensions in feet

    try:
        quote = fetch_roofing_quotes(roof_type, dimensions)
        print("Quote details:", quote)
    except Exception as e:
        print("Failed to fetch roofing quote:", e)
```
