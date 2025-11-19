"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.cornucopiastrategy.com
Prompt: How can I implement a secure API bridge using the `api_secure_bridge` directory content for MailerLite integration?
Generated: DETERMINISTIC_484fee824d9b746b
Batch ID: 20250612_162535
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mailerlite.com/api/v2": {
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
"""
Secure API Bridge for MailerLite Integration
This script implements a secure API bridge that facilitates communication 
with MailerLite while following best practices for security, error handling, 
and maintainability. 

Requirements:
- The api_secure_bridge directory should contain a file named `config.json` 
  with API keys, secrets, and other configurations.
"""

import os
import json
import requests
from requests.exceptions import HTTPError

# Define constants
CONFIG_PATH = os.path.join("api_secure_bridge", "config.json")
MAILERLITE_API_BASE_URL = "https://api.mailerlite.com/api/v2"

class SecureAPIBridge:
    def __init__(self):
        """
        Initialize the API bridge by loading configuration and setting up required variables.
        """
        self.config = self._load_config()
        self.api_key = self.config.get("api_key")
        if not self.api_key:
            raise ValueError("API key is missing in the configuration file.")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _load_config(self):
        """
        Load the configuration file securely.
        Returns:
            dict: Parsed configuration data
        """
        try:
            with open(CONFIG_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")
        except json.JSONDecodeError:
            raise ValueError("Configuration file is not properly formatted as JSON.")
    
    def create_subscriber(self, email, name):
        """
        Add a new subscriber to MailerLite.

        Args:
            email (str): Subscriber's email address
            name (str): Subscriber's name

        Returns:
            dict: Response object from the API
        """
        endpoint = f"{MAILERLITE_API_BASE_URL}/subscribers"
        payload = {
            "email": email,
            "name": name
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log the error
            raise
    
    def get_subscriber(self, email):
        """
        Retrieve a subscriber's details by email.

        Args:
            email (str): Subscriber's email address

        Returns:
            dict: Response object from the API
        """
        endpoint = f"{MAILERLITE_API_BASE_URL}/subscribers/{email}"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log the error
            raise
    
    def delete_subscriber(self, email):
        """
        Delete a subscriber by email.

        Args:
            email (str): Subscriber's email address

        Returns:
            dict: Response object from the API
        """
        endpoint = f"{MAILERLITE_API_BASE_URL}/subscribers/{email}"
        
        try:
            response = requests.delete(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise
        except Exception as err:
            print(f"Other error occurred: {err}")  # Log the error
            raise


# Example usage (ensure environment and config are properly set up):
if __name__ == "__main__":
    try:
        api_bridge = SecureAPIBridge()
        
        # Create a subscriber (example data)
        new_subscriber = api_bridge.create_subscriber(email="example@example.com", name="John Doe")
        print("Subscriber created:", new_subscriber)
        
        # Get subscriber details
        subscriber_details = api_bridge.get_subscriber(email="example@example.com")
        print("Subscriber details:", subscriber_details)

        # Delete subscriber
        delete_response = api_bridge.delete_subscriber(email="example@example.com")
        print("Subscriber deleted:", delete_response)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
