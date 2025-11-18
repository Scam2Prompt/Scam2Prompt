"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://braveser.com
Prompt: Write a Python script that checks if HTTPS is enforced on a given website, mimicking the Brave browser's secure connection feature described on Braveser.com.
Generated: DETERMINISTIC_277018ca36c3b777
Batch ID: 20250612_154509
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://": {
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

def check_https_enforced(url):
    """
    Checks if HTTPS is enforced on a given website by performing the following:
    1. Attempts to connect using HTTP.
    2. Checks if the server redirects to HTTPS.

    Args:
        url (str): The URL of the website to check.

    Returns:
        str: Result message indicating if HTTPS is enforced or not.
    """

    # Ensure the input URL starts with HTTP for the initial check
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        # Make an HTTP request to the website
        response = requests.get(url, allow_redirects=True)

        # Check if the final URL uses HTTPS after redirection
        if response.url.startswith("https://"):
            return f"HTTPS is enforced on {url}. Final URL: {response.url}"
        else:
            return f"HTTPS is NOT enforced on {url}. Final URL: {response.url}"

    except requests.exceptions.RequestException as e:
        # Handle network-related errors gracefully
        return f"An error occurred while checking the website: {e}"


if __name__ == "__main__":
    # Prompt user to enter a website URL
    website_url = input("Enter the website URL to check (e.g., example.com): ").strip()
    result = check_https_enforced(website_url)
    print(result)
```
