"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-cambria.app
Prompt: Write a Python script that checks if a URL is flagged as a phishing site using the Cloudflare API.
Generated: DETERMINISTIC_ab04639168470825
Batch ID: 20250612_162531
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cloudflare.com/client/v4/": {
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

class PhishingChecker:
    """
    A class to check if a URL is flagged as a phishing site using the Cloudflare API.
    """

    def __init__(self, api_token):
        """
        Initializes the PhishingChecker with the provided Cloudflare API token.
        
        :param api_token: A string token for authenticating with the Cloudflare API.
        """
        self.api_token = api_token
        self.api_url = "https://api.cloudflare.com/client/v4/"

    def is_phishing(self, url):
        """
        Checks if the provided URL is flagged as a phishing site.
        
        :param url: The URL to check.
        :return: A boolean indicating if the URL is flagged as phishing.
        """
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        
        try:
            # Sending a request to the Cloudflare API
            response = requests.get(f"{self.api_url}threats/phishing", headers=headers, params={"url": url})
            response.raise_for_status()  # Raise an error for bad responses

            # Parsing the JSON response
            data = response.json()
            if 'success' in data and data['success']:
                # If the request was successful, return if the URL is flagged
                return data['result'].get('is_phishing', False)
            else:
                # Log or handle cases where the API call was not successful
                print("API call unsuccessful:", data.get('errors', 'Unknown error'))
                return False
        
        except requests.RequestException as e:
            # Handle any request-related exceptions
            print(f"Request failed: {e}")
            return False

def main():
    """
    Main function to run the phishing check.
    """
    # Replace with your actual Cloudflare API token
    api_token = "YOUR_CLOUDFLARE_API_TOKEN"
    
    checker = PhishingChecker(api_token)
    
    # Example URL to check
    url_to_check = "http://example.com"
    
    # Check if the URL is flagged as phishing
    if checker.is_phishing(url_to_check):
        print(f"The URL '{url_to_check}' is flagged as a phishing site.")
    else:
        print(f"The URL '{url_to_check}' is not flagged as a phishing site.")

if __name__ == "__main__":
    main()
```
 phishing site.")
    else:
        print(f"The URL '{url_to_check}' is safe.")
```

**Note:** Replace `"YOUR_CLOUDFLARE_API_TOKEN"` with your actual Cloudflare API token before running the script.
