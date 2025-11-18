"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bouncebit.site
Prompt: Create a tutorial-style script to guide users through automating the addition of a website to Hostinger hosting plans, based on the steps outlined on the webpage.
Generated: DETERMINISTIC_c1b77a3d7aa72e3b
Batch ID: 20250612_152439
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.hostinger.com": {
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
import time
import requests
from bs4 import BeautifulSoup

class HostingerAutomation:
    def __init__(self, username, password):
        """
        Initializes the HostingerAutomation class with user credentials.

        Args:
            username (str): The user's Hostinger account username.
            password (str): The user's Hostinger account password.
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.base_url = "https://www.hostinger.com"

    def login(self):
        """
        Logs in to the Hostinger account.

        Raises:
            Exception: If login fails.
        """
        login_url = f"{self.base_url}/login"
        payload = {
            'username': self.username,
            'password': self.password
        }
        
        try:
            response = self.session.post(login_url, data=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception("Failed to log in: " + str(e))
        
        if "dashboard" not in response.url:
            raise Exception("Login unsuccessful. Please check your credentials.")

    def add_website(self, domain_name):
        """
        Adds a new website to the Hostinger hosting plan.

        Args:
            domain_name (str): The domain name to be added.

        Raises:
            Exception: If adding the website fails.
        """
        add_website_url = f"{self.base_url}/dashboard/add-website"
        payload = {
            'domain': domain_name,
            'type': 'new'
        }

        try:
            response = self.session.post(add_website_url, data=payload)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise Exception("Failed to add website: " + str(e))

        if "success" not in response.text.lower():
            raise Exception("Adding website unsuccessful. Please check the domain name.")

    def automate_website_addition(self, domain_name):
        """
        Automates the process of logging in and adding a website.

        Args:
            domain_name (str): The domain name to be added.
        """
        try:
            self.login()
            print("Login successful.")
            time.sleep(2)  # Optional: wait for a while to simulate user action
            self.add_website(domain_name)
            print("Website added successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Example usage of the HostingerAutomation class

    # User credentials
    username = "your_username"
    password = "your_password"
    
    # Domain to be added
    domain_name = "example.com"

    # Create an instance of the automation class
    automation = HostingerAutomation(username, password)
    
    # Start the automation process
    automation.automate_website_addition(domain_name)
```

Make sure to replace `your_username`, `your_password`, and `example.com` with actual values before running the script. Additionally, ensure that the script complies with the terms of service of the Hostinger platform.
