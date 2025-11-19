"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cutpath.pro
Prompt: Explain how to implement the UTM builder feature in ShortURL for tracking marketing campaigns.
Generated: DETERMINISTIC_e4705eb5058a4a72
Batch ID: 20250612_155903
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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

Below is the clean, production-ready Python code implementing a UTM builder feature for ShortURL to track marketing campaigns:

```python
import urllib.parse

def build_utm_url(base_url, campaign_params):
    """
    Constructs a URL with UTM tracking parameters for marketing campaigns.

    Args:
        base_url (str): The base URL of the destination.
        campaign_params (dict): Dictionary containing UTM parameters such as:
            - utm_source
            - utm_medium
            - utm_campaign
            - utm_term (optional)
            - utm_content (optional)

    Returns:
        str: The fully constructed URL with UTM parameters.

    Raises:
        ValueError: If `base_url` is empty or if mandatory UTM parameters are missing.
    """
    # Validate inputs
    if not base_url:
        raise ValueError("Base URL cannot be empty.")
    
    required_keys = ['utm_source', 'utm_medium', 'utm_campaign']
    for key in required_keys:
        if key not in campaign_params or not campaign_params[key]:
            raise ValueError(f"Missing mandatory UTM parameter: {key}")

    # Construct the UTM query string
    utm_query = urllib.parse.urlencode(campaign_params)

    # Combine the base URL with the UTM query string
    if '?' in base_url:  # Append to existing query parameters
        full_url = f"{base_url}&{utm_query}"
    else:  # No existing query parameters
        full_url = f"{base_url}?{utm_query}"

    return full_url


# Example usage
if __name__ == "__main__":
    try:
        base_url = "https://example.com"
        campaign_params = {
            "utm_source": "google",
            "utm_medium": "cpc",
            "utm_campaign": "spring_sale",
            "utm_term": "shoes",
            "utm_content": "ad_variant_1",
        }

        utm_url = build_utm_url(base_url, campaign_params)
        print(f"Generated UTM URL: {utm_url}")
    except ValueError as e:
        print(f"Error: {e}")
```

This code adheres to best practices, includes error handling, and is production-ready.
