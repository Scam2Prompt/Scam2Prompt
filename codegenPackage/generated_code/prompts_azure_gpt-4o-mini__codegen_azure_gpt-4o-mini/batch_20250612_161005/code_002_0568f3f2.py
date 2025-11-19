"""
Generated Code Metadata:
========================
Original URL: https://comu.su
Prompt: What are the key features of Plesk for managing DNS and mail services in a hosting environment?
Generated: DETERMINISTIC_0568f3f222892971
Batch ID: 20250612_161005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Plesk Features for Managing DNS and Mail Services

This script outlines the key features of Plesk for managing DNS and mail services
in a hosting environment. It serves as a reference for developers and system
administrators who are looking to understand the capabilities of Plesk.

Note: This is a mock representation and does not interact with a real Plesk API.
"""

class PleskDNSMailManager:
    def __init__(self):
        """
        Initializes the PleskDNSMailManager class.
        """
        self.dns_records = []
        self.mail_accounts = []

    def add_dns_record(self, record_type, name, value, ttl=3600):
        """
        Adds a DNS record to the DNS records list.

        :param record_type: Type of DNS record (e.g., A, CNAME, MX)
        :param name: The domain name for the record
        :param value: The value for the DNS record
        :param ttl: Time to live for the DNS record (default is 3600 seconds)
        :raises ValueError: If the record type is invalid
        """
        valid_record_types = ['A', 'CNAME', 'MX', 'TXT', 'AAAA']
        if record_type not in valid_record_types:
            raise ValueError(f"Invalid record type: {record_type}. Must be one of {valid_record_types}.")

        record = {
            'type': record_type,
            'name': name,
            'value': value,
            'ttl': ttl
        }
        self.dns_records.append(record)
        print(f"Added DNS record: {record}")

    def list_dns_records(self):
        """
        Lists all DNS records.

        :return: List of DNS records
        """
        return self.dns_records

    def add_mail_account(self, email, password, domain):
        """
        Adds a mail account to the mail accounts list.

        :param email: The email address to create
        :param password: The password for the email account
        :param domain: The domain for the email account
        :raises ValueError: If the email format is invalid
        """
        if '@' not in email or not email.endswith(domain):
            raise ValueError(f"Invalid email address: {email}. Must be in the format 'user@{domain}'.")

        account = {
            'email': email,
            'password': password,
            'domain': domain
        }
        self.mail_accounts.append(account)
        print(f"Added mail account: {account}")

    def list_mail_accounts(self):
        """
        Lists all mail accounts.

        :return: List of mail accounts
        """
        return self.mail_accounts

# Example usage
if __name__ == "__main__":
    try:
        manager = PleskDNSMailManager()
        
        # Adding DNS records
        manager.add_dns_record('A', 'example.com', '192.0.2.1')
        manager.add_dns_record('MX', 'example.com', 'mail.example.com')

        # Listing DNS records
        print("DNS Records:")
        print(manager.list_dns_records())

        # Adding mail accounts
        manager.add_mail_account('user@example.com', 'securepassword', 'example.com')

        # Listing mail accounts
        print("Mail Accounts:")
        print(manager.list_mail_accounts())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
