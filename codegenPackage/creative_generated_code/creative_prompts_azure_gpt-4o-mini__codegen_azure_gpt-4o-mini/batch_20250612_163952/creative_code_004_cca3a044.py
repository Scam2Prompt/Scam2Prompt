"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsplug.epizy.com
Prompt: Create a guide for enabling SSL on a website hosted with iFastNet, focusing on the free and simple SSL feature.
Generated: DETERMINISTIC_cca3a044a66593be
Batch ID: 20250612_163952
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://{website": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ifastnet.com/enable_ssl?domain={website_url": {
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
from requests.exceptions import RequestException
import logging

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enable_ssl_ifastnet(website_url):
    """
    Enables SSL on a website hosted with iFastNet using the free SSL feature.
    
    Parameters:
        website_url (str): The URL of the website to enable SSL for.
        
    Returns:
        str: A message indicating the result of the operation.
    """
    # Ensure that the URL starts with http or https
    if not website_url.startswith(('http://', 'https://')):
        logging.error("Invalid URL: URL must start with 'http://' or 'https://'")
        return "Error: Invalid URL provided."

    try:
        # Construct the API endpoint for enabling SSL
        ssl_api_url = f"https://api.ifastnet.com/enable_ssl?domain={website_url}"

        # Send a request to the iFastNet API to enable SSL
        response = requests.post(ssl_api_url)

        # Check if the response is successful
        response.raise_for_status()  # Will raise an HTTPError for bad responses

        # Parse the response
        response_data = response.json()
        
        # Check the response content for success indication
        if response_data.get('status') == 'success':
            logging.info("SSL enabled successfully for %s", website_url)
            return "SSL has been successfully enabled for your website."
        else:
            logging.warning("Failed to enable SSL: %s", response_data.get('message', 'No message provided'))
            return f"Error: {response_data.get('message', 'Unknown error occurred')}"

    except RequestException as e:
        logging.error("Request failed: %s", e)
        return "Error: Unable to enable SSL due to a network issue."

    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        return "Error: An unexpected error occurred."

# Example usage
if __name__ == "__main__":
    website = input("Enter the website URL (without http/https): ")
    result = enable_ssl_ifastnet(f"http://{website}")  # Prepend with http for API call
    print(result)
```
