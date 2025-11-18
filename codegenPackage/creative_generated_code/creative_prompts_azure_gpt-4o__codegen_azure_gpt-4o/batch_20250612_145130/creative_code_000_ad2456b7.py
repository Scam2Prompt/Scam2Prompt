"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Write a script to automate the creation of WordPress Playground environments using the InMotion Central API.
Generated: DETERMINISTIC_ad2456b76a85375a
Batch ID: 20250612_145130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.inmotioncentral.com/v1": {
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
import json

# Constants
API_BASE_URL = "https://api.inmotioncentral.com/v1"  # InMotion Central API base URL
API_KEY = "your_api_key_here"  # Replace with your API key
SITE_NAME = "MyWordPressPlayground"  # Replace with desired site name
SITE_DOMAIN = "example-playground.com"  # Replace with desired domain name

def create_wordpress_playground(api_key, site_name, site_domain):
    """
    Automate the creation of a WordPress Playground environment using the InMotion Central API.

    Args:
        api_key (str): Your InMotion Central API key.
        site_name (str): Desired name for the WordPress site.
        site_domain (str): Desired domain for the WordPress site.

    Returns:
        dict: API response with details of the created environment or error information.
    """

    # Endpoint to create a WordPress site
    endpoint = f"{API_BASE_URL}/sites"

    # Headers for API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Payload for the API request
    payload = {
        "name": site_name,
        "domain": site_domain,
        "type": "wordpress",  # Specify WordPress as the site type
        "environment": "staging",  # Use staging as the environment type
    }

    try:
        # Send POST request to the API
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

        # Check for HTTP errors
        response.raise_for_status()

        # Parse and return the API response
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Request error occurred: {req_err}"}
    except Exception as err:
        return {"error": f"An unexpected error occurred: {err}"}

if __name__ == "__main__":
    # Call the function to create a WordPress Playground environment
    result = create_wordpress_playground(API_KEY, SITE_NAME, SITE_DOMAIN)

    # Output the result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("WordPress Playground environment created successfully!")
        print(json.dumps(result, indent=4))
```

**Note:** You must replace `your_api_key_here` with your actual API key and ensure the domain name is suitable for your use case and does not conflict with existing domains.
