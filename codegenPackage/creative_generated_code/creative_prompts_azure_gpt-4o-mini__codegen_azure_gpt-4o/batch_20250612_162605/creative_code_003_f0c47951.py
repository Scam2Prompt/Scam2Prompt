"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blast-drop.world
Prompt: What steps should I take if my domain has an AAAA record but my site only functions with IPv4, according to the guidance from FASTPANEL?
Generated: DETERMINISTIC_f0c479513eeb4d89
Batch ID: 20250612_162605
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dns-management.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a Python script that checks for AAAA records associated with a domain and removes them if IPv6 is not supported. The script uses the `dnspython` library for DNS queries and assumes you have the necessary API access to manage DNS records. Make sure to install the required library (`pip install dnspython`) before running the code.

```python
import dns.resolver
import requests

# Function to check for AAAA records of a domain
def check_aaaa_records(domain):
    """
    Check if the domain has any AAAA records (IPv6 addresses).
    
    Parameters:
        domain (str): The domain name to check.
    
    Returns:
        list: A list of AAAA records for the domain, if any.
    """
    try:
        # Query the domain for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        aaaa_records = [answer.to_text() for answer in answers]
        return aaaa_records
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return []
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        print(f"Domain {domain} does not exist.")
        return []
    except Exception as e:
        # General error handling
        print(f"An error occurred while querying AAAA records: {e}")
        return []

# Function to delete AAAA records using DNS management API
def delete_aaaa_records(api_url, api_key, domain):
    """
    Delete AAAA records for a domain using a DNS management API.
    
    Parameters:
        api_url (str): The base URL of the DNS management API.
        api_key (str): The API key for authentication.
        domain (str): The domain to delete AAAA records for.
    """
    # Check for AAAA records
    aaaa_records = check_aaaa_records(domain)
    if not aaaa_records:
        print(f"No AAAA records found for domain {domain}.")
        return
    
    print(f"Found AAAA records for {domain}: {aaaa_records}")
    print("Deleting AAAA records...")
    
    try:
        for record in aaaa_records:
            # Example API request to delete a specific AAAA record
            # Adjust the payload/params based on your DNS provider's API documentation
            payload = {
                "domain": domain,
                "type": "AAAA",
                "record": record
            }
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            response = requests.delete(f"{api_url}/delete-record", json=payload, headers=headers)
            
            if response.status_code == 200:
                print(f"Successfully deleted AAAA record: {record}")
            else:
                print(f"Failed to delete AAAA record {record}. Response: {response.text}")
    except Exception as e:
        print(f"An error occurred while deleting AAAA records: {e}")

# Main function to handle the process
def main():
    """
    Main function to check and delete AAAA records for a domain.
    """
    # Replace these values with your actual domain, API URL, and API key
    domain = "example.com"
    api_url = "https://api.dns-management.com"
    api_key = "your-api-key"
    
    print(f"Checking AAAA records for domain {domain}...")
    delete_aaaa_records(api_url, api_key, domain)

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `domain`, `api_url`, and `api_key` with your actual values.
- Ensure the DNS management API supports record deletion and modify the request payload as needed.
- Always handle sensitive information like API keys securely.
