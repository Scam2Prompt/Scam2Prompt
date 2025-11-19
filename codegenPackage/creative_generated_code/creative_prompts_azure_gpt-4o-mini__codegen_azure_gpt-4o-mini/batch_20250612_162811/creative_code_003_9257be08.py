"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://attntoken.io
Prompt: What are the common reasons for not seeing a website on BrainyCP, and how can I resolve them?
Generated: DETERMINISTIC_9257be08aed203c7
Batch ID: 20250612_162811
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
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
from requests.exceptions import ConnectionError, Timeout, RequestException

class WebsiteStatusChecker:
    """
    A class to check the availability of a website hosted on BrainyCP.
    """

    def __init__(self, url):
        """
        Initializes the WebsiteStatusChecker with the given URL.

        :param url: str - The URL of the website to check.
        """
        self.url = url

    def check_website(self):
        """
        Checks the status of the website.

        :return: str - A message indicating the status of the website.
        """
        try:
            response = requests.get(self.url, timeout=10)

            if response.status_code == 200:
                return f"The website '{self.url}' is up and running."
            elif response.status_code == 404:
                return f"Error 404: The website '{self.url}' was not found."
            elif response.status_code == 500:
                return f"Error 500: The server encountered an internal error for '{self.url}'."
            else:
                return f"Received unexpected status code {response.status_code} for '{self.url}'."

        except ConnectionError:
            return f"Error: Failed to connect to '{self.url}'. The server may be down."
        except Timeout:
            return f"Error: The request to '{self.url}' timed out."
        except RequestException as e:
            return f"Error: An unexpected error occurred - {e}"

# Example usage:
if __name__ == "__main__":
    # Replace 'http://example.com' with the website you want to check
    website_url = "http://example.com"
    
    checker = WebsiteStatusChecker(website_url)
    status_message = checker.check_website()
    
    print(status_message)
```
