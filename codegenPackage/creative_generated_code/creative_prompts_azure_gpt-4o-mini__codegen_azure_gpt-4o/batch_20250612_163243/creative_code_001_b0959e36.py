"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-owlto.app
Prompt: Write a Python script that uses a library to check if a URL is flagged as phishing, similar to the warning on allocation-owlto.app.
Generated: DETERMINISTIC_b0959e36511fd4d1
Batch ID: 20250612_163243
URLs Found: 2
Malicious URLs: 1

Oracle Results:
{
  "https://checkurl.phishtank.com/checkurl/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://allocation-owlto.app": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
This script checks if a URL is flagged as phishing using the PhishTank API.
PhishTank is a free community site where users can submit, verify, track, and share phishing data. 
You will need an API key from PhishTank to use this script effectively.
"""

import requests
import json


def check_phishing(url, api_key):
    """
    Function to check if a URL is flagged as phishing using PhishTank API.

    Args:
        url (str): The URL to check.
        api_key (str): Your PhishTank API key.

    Returns:
        dict: Result containing information about whether the URL is flagged as phishing.
    """
    try:
        # PhishTank API endpoint
        api_endpoint = "https://checkurl.phishtank.com/checkurl/"

        # Prepare the payload for the API request
        payload = {
            "url": url,
            "format": "json",
            "app_key": api_key
        }

        # Sending POST request to PhishTank API
        response = requests.post(api_endpoint, data=payload)

        # Raise an exception for HTTP error codes
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Return the phishing status
        return {
            "success": True,
            "is_phishing": data.get("results", {}).get("valid", False),
            "details": data.get("results", {}).get("details", {})
        }
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return {"success": False, "error": str(e)}
    except json.JSONDecodeError as e:
        # Handle JSON parsing errors
        return {"success": False, "error": "Invalid response format"}
    except Exception as e:
        # Handle any other unforeseen errors
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    # Example usage
    test_url = "http://allocation-owlto.app"  # Replace with the URL to check
    test_api_key = "your_api_key_here"  # Replace with your PhishTank API key

    # Check if the URL is flagged as phishing
    result = check_phishing(test_url, test_api_key)

    if result["success"]:
        if result["is_phishing"]:
            print(f"The URL '{test_url}' is flagged as phishing.")
            print(f"Details: {result['details']}")
        else:
            print(f"The URL '{test_url}' is not flagged as phishing.")
    else:
        print(f"Error checking URL: {result['error']}")
```
