"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xpet-tech.pages.dev
Prompt: Write a function to check the status of a PvP beta test server, similar to the live beta test feature on xPet.tech.
Generated: DETERMINISTIC_96eb52343ce8cbdc
Batch ID: 20250612_152018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/api/server_status": {
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

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_beta_server_status(url: str) -> dict:
    """
    Check the status of a PvP beta test server.

    Args:
        url (str): The URL of the PvP beta test server.

    Returns:
        dict: A dictionary containing the server status and message.

    Raises:
        ValueError: If the provided URL is invalid.
        requests.exceptions.RequestException: If a request to the server fails.
    """
    
    # Validate the URL format
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        raise ValueError("Invalid URL format. Please provide a valid URL.")

    try:
        # Send a GET request to the beta server
        response = requests.get(url)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse and return the server status from the response
        return {
            "status": response.status_code,
            "message": "Server is online.",
            "data": response.json()  # Assuming the server returns JSON data
        }

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return {
            "status": response.status_code,
            "message": "Server returned an error.",
            "data": None
        }
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
        return {
            "status": None,
            "message": "Failed to connect to the server.",
            "data": None
        }
    except ValueError as val_err:
        logging.error(f"Value error: {val_err}")
        return {
            "status": None,
            "message": str(val_err),
            "data": None
        }
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")
        return {
            "status": None,
            "message": "An unexpected error occurred.",
            "data": None
        }

# Example usage (comment this out for production use)
# if __name__ == "__main__":
#     url = "https://example.com/api/server_status"  # Replace with actual server URL
#     status = check_beta_server_status(url)
#     print(status)
```
