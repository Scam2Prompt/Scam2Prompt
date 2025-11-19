"""
Generated Code Metadata:
========================
Original URL: https://cetlus.zone
Prompt: Write a Python script to check if a domain has a valid registration record, referencing the error message "cetlus.zone Adlı Domainin Sistmemizde Kaydı Yoktur".
Generated: DETERMINISTIC_3b25ec7795dd6175
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import whois
import sys
from datetime import datetime

def check_domain_registration(domain_name):
    """
    Check if a domain has a valid registration record.
    
    Args:
        domain_name (str): The domain name to check.
        
    Returns:
        dict: A dictionary containing the registration status and details.
              Keys: 'is_registered', 'error', 'expiration_date'
    """
    result = {
        'is_registered': False,
        'error': None,
        'expiration_date': None
    }
    
    try:
        domain_info = whois.whois(domain_name)
        
        # Check if domain exists by looking at expiration date
        if domain_info.expiration_date:
            result['is_registered'] = True
            if isinstance(domain_info.expiration_date, list):
                result['expiration_date'] = domain_info.expiration_date[0]
            else:
                result['expiration_date'] = domain_info.expiration_date
        else:
            result['error'] = f"{domain_name} Adlı Domainin Sistmemizde Kaydı Yoktur"
            
    except whois.parser.PywhoisError as e:
        if "No match for" in str(e) or "not found" in str(e).lower():
            result['error'] = f"{domain_name} Adlı Domainin Sistmemizde Kaydı Yoktur"
        else:
            result['error'] = f"Error checking domain: {str(e)}"
    except Exception as e:
        result['error'] = f"Unexpected error: {str(e)}"
        
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python domain_checker.py <domain_name>")
        sys.exit(1)
        
    domain = sys.argv[1]
    result = check_domain_registration(domain)
    
    if result['is_registered']:
        print(f"Domain {domain} is registered.")
        print(f"Expiration date: {result['expiration_date']}")
    else:
        print(result['error'])
```
