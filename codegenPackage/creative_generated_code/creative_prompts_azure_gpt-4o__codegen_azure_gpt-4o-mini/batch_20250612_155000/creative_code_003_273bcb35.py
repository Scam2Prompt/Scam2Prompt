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
from email.utils import parseaddr
from dns import resolver, exception

# Exception to handle email validation errors
class EmailValidationError(Exception):
    pass

def is_valid_email(email: str) -> bool:
    """Validate the format of an email address using regex."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def get_domain(email: str) -> str:
    """Extract the domain from an email address."""
    return parseaddr(email)[1].split('@')[-1]

def verify_domain(domain: str) -> bool:
    """Check if the domain has an MX record, indicating it can receive emails."""
    try:
        records = resolver.resolve(domain, 'MX')
        return len(records) > 0
    except (exception.DNSException, Exception) as e:
        raise EmailValidationError(f"Domain verification failed: {str(e)}")

def validate_email(email: str) -> bool:
    """Validate the email address format and check its domain."""
    if not is_valid_email(email):
        raise EmailValidationError("Invalid email format.")
    
    domain = get_domain(email)
    if not verify_domain(domain):
        raise EmailValidationError("Domain does not have valid MX records.")
    
    return True

def main():
    """Main function to validate sender email addresses."""
    email_list = [
        "example@valid-domain.com",
        "invalid-email.com",
        "test@invalid-domain.com"
    ]
    
    for email in email_list:
        try:
            if validate_email(email):
                print(f"{email} is valid and verified.")
        except EmailValidationError as e:
            print(f"Validation error for {email}: {e}")

if __name__ == "__main__":
    main()
```
