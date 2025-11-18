"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxworke.com
Prompt: Provide a Python script to interact with CyberPanel's hosting control panel features, ensuring compatibility with its documentation.
Generated: DETERMINISTIC_7f5e108e9fc8085e
Batch ID: 20250612_153244
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cyberpanel-domain:8090": {
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
from requests.exceptions import HTTPError

# Constants
CYBERPANEL_URL = "https://your-cyberpanel-domain:8090"  # Replace with your CyberPanel URL
API_KEY = "your-api-key"                                # Replace with your CyberPanel API key

# Headers for authentication
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def send_request(endpoint, payload=None, method="GET"):
    """
    Sends an HTTP request to the CyberPanel API.

    Args:
        endpoint (str): The API endpoint.
        payload (dict, optional): Data to send in the request body. Default is None.
        method (str): HTTP method (GET, POST, etc.). Default is "GET".

    Returns:
        dict: JSON response from the API.

    Raises:
        HTTPError: If the request fails.
    """
    url = f"{CYBERPANEL_URL}{endpoint}"
    try:
        if method.upper() == "GET":
            response = requests.get(url, headers=HEADERS, params=payload, timeout=10)
        elif method.upper() == "POST":
            response = requests.post(url, headers=HEADERS, json=payload, timeout=10)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        # Raise an exception if the status code indicates an error
        response.raise_for_status()

        # Return the JSON response
        return response.json()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise

def create_website(domain, email, package):
    """
    Creates a new website on CyberPanel.

    Args:
        domain (str): Domain name for the website.
        email (str): Administrator's email for the website.
        package (str): Hosting package to use.

    Returns:
        dict: API response indicating success or failure.
    """
    endpoint = "/api/createWebsite"
    payload = {
        "domainName": domain,
        "ownerEmail": email,
        "packageName": package,
    }
    return send_request(endpoint, payload, method="POST")

def list_websites():
    """
    Lists all websites on CyberPanel.

    Returns:
        dict: API response containing all websites.
    """
    endpoint = "/api/listWebsites"
    return send_request(endpoint)

def delete_website(domain):
    """
    Deletes a website on CyberPanel.

    Args:
        domain (str): Domain name of the website to delete.

    Returns:
        dict: API response indicating success or failure.
    """
    endpoint = "/api/deleteWebsite"
    payload = {"domainName": domain}
    return send_request(endpoint, payload, method="POST")

# Example usage
if __name__ == "__main__":
    try:
        # Replace the sample data below with actual values
        domain_name = "example.com"
        admin_email = "admin@example.com"
        package_name = "Default"

        # Creating a new website
        print("Creating website...")
        response = create_website(domain_name, admin_email, package_name)
        print("Create Website Response:", response)

        # Listing all websites
        print("Listing websites...")
        response = list_websites()
        print("List Websites Response:", response)

        # Deleting a website
        print("Deleting website...")
        response = delete_website(domain_name)
        print("Delete Website Response:", response)

    except Exception as e:
        print("An error occurred during execution:", e)
```

Replace placeholders with actual values for `CYBERPANEL_URL` and `API_KEY`. Ensure the CyberPanel API is enabled and accessible from your Python script. Follow CyberPanel's official documentation for additional endpoints and required payloads.
