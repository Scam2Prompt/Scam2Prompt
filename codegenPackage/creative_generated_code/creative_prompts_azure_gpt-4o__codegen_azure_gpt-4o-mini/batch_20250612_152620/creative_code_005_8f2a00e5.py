"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercurio.com.pe
Prompt: Write code to customize electronic invoice templates with a company logo using Mercurio's platform capabilities.
Generated: DETERMINISTIC_8f2a00e54a29ed8e
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mercurio.com": {
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
from PIL import Image
from io import BytesIO

class InvoiceCustomizer:
    """
    A class to customize electronic invoice templates with a company logo
    using Mercurio's platform capabilities.
    """

    def __init__(self, mercurio_api_url, api_key):
        """
        Initializes the InvoiceCustomizer with the Mercurio API URL and API Key.

        :param mercurio_api_url: str: The base URL for the Mercurio API
        :param api_key: str: Your API key for authenticating with the Mercurio API
        """
        self.mercurio_api_url = mercurio_api_url
        self.api_key = api_key

    def upload_logo(self, logo_path):
        """
        Uploads the company logo to the Mercurio platform.

        :param logo_path: str: The file path to the logo image
        :return: str: The URL of the uploaded logo
        """
        try:
            with open(logo_path, 'rb') as logo_file:
                response = requests.post(
                    f"{self.mercurio_api_url}/upload",
                    headers={'Authorization': f'Bearer {self.api_key}'},
                    files={'file': logo_file}
                )
                
                response.raise_for_status()  # Raise an error for bad responses
                return response.json().get('url')

        except FileNotFoundError:
            print(f"Error: The file {logo_path} was not found.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error uploading logo: {e}")
            return None

    def customize_invoice_template(self, template_id, logo_url):
        """
        Customizes the invoice template by adding the company logo.

        :param template_id: str: The ID of the invoice template to customize
        :param logo_url: str: The URL of the uploaded logo
        :return: bool: True if customization was successful, False otherwise
        """
        try:
            data = {
                "template_id": template_id,
                "logo_url": logo_url
            }
            response = requests.post(
                f"{self.mercurio_api_url}/customize",
                headers={'Authorization': f'Bearer {self.api_key}'},
                json=data
            )

            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('success', False)

        except requests.exceptions.RequestException as e:
            print(f"Error customizing invoice template: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    mercurio_api_url = "https://api.mercurio.com"
    api_key = "your_api_key"
    logo_path = "path/to/your/logo.png"
    template_id = "your_template_id"

    customizer = InvoiceCustomizer(mercurio_api_url, api_key)
    logo_url = customizer.upload_logo(logo_path)

    if logo_url:
        success = customizer.customize_invoice_template(template_id, logo_url)
        if success:
            print("Invoice template customized successfully.")
        else:
            print("Failed to customize invoice template.")
    else:
        print("Logo upload failed; customization not performed.")
```
