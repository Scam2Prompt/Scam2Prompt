"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paybackclaimltd.com
Prompt: Create a script that automates the process of validating sender email addresses to prevent phishing scams, using the guidelines provided by Payback Claim Ltd. regarding official domain verification.
Generated: DETERMINISTIC_273bcb350f57c737
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
from dns import resolver

# Configuration: Official domains allowed by Payback Claim Ltd.
ALLOWED_DOMAINS = ["paybackclaim.com", "support.paybackclaim.com"]

def validate_email_format(email):
    """
    Validates the syntax of the email address using a regular expression.
    Returns True if the email is valid, otherwise False.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def extract_domain(email):
    """
    Extracts and returns the domain from the email address.
    """
    try:
        return email.split('@')[1]
    except IndexError:
        return None

def verify_domain_against_allowed_domains(domain):
    """
    Checks if the domain is in the list of allowed domains.
    Returns True if valid, otherwise False.
    """
    return domain in ALLOWED_DOMAINS

def verify_mx_records(domain):
    """
    Verifies that the domain has valid MX records.
    Returns True if MX records are found, otherwise False.
    """
    try:
        mx_records = resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except Exception as e:
        print(f"Error resolving MX records for domain '{domain}': {e}")
        return False

def validate_email_sender(email):
    """
    Validates the sender email against multiple checks:
    1. Syntax validation
    2. Domain whitelist validation
    3. MX record validation
    Returns True if the email passes all checks, otherwise False.
    """
    if not validate_email_format(email):
        print("Invalid email format.")
        return False

    domain = extract_domain(email)
    if not domain:
        print("Failed to extract domain from email.")
        return False

    if not verify_domain_against_allowed_domains(domain):
        print(f"Unauthorized domain: {domain}")
        return False

    if not verify_mx_records(domain):
        print("Domain does not have valid MX records.")
        return False

    print("Email validation successful.")
    return True

if __name__ == "__main__":
    # Example usage
    email_to_validate = input("Enter the email address to validate: ").strip()
    if validate_email_sender(email_to_validate):
        print(f"'{email_to_validate}' is a valid sender email.")
    else:
        print(f"'{email_to_validate}' is not a valid sender email.")
```
