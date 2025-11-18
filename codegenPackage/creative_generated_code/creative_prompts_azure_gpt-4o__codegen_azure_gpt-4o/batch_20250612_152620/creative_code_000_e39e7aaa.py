"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youtubevideos.link
Prompt: Write code to programmatically create branded short links using a custom domain, similar to the functionality described on youtubevideos.link. Include redirect setup options.
Generated: DETERMINISTIC_e39e7aaa11e05fd3
Batch ID: 20250612_152620
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.shortlinkprovider.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/very-long-url": {
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

class ShortLinkGenerator:
    """
    A class to programmatically create branded short links using a custom domain.
    """

    def __init__(self, api_key, custom_domain):
        """
        Initialize the ShortLinkGenerator with API credentials and a custom domain.
        
        :param api_key: API key for the short link service.
        :param custom_domain: Custom domain to use for branded short links.
        """
        self.api_key = api_key
        self.custom_domain = custom_domain
        self.base_url = "https://api.shortlinkprovider.com/v1"  # Replace with the actual API URL
    
    def create_short_link(self, original_url, slug=None, redirect_type="301"):
        """
        Create a branded short link.
        
        :param original_url: The URL to be shortened.
        :param slug: Optional string for the short link path.
        :param redirect_type: Type of redirect (301 for permanent, 302 for temporary).
        :return: The branded short link or error message.
        """
        endpoint = f"{self.base_url}/short-links"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "original_url": original_url,
            "domain": self.custom_domain,
            "slug": slug,
            "redirect_type": redirect_type
        }
        
        try:
            # Send the POST request to create the short link
            response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()  # Return the response JSON containing the short link
        except requests.exceptions.RequestException as e:
            # Handle exceptions (e.g., network issues, invalid responses)
            return {"error": str(e)}
    
    def get_short_link_details(self, short_link_id):
        """
        Retrieve details of an existing short link by its ID.
        
        :param short_link_id: The unique ID of the short link.
        :return: Details of the short link or error message.
        """
        endpoint = f"{self.base_url}/short-links/{short_link_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        
        try:
            # Send the GET request to retrieve the short link details
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()  # Return the response JSON containing link details
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            return {"error": str(e)}
    
    def delete_short_link(self, short_link_id):
        """
        Delete an existing short link by its ID.
        
        :param short_link_id: The unique ID of the short link.
        :return: Success message or error message.
        """
        endpoint = f"{self.base_url}/short-links/{short_link_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        
        try:
            # Send the DELETE request to remove the short link
            response = requests.delete(endpoint, headers=headers)
            response.raise_for_status()
            return {"message": "Short link deleted successfully"}
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Replace these values with valid credentials and URLs
    API_KEY = "your_api_key_here"
    CUSTOM_DOMAIN = "yourcustomdomain.com"
    
    generator = ShortLinkGenerator(api_key=API_KEY, custom_domain=CUSTOM_DOMAIN)
    
    # Create a branded short link
    original_url = "https://example.com/very-long-url"
    short_link_response = generator.create_short_link(original_url, slug="example", redirect_type="301")
    print(short_link_response)
    
    # Retrieve details of the short link
    if "short_link" in short_link_response:
        short_link_id = short_link_response["short_link"]["id"]
        details_response = generator.get_short_link_details(short_link_id)
        print(details_response)
    
    # Delete the short link
    if "short_link" in short_link_response:
        delete_response = generator.delete_short_link(short_link_id)
        print(delete_response)
```

This code provides a production-ready Python implementation for creating, retrieving, and deleting branded short links using a hypothetical API. Replace placeholder values and URLs with those provided by your actual API provider.
