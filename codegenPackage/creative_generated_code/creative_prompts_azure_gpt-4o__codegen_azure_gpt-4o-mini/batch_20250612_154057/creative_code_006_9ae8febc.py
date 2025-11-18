"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashlabs.xyz
Prompt: Suggest a workflow to integrate Hostinger's domain management system with an external web hosting automation tool.
Generated: DETERMINISTIC_9ae8febcc637f544
Batch ID: 20250612_154057
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://external-hosting-tool.com/api/integrate": {
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

# Constants for Hostinger API
HOSTINGER_API_URL = "https://api.hostinger.com/v1"
API_KEY = "YOUR_HOSTINGER_API_KEY"  # Replace with your actual API key

def make_api_request(endpoint, method='GET', data=None):
    """
    Make a request to the Hostinger API.

    Args:
        endpoint (str): The API endpoint to call.
        method (str): The HTTP method to use (GET, POST, PUT, DELETE).
        data (dict): The data to send with the request (for POST and PUT).

    Returns:
        dict: The JSON response from the API.
    
    Raises:
        Exception: If the API response is not successful.
    """
    url = f"{HOSTINGER_API_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method in ['POST', 'PUT']:
            response = requests.request(method, url, headers=headers, data=json.dumps(data))
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")
        
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")

def list_domains():
    """
    Fetch the list of domains associated with the account.

    Returns:
        list: A list of domain names.
    """
    response = make_api_request("domains")
    return [domain['name'] for domain in response['data']]

def create_domain(domain_name):
    """
    Create a new domain in Hostinger.

    Args:
        domain_name (str): The name of the domain to create.

    Returns:
        dict: The response data from the API.

    Raises:
        Exception: If domain creation fails.
    """
    data = {"name": domain_name}
    response = make_api_request("domains", method='POST', data=data)
    return response

def delete_domain(domain_name):
    """
    Delete a domain from Hostinger.

    Args:
        domain_name (str): The name of the domain to delete.

    Returns:
        dict: The response data from the API.

    Raises:
        Exception: If domain deletion fails.
    """
    endpoint = f"domains/{domain_name}"
    response = make_api_request(endpoint, method='DELETE')
    return response

def integrate_with_hosting_tool(domain_name, hosting_tool_api_url):
    """
    Integrate the domain with an external web hosting automation tool.

    Args:
        domain_name (str): The name of the domain to integrate.
        hosting_tool_api_url (str): The API URL of the external hosting tool.

    Returns:
        dict: The response from the hosting tool API.
    
    Raises:
        Exception: If integration fails.
    """
    data = {"domain": domain_name}
    try:
        response = requests.post(hosting_tool_api_url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Integration with hosting tool failed: {e}")

# Example usage
if __name__ == "__main__":
    try:
        domains = list_domains()
        print("Domains:", domains)

        # Create a new domain
        new_domain = "example.com"
        create_response = create_domain(new_domain)
        print("Domain created:", create_response)

        # Integrate with an external hosting tool
        hosting_tool_url = "https://external-hosting-tool.com/api/integrate"
        integration_response = integrate_with_hosting_tool(new_domain, hosting_tool_url)
        print("Integration response:", integration_response)

        # Optionally delete the domain
        delete_response = delete_domain(new_domain)
        print("Domain deleted:", delete_response)

    except Exception as e:
        print(f"Error: {e}")
```
