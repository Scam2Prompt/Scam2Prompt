"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devv.sellpass.io
Prompt: Write a function to handle errors when accessing resources, inspired by the error message mentioned on the Devv webpage.
Generated: DETERMINISTIC_ec4418b32d834a70
Batch ID: 20250612_154313
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/resource": {
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
import logging
import requests

# Configure logging for error handling
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def access_resource(url):
    """
    Access a resource from the given URL and handle errors appropriately.

    Parameters:
    url (str): The URL of the resource to access.

    Returns:
    dict or None: Returns the JSON response if successful or None in case of an error.
    """
    try:
        # Attempt to send a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        
        # If the request was successful, return the JSON content
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 404, 500)
        logging.error(f'HTTP error occurred: {http_err} - URL: {url}')
    except requests.exceptions.ConnectionError as conn_err:
        # Handle connection errors
        logging.error(f'Connection error occurred: {conn_err} - URL: {url}')
    except requests.exceptions.Timeout as timeout_err:
        # Handle timeout errors
        logging.error(f'Timeout error occurred: {timeout_err} - URL: {url}')
    except requests.exceptions.RequestException as req_err:
        # Handle any other request-related errors
        logging.error(f'An error occurred: {req_err} - URL: {url}')
    except Exception as e:
        # Handle any other unexpected errors
        logging.error(f'An unexpected error occurred: {e} - URL: {url}')

    # Return None if an error occurred
    return None

# Example of how to use the function
if __name__ == "__main__":
    resource_url = "https://api.example.com/resource"
    result = access_resource(resource_url)
    if result is not None:
        print("Resource accessed successfully:", result)
    else:
        print("Failed to access resource.")
```
