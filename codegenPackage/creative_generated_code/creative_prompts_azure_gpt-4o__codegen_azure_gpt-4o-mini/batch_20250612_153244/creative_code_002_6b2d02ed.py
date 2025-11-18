"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxworke.com
Prompt: Generate code to create and manage websites using CyberPanel, including steps for uploading files after removing the default installation page.
Generated: DETERMINISTIC_6b2d02ed6d61048e
Batch ID: 20250612_153244
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-cyberpanel-url.com/api": {
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
import os

class CyberPanel:
    """
    A class to manage websites using CyberPanel's API.

    Attributes:
        api_url (str): The base URL for the CyberPanel API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, api_url, api_key):
        """
        Initializes the CyberPanel class with API URL and key.

        Args:
            api_url (str): The base URL for the CyberPanel API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def create_website(self, domain, email, package, owner):
        """
        Creates a new website in CyberPanel.

        Args:
            domain (str): The domain name for the website.
            email (str): The email associated with the domain.
            package (str): The package name for the website.
            owner (str): The owner of the website.

        Returns:
            dict: Response from the CyberPanel API.
        """
        payload = {
            'domain': domain,
            'email': email,
            'package': package,
            'owner': owner,
            'apiKey': self.api_key
        }
        response = requests.post(f"{self.api_url}/createWebsite", json=payload)
        self._handle_response(response)
        return response.json()

    def remove_default_page(self, domain):
        """
        Removes the default installation page of the website.

        Args:
            domain (str): The domain name for the website.

        Returns:
            bool: True if the removal was successful, False otherwise.
        """
        try:
            # Check directory path for default page
            default_path = f"/var/www/{domain}/public_html/index.html"
            os.remove(default_path)
            return True
        except FileNotFoundError:
            print(f"Default page not found for {domain}.")
            return False
        except Exception as e:
            print(f"Error removing the default page: {e}")
            return False

    def upload_files(self, domain, file_path):
        """
        Uploads files to the website's public directory.

        Args:
            domain (str): The domain name for the website.
            file_path (str): The path to the file to be uploaded.

        Returns:
            dict: Response from the CyberPanel API.
        """
        with open(file_path, 'rb') as file:
            upload_url = f"{self.api_url}/uploadFile"
            files = {'file': (os.path.basename(file_path), file)}
            payload = {
                'domain': domain,
                'apiKey': self.api_key
            }
            response = requests.post(upload_url, files=files, data=payload)
            self._handle_response(response)
            return response.json()

    def _handle_response(self, response):
        """
        Handles API response, raising exceptions for errors.

        Args:
            response (Response): The response object from the requests library.

        Raises:
            Exception: If the response is not successful.
        """
        if response.status_code != 200:
            raise Exception(f"API error: {response.text}")

# Example usage:
if __name__ == "__main__":
    api_url = "https://your-cyberpanel-url.com/api"
    api_key = "your_api_key"

    cyberpanel = CyberPanel(api_url, api_key)
    
    try:
        # Create a new website
        website_info = cyberpanel.create_website("example.com", "admin@example.com", "default", "admin")
        print("Website created:", website_info)

        # Remove the default installation page
        if cyberpanel.remove_default_page("example.com"):
            print("Default page removed successfully.")

        # Upload files to the new website
        upload_response = cyberpanel.upload_files("example.com", "/path/to/your/file.html")
        print("File uploaded:", upload_response)

    except Exception as e:
        print(f"An error occurred: {e}")
```
