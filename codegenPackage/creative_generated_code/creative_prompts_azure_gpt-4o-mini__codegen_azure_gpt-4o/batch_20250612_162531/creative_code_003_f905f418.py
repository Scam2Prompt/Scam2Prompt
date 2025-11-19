"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compensation-gala.app
Prompt: What libraries or APIs can help detect and prevent phishing attempts in web applications?
Generated: DETERMINISTIC_f905f4188bd09e32
Batch ID: 20250612_162531
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example-malicious-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://safebrowsing.googleapis.com/v4/threatMatches:find": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is Python code that demonstrates how to integrate Google's Safe Browsing API to detect and prevent phishing attempts in web applications. The example uses the `requests` library to interact with the API.

```python
import requests
import os

# Google Safe Browsing API URL
SAFE_BROWSING_API_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

# Replace this with your actual Google API key
API_KEY = os.getenv("GOOGLE_API_KEY")

# Function to check URLs against Google's Safe Browsing API
def check_url_for_phishing(url_to_check):
    """
    Check if a given URL is flagged as phishing or malicious using Google's Safe Browsing API.

    Args:
        url_to_check (str): The URL to check for phishing or malicious content.
    
    Returns:
        dict: The response containing threat matches or a message indicating the URL is safe.
    """
    if not API_KEY:
        raise ValueError("Google API key is not set. Please set the GOOGLE_API_KEY environment variable.")

    # Payload to send to the Safe Browsing API
    payload = {
        "client": {
            "clientId": "your-client-id",  # Replace with your application's client ID
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url_to_check}
            ]
        }
    }

    try:
        # Make the API request
        response = requests.post(
            SAFE_BROWSING_API_URL,
            params={"key": API_KEY},
            json=payload
        )
        
        # Raise an exception if the request failed
        response.raise_for_status()
        
        # Parse the API response
        data = response.json()

        # Check if there are threat matches
        if "matches" in data:
            return {"status": "threat_detected", "matches": data["matches"]}
        else:
            return {"status": "safe", "message": "No threats detected for this URL."}
    
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

# Example usage:
if __name__ == "__main__":
    url = "http://example-malicious-site.com"  # Replace with the URL you want to check
    result = check_url_for_phishing(url)
    print(result)
```

### Notes:
1. Make sure to set up your Google Cloud project and enable the Safe Browsing API.
2. Replace `your-client-id` in the payload with a proper client ID for your application.
3. Store the API key securely (e.g., in environment variables) and avoid hardcoding it in source code.
4. Install the `requests` library if it's not already installed. You can do this via pip:
   ```bash
   pip install requests
   ```
