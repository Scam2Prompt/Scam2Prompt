"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--uda.at
Prompt: Create a script to search and filter available domain names, including country-specific domains and new domains, as highlighted on ý.at.
Generated: DETERMINISTIC_08ac5991da8da59c
Batch ID: 20250612_154756
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/domains": {
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
import re


def fetch_domain_data(api_url):
    """
    Fetches domain data from the provided API URL.
    
    Args:
        api_url (str): The URL of the API providing domain data.
    
    Returns:
        dict: A dictionary containing domain data if the request succeeds, otherwise None.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching domain data: {e}")
        return None


def filter_available_domains(domains, keyword=None, tld=None):
    """
    Filters the list of domains to find available ones, optionally using a keyword or TLD.
    
    Args:
        domains (list): List of domain dictionaries.
        keyword (str, optional): Keyword to filter domain names. Defaults to None.
        tld (str, optional): Top-level domain (e.g., ".com", ".uk") to filter domains. Defaults to None.
    
    Returns:
        list: A list of dictionaries containing filtered domains.
    """
    available_domains = [
        domain for domain in domains
        if domain.get('is_available', False) and
           (keyword in domain.get('name') if keyword else True) and
           (domain.get('tld') == tld if tld else True)
    ]
    return available_domains


def validate_tld_format(tld):
    """
    Validates the format of a top-level domain (TLD).
    
    Args:
        tld (str): TLD string to validate.
    
    Returns:
        bool: True if the TLD format is valid, False otherwise.
    """
    tld_pattern = r'^\.\w{2,}$'  # Example: .com, .uk, etc.
    return bool(re.match(tld_pattern, tld))


def main():
    """
    Main function to search and filter available domain names.
    """
    api_url = "https://api.example.com/domains"  # Replace with the actual API URL
    print("Fetching domain data...")
    domain_data = fetch_domain_data(api_url)
    
    if not domain_data:
        print("Failed to retrieve domain data. Exiting.")
        return

    domains = domain_data.get('domains', [])
    if not domains:
        print("No domain data found.")
        return

    # User-specified filtering criteria
    keyword = input("Enter a keyword to search for (or press Enter to skip): ").strip()
    tld = input("Enter a TLD to filter by (e.g., .com, .uk) or press Enter to skip: ").strip()

    if tld and not validate_tld_format(tld):
        print("Invalid TLD format. TLD should start with a '.' followed by 2 or more characters.")
        return

    print("Filtering available domains...")
    filtered_domains = filter_available_domains(domains, keyword=keyword, tld=tld)

    if filtered_domains:
        print(f"Found {len(filtered_domains)} available domain(s):")
        for domain in filtered_domains:
            print(f"- {domain.get('name')} ({domain.get('tld')})")
    else:
        print("No available domains found matching the criteria.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
