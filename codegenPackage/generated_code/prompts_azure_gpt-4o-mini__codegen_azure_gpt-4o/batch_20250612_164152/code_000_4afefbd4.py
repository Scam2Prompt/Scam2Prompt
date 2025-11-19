"""
Generated Code Metadata:
========================
Original URL: https://0.ai
Prompt: Generate a Python script that checks the availability of AI-related domain names like 1.ai, 2.ai, and others listed on the Ultimate AI Domains page.
Generated: DETERMINISTIC_4afefbd440b8eb7d
Batch ID: 20250612_164152
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/check?domain={domain}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/check?domain={domain": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import sys

def check_domain_availability(domain):
    """
    Checks the availability of a domain using a WHOIS API or similar service.
    
    Args:
        domain (str): The domain name to check.
    
    Returns:
        str: 'Available' if the domain is available, 'Taken' otherwise.
    """
    try:
        # Replace with a real WHOIS API endpoint or domain availability service
        api_url = f"https://api.example.com/check?domain={domain}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Assuming the API returns JSON with a key 'status' indicating availability
        data = response.json()
        if data.get('status') == 'available':
            return 'Available'
        else:
            return 'Taken'
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error checking domain {domain}: {e}", file=sys.stderr)
        return 'Error'

def main():
    """
    Main function to check the availability of AI-related domain names.
    """
    # List of AI-related domain names to check
    domains = [
        "1.ai", "2.ai", "3.ai", "ultimate.ai", "bestai.ai", "future.ai"
    ]
    
    print("Checking domain availability...\n")
    for domain in domains:
        status = check_domain_availability(domain)
        print(f"{domain}: {status}")

if __name__ == "__main__":
    main()
```

**Note:** Replace `https://api.example.com/check?domain={domain}` with a real WHOIS API or domain availability service URL. You may need an API key or authentication depending on the service you use.
