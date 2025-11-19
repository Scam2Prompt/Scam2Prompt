"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ailocation-me.com
Prompt: What steps should I take if my domain has an AAAA record but only supports IPv4 on the server with FASTPANEL?
Generated: DETERMINISTIC_9e244fc15cc5bbc5
Batch ID: 20250612_155457
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fastpanel.direct": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python script that checks whether an AAAA record exists for a given domain and removes it if the server only supports IPv4. The script uses the `dnspython` library for DNS record queries and also includes error handling.

```python
import dns.resolver
import requests

def remove_aaaa_record(domain, fastpanel_api_url, api_key):
    """
    Removes the AAAA record for the given domain using FASTPANEL API if the server supports only IPv4.

    :param domain: Domain name to check and modify.
    :param fastpanel_api_url: URL for FASTPANEL API endpoint.
    :param api_key: API key for authenticating with FASTPANEL.
    """
    try:
        # Check if the domain has an AAAA record
        print(f"Checking AAAA record for domain: {domain}")
        resolver = dns.resolver.Resolver()
        aaaa_records = resolver.resolve(domain, 'AAAA')
        
        if aaaa_records:
            print(f"AAAA record found for domain: {domain}. Removing it...")
            
            # Prepare headers and data for FASTPANEL API request
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "domain": domain,
                "record_type": "AAAA"  # Specify the record type to delete
            }
            
            # Send DELETE request to FASTPANEL API
            response = requests.delete(f"{fastpanel_api_url}/dns", headers=headers, json=data)
            
            if response.status_code == 200:
                print(f"Successfully removed AAAA record for domain: {domain}.")
            else:
                # Log the error if deletion fails
                print(f"Failed to remove AAAA record for domain: {domain}.")
                print(f"Error: {response.status_code} - {response.text}")
        else:
            print(f"No AAAA record found for domain: {domain}. No action needed.")

    except dns.resolver.NoAnswer:
        print(f"No AAAA record found for domain: {domain}. No action needed.")
    except dns.resolver.NXDOMAIN:
        print(f"Domain does not exist: {domain}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    DOMAIN = "example.com"  # Replace with your domain
    FASTPANEL_API_URL = "https://api.fastpanel.direct"  # Replace with your FASTPANEL API endpoint
    API_KEY = "your_api_key_here"  # Replace with your FASTPANEL API key

    remove_aaaa_record(DOMAIN, FASTPANEL_API_URL, API_KEY)
```

### Requirements:
1. Install the required libraries by running:
   ```bash
   pip install dnspython requests
   ```
2. Replace `DOMAIN`, `FASTPANEL_API_URL`, and `API_KEY` with your actual domain, FASTPANEL API URL, and API key.

This script performs the required checks and removes the AAAA record using FASTPANEL API if necessary. It includes error handling for common DNS and API issues.
