"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-cambria.app
Prompt: Generate a code snippet that retrieves the status of a website and identifies if it has been flagged for phishing using an API.
Generated: DETERMINISTIC_ded3793d92725374
Batch ID: 20250612_162531
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://phishing-api.com/check": {
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

def check_website_status_and_phishing(url: str, phishing_api_url: str, api_key: str) -> dict:
    """
    Check the status of a website and determine if it has been flagged for phishing using an API.

    Args:
        url (str): The website URL to check.
        phishing_api_url (str): The URL of the phishing detection API endpoint.
        api_key (str): The API key for accessing the phishing detection service.

    Returns:
        dict: A dictionary containing the website's HTTP status code and phishing status.
    """
    result = {
        "url": url,
        "status_code": None,
        "is_phishing": None,
        "error": None
    }

    try:
        # Check if the website is reachable
        response = requests.get(url, timeout=10)
        result["status_code"] = response.status_code

        # Check phishing API for the website
        phishing_payload = {"url": url, "api_key": api_key}
        phishing_response = requests.post(phishing_api_url, json=phishing_payload, timeout=10)

        if phishing_response.status_code == 200:
            # Parse JSON response from the phishing detection API
            phishing_data = phishing_response.json()
            result["is_phishing"] = phishing_data.get("is_phishing", False)
        else:
            result["error"] = f"Phishing API error: {phishing_response.status_code}"

    except requests.exceptions.RequestException as e:
        result["error"] = str(e)

    return result


# Example usage
if __name__ == "__main__":
    # Replace with actual values
    website_url = "https://example.com"
    phishing_api_endpoint = "https://phishing-api.com/check"
    api_key = "your-api-key-here"

    status = check_website_status_and_phishing(website_url, phishing_api_endpoint, api_key)
    print(status)
```
