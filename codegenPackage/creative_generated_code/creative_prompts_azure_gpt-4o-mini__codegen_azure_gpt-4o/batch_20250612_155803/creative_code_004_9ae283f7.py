"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupi.red
Prompt: Provide an example of API calls to check the status of a website hosted on Ispmanager.
Generated: DETERMINISTIC_9ae283f70901bada
Batch ID: 20250612_155803
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-ispmanager-instance.example.com": {
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

class ISPManagerAPI:
    """
    A class to interact with the ISPmanager API for checking website status.
    """
    def __init__(self, base_url, username, password):
        """
        Initializes the ISPManagerAPI class with authentication details.
        
        :param base_url: The base URL of the ISPmanager instance.
        :param username: Username for authentication.
        :param password: Password for authentication.
        """
        self.base_url = base_url
        self.auth = (username, password)

    def check_website_status(self, domain_name):
        """
        Checks the status of a website hosted on ISPmanager.
        
        :param domain_name: The domain name of the website to check.
        :return: A dictionary containing the status of the website or an error message.
        """
        endpoint = f"{self.base_url}/json/v5/site.domain"
        params = {"func": "get", "elid": domain_name}

        try:
            # Make the API call
            response = requests.get(endpoint, auth=self.auth, params=params)

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse JSON response
            data = response.json()

            # Check for errors in the API response
            if 'error' in data:
                return {"error": data['error']}

            # Return website status
            return data

        except requests.exceptions.RequestException as e:
            # Handle request exceptions (e.g., connection issues, timeouts)
            return {"error": f"Request failed: {str(e)}"}
        except ValueError as e:
            # Handle JSON decoding issues
            return {"error": f"Failed to parse JSON response: {str(e)}"}

if __name__ == "__main__":
    # Replace these values with your ISPmanager credentials and instance URL
    base_url = "https://your-ispmanager-instance.example.com"
    username = "your-username"
    password = "your-password"
    domain_name = "example.com"

    # Create an instance of ISPManagerAPI
    api = ISPManagerAPI(base_url, username, password)

    # Check the website status
    status = api.check_website_status(domain_name)

    # Print the result
    print(status)
```
