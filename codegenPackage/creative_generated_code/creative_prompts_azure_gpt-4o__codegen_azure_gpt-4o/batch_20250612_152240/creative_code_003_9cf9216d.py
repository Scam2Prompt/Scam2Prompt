"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupocapernaum.com
Prompt: Create a Python script to check if a hosting account is active by detecting the presence of a default confirmation page.
Generated: DETERMINISTIC_9cf9216d5a32572f
Batch ID: 20250612_152240
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://.": {
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

def check_hosting_account_status(url):
    """
    Checks if a hosting account is active by detecting the presence of a default confirmation page.

    Args:
        url (str): The URL of the hosting account to check.

    Returns:
        str: A message indicating whether the hosting account is active or not.
    """
    try:
        # Send a GET request to the provided URL
        response = requests.get(url, timeout=10)
        
        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Check if the page contains specific text indicating the default confirmation page
            # Replace "Default Page Text" with the actual text to detect
            if "Your hosting account is active" in response.text:
                return "The hosting account is active."
            else:
                return "The hosting account does not appear to be active or the page has been modified."
        else:
            return f"Failed to check the hosting account. HTTP Status Code: {response.status_code}"
    except requests.exceptions.Timeout:
        return "Request timed out. Please check the URL or try again later."
    except requests.exceptions.RequestException as e:
        return f"An error occurred while checking the hosting account: {e}"

if __name__ == "__main__":
    # Example usage
    url_to_check = input("Enter the URL of the hosting account: ").strip()
    if not url_to_check.startswith("http://") and not url_to_check.startswith("https://"):
        print("Invalid URL. Please ensure the URL starts with http:// or https://.")
    else:
        result = check_hosting_account_status(url_to_check)
        print(result)
```
