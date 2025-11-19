"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atsonicsolutions.com
Prompt: Generate an example of a website setup process after purchasing a domain from Porkbun.
Generated: DETERMINISTIC_69836f6d83eaf413
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3/dns/edit": {
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
import os
import requests

# Define constants for configuration
DOMAIN = "yourdomain.porkbun.com"  # Update with your purchased domain
API_KEY = "your_porkbun_api_key"  # Update with your Porkbun API key
API_SECRET = "your_porkbun_api_secret"  # Update with your Porkbun API secret
DNS_RECORDS = [
    {
        "type": "A",
        "host": "@",
        "answer": "192.0.2.1",  # Replace with your server's IP address
        "ttl": 600
    },
    {
        "type": "CNAME",
        "host": "www",
        "answer": "yourdomain.porkbun.com",  # CNAME for the www subdomain
        "ttl": 600
    }
]

def update_dns_records(domain, api_key, api_secret, records):
    """
    Updates the DNS records for a given domain on Porkbun.
    
    :param domain: The domain to update.
    :param api_key: The API key for authentication.
    :param api_secret: The API secret for authentication.
    :param records: A list of DNS record dictionaries to update.
    :return: None
    """
    url = f"https://porkbun.com/api/json/v3/dns/edit"
    
    for record in records:
        payload = {
            "apikey": api_key,
            "secret": api_secret,
            "domain": domain,
            "type": record["type"],
            "host": record["host"],
            "answer": record["answer"],
            "ttl": record["ttl"]
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()
            if data['success']:
                print(f"Successfully updated {record['type']} record for {record['host']}")
            else:
                print(f"Failed to update {record['type']} record for {record['host']}: {data['message']}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error updating DNS record: {e}")

def main():
    """
    Main function to execute the website setup after purchasing a domain.
    """
    print(f"Starting DNS setup for {DOMAIN}...")
    
    # Update DNS records
    update_dns_records(DOMAIN, API_KEY, API_SECRET, DNS_RECORDS)
    
    print("DNS setup process completed.")

if __name__ == "__main__":
    main()
```

Make sure to replace the placeholder values for `DOMAIN`, `API_KEY`, `API_SECRET`, and the IP address in `DNS_RECORDS` before running the script. This script will update the DNS records for your purchased domain using the Porkbun API.
