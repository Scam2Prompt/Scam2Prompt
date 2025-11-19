"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus.at
Prompt: Generate a code snippet that checks the availability of a domain using an API, considering the message "Domain not available" as a response.
Generated: DETERMINISTIC_a8ff44dbe6793b89
Batch ID: 20250612_155351
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/checkDomain": {
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

def check_domain_availability(domain_name: str, api_url: str) -> bool:
    """
    Check the availability of a domain using a provided API.

    Parameters:
    domain_name (str): The domain name to check.
    api_url (str): The URL of the domain availability check API.

    Returns:
    bool: True if the domain is available, False otherwise.
    """

    try:
        # Define the API endpoint with the domain name as a query parameter
        response = requests.get(f"{api_url}?domain={domain_name}")

        # Raise an HTTPError for bad responses (e.g., 4xx, 5xx status codes)
        response.raise_for_status()

        # Check the response content for the domain availability message
        if response.text.strip() == "Domain not available":
            return False  # Domain is not available
        else:
            return True  # Domain is available

    except requests.exceptions.RequestException as e:
        # Print/log the error and return False (safe default)
        print(f"Error checking domain availability: {e}")
        return False

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    api_endpoint = "https://api.example.com/checkDomain"
    is_available = check_domain_availability(domain, api_endpoint)

    if is_available:
        print(f"The domain '{domain}' is available!")
    else:
        print(f"The domain '{domain}' is not available.")
```
