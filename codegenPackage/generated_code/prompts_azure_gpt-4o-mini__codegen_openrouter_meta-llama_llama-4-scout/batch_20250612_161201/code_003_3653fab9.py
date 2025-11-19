"""
Generated Code Metadata:
========================
Original URL: https://namebudget.net
Prompt: What are the recommended lengths and characteristics of domain names based on NameBudget's advice?
Generated: DETERMINISTIC_3653fab98a3016b4
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Domain Name Length and Characteristics Advisor based on NameBudget's advice.

This script provides recommended lengths and characteristics of domain names.
It checks for the validity and strength of a given domain name.

Author: [Your Name]
Date: [Today's Date]
"""

import re

class DomainNameAdvisor:
    def __init__(self):
        # Recommended lengths according to NameBudget
        self.min_length = 2
        self.max_length = 63

    def check_length(self, domain_name):
        """
        Check if the domain name length is within the recommended range.

        Args:
            domain_name (str): The domain name to check.

        Returns:
            bool: True if the length is valid, False otherwise.
        """
        return self.min_length <= len(domain_name) <= self.max_length

    def check_characters(self, domain_name):
        """
        Check if the domain name contains only valid characters.

        Args:
            domain_name (str): The domain name to check.

        Returns:
            bool: True if the characters are valid, False otherwise.
        """
        # Valid characters are letters, digits, and hyphens
        pattern = r'^[a-zA-Z0-9-]+$'
        return bool(re.match(pattern, domain_name))

    def check_tld(self, domain_name):
        """
        Check if the domain name has a valid top-level domain (TLD).

        Args:
            domain_name (str): The domain name to check.

        Returns:
            bool: True if the TLD is valid, False otherwise.
        """
        # For simplicity, assume a valid TLD is at least 2 characters long
        parts = domain_name.split('.')
        return len(parts) > 1 and len(parts[-1]) >= 2

    def advise(self, domain_name):
        """
        Provide advice on the given domain name.

        Args:
            domain_name (str): The domain name to advise on.

        Returns:
            dict: A dictionary containing the advice.
        """
        advice = {
            'valid': True,
            'messages': []
        }

        if not self.check_length(domain_name):
            advice['valid'] = False
            advice['messages'].append(f'Domain name should be between {self.min_length} and {self.max_length} characters long.')

        if not self.check_characters(domain_name):
            advice['valid'] = False
            advice['messages'].append('Domain name should only contain letters, digits, and hyphens.')

        if not self.check_tld(domain_name):
            advice['valid'] = False
            advice['messages'].append('Domain name should have a valid top-level domain (TLD).')

        return advice


def main():
    advisor = DomainNameAdvisor()

    # Test the advisor
    domain_names = [
        'example.com',
        'verylongdomainnametesthatexceedsthemaxlength.com',
        'invalid@domain.com',
        'short.tld',
        'valid123-domain.com'
    ]

    for domain_name in domain_names:
        advice = advisor.advise(domain_name)
        print(f'Domain Name: {domain_name}')
        print(f'Valid: {advice["valid"]}')
        if not advice['valid']:
            for message in advice['messages']:
                print(f'- {message}')
        print('---')


if __name__ == '__main__':
    main()
```
