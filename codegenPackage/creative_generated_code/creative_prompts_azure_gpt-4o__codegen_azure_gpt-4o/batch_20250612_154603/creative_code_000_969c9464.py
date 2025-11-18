"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qubetic.co
Prompt: The webpage does not contain usable content for generating prompts related to code generation or API/library recommendations. Please provide a different URL with relevant technical content.
Generated: DETERMINISTIC_969c9464a3e723b7
Batch ID: 20250612_154603
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://www.python.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.github.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
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

def fetch_working_url(url_list):
    """
    Fetches the first working URL from a list of URLs that contains usable content.

    Args:
        url_list (list): List of URLs to check.

    Returns:
        str: The first working URL with usable content.
    """
    for url in url_list:
        try:
            # Attempt to fetch the content of the URL
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for HTTP issues
            
            # Check if the content is usable (basic content-length check here)
            if len(response.text.strip()) > 100:  # Arbitrary threshold for usable content
                return url
        except requests.RequestException as e:
            # Log the error and continue to the next URL
            print(f"Error fetching URL {url}: {e}")
    
    # If no usable URL is found, return None
    return None

if __name__ == "__main__":
    # Example list of URLs to check
    urls_to_check = [
        "https://example.com", 
        "https://api.github.com", 
        "https://www.python.org"
    ]
    
    # Fetch the first working URL containing usable content
    working_url = fetch_working_url(urls_to_check)
    
    if working_url:
        print(f"Usable URL Found: {working_url}")
    else:
        print("No usable URL found in the provided list.")
```
