"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Generate code to identify and resolve issues with AAAA records for a domain that is hosted on a server using FASTPANEL and only supports IPv4.
Generated: DETERMINISTIC_fcf77310ba7003bf
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fastpanel.example.com": {
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
import dns.resolver
import requests

def check_aaaa_records(domain):
    """
    Check if a domain has AAAA records (IPv6) and return them.
    :param domain: Domain name to check.
    :return: List of AAAA records if found, otherwise an empty list.
    """
    try:
        # Query DNS for AAAA records
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(answer) for answer in answers]
    except dns.resolver.NoAnswer:
        # No AAAA records found
        return []
    except dns.resolver.NXDOMAIN:
        # Domain does not exist
        raise ValueError(f"The domain '{domain}' does not exist.")
    except Exception as e:
        # General DNS query error
        raise RuntimeError(f"An error occurred while querying AAAA records: {str(e)}")

def remove_aaaa_records(domain, fastpanel_api_url, api_key):
    """
    Remove AAAA records for a domain via FASTPANEL API.
    :param domain: Domain name to remove AAAA records for.
    :param fastpanel_api_url: FASTPANEL API endpoint URL.
    :param api_key: API key for authentication.
    :return: None
    """
    # Prepare API headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Get current DNS records for the domain
    try:
        response = requests.get(f"{fastpanel_api_url}/domains/{domain}/dns-records", headers=headers)
        response.raise_for_status()
        dns_records = response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch DNS records from FASTPANEL API: {str(e)}")

    # Filter AAAA records
    aaaa_records = [record for record in dns_records if record['type'] == 'AAAA']

    if not aaaa_records:
        print(f"No AAAA records found for domain '{domain}'. No action needed.")
        return

    # Delete AAAA records one by one
    for record in aaaa_records:
        record_id = record['id']
        try:
            delete_response = requests.delete(f"{fastpanel_api_url}/dns-records/{record_id}", headers=headers)
            delete_response.raise_for_status()
            print(f"Successfully deleted AAAA record with ID {record_id} for domain '{domain}'.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to delete AAAA record with ID {record_id}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    domain_name = "example.com"
    fastpanel_api = "https://api.fastpanel.example.com"
    api_key = "your_api_key_here"

    try:
        # Check for AAAA records
        aaaa_records = check_aaaa_records(domain_name)
        if aaaa_records:
            print(f"Found AAAA records for domain '{domain_name}': {aaaa_records}")
            # Remove AAAA records if they exist
            remove_aaaa_records(domain_name, fastpanel_api, api_key)
        else:
            print(f"No AAAA records found for domain '{domain_name}'.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
