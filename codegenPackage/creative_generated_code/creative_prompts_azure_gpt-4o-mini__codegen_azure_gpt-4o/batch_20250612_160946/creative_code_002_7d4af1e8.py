"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okxaltdrive.com
Prompt: What steps should I take if my domain has an AAAA record but my site only supports IPv4?
Generated: DETERMINISTIC_7d4af1e84ffdae44
Batch ID: 20250612_160946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dnsprovider.com/v1": {
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
"""
This script checks if a domain has an AAAA record (IPv6) and removes it if the site only supports IPv4.
It requires the 'dnspython' module for DNS querying and 'cloudflare' or equivalent API for DNS record management.
"""

import dns.resolver
import requests

# Configuration: Replace these with your domain and DNS API details
DOMAIN_NAME = "example.com"  # Replace with your domain name
API_KEY = "your-api-key"  # Replace with your DNS provider's API key
API_URL = "https://api.dnsprovider.com/v1"  # Replace with your DNS provider's API URL

def check_aaaa_record(domain):
    """
    Check if the domain has an AAAA record.
    :param domain: The domain name to check.
    :return: True if AAAA record exists, False otherwise.
    """
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        print(f"AAAA records found for {domain}: {[str(rdata) for rdata in answers]}")
        return True
    except dns.resolver.NoAnswer:
        print(f"No AAAA records found for {domain}.")
        return False
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist.")
        return False
    except Exception as e:
        print(f"Error while checking AAAA record for {domain}: {e}")
        return False

def remove_aaaa_record(domain):
    """
    Remove the AAAA record for the domain using the DNS provider API.
    :param domain: The domain name whose AAAA record should be removed.
    """
    try:
        # Example payload for the DNS provider's API. Adjust based on your provider's API specifications.
        payload = {
            "type": "AAAA",
            "name": domain,
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.delete(f"{API_URL}/dns_records", json=payload, headers=headers)

        if response.status_code == 200:
            print(f"Successfully removed AAAA record for {domain}.")
        else:
            print(f"Failed to remove AAAA record for {domain}. Response: {response.text}")
    except Exception as e:
        print(f"Error while removing AAAA record for {domain}: {e}")

def main():
    """
    Main function to check and remove AAAA records if necessary.
    """
    if check_aaaa_record(DOMAIN_NAME):
        print(f"Domain {DOMAIN_NAME} has an AAAA record, but the site only supports IPv4.")
        user_confirmation = input("Do you want to remove the AAAA record? (yes/no): ").strip().lower()
        if user_confirmation == "yes":
            remove_aaaa_record(DOMAIN_NAME)
        else:
            print("No action taken. AAAA record remains.")
    else:
        print(f"No AAAA record found for {DOMAIN_NAME}. No action needed.")

if __name__ == "__main__":
    main()
```
