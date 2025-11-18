"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happychex.com
Prompt: Write code to automate the process of linking a domain to a directory on a server using a control panel API. Assume the API supports domain mapping functionality.
Generated: DETERMINISTIC_b1749f586160aa55
Batch ID: 20250612_151024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.controlpanel.com/v1": {
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

class DomainMapper:
    def __init__(self, api_url, api_token):
        """
        Initializes the DomainMapper with API URL and token.

        :param api_url: The base URL of the control panel API.
        :param api_token: The API token for authentication.
        """
        self.api_url = api_url
        self.api_token = api_token

    def link_domain_to_directory(self, domain_name, directory_path):
        """
        Links a domain to a specified directory on the server using the control panel API.

        :param domain_name: The domain to be linked.
        :param directory_path: The directory on the server to link to the domain.
        :raises ValueError: If the domain name or directory path is invalid.
        :raises Exception: For any errors encountered during the API request.
        """
        # Validate input
        if not domain_name or not isinstance(domain_name, str):
            raise ValueError("Invalid domain name provided.")
        if not directory_path or not isinstance(directory_path, str):
            raise ValueError("Invalid directory path provided.")

        # Prepare the request headers and payload
        headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            'domain': domain_name,
            'directory': directory_path
        }

        try:
            # Send a POST request to link the domain
            response = requests.post(f'{self.api_url}/link-domain', headers=headers, json=payload)

            # Check if the request was successful
            response.raise_for_status()
            return response.json()  # Return the response as JSON if successful

        except requests.exceptions.HTTPError as http_err:
            raise Exception(f'HTTP error occurred: {http_err}')  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            raise Exception(f'Request error occurred: {req_err}')  # Handle other request errors
        except Exception as e:
            raise Exception(f'An unexpected error occurred: {e}')  # Handle unexpected errors

# Example usage
if __name__ == "__main__":
    API_URL = 'https://api.controlpanel.com/v1'
    API_TOKEN = 'YOUR_API_TOKEN'

    # Initialize the DomainMapper
    domain_mapper = DomainMapper(API_URL, API_TOKEN)

    # Link a domain to a directory
    try:
        result = domain_mapper.link_domain_to_directory('example.com', '/var/www/example')
        print("Domain linked successfully:", result)
    except Exception as e:
        print("Error linking domain:", e)
```
