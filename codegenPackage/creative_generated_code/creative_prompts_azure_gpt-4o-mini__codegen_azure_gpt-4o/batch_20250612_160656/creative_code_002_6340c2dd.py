"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: What are the key features of Plesk for managing DNS and mail services?
Generated: DETERMINISTIC_6340c2dd8f803a0a
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the key features of Plesk for managing DNS and mail services.
It uses a simulated API-like structure to showcase DNS and mail management functionalities.

Note: This is a simulated implementation for illustrative purposes and does not directly interact with a real Plesk server.
"""

import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PleskManager:
    def __init__(self):
        """
        Initialize the PleskManager with simulated DNS and mail settings.
        """
        self.dns_records = {}  # DNS records stored as a dictionary
        self.mail_accounts = {}  # Mail accounts stored as a dictionary

    # DNS Management
    def add_dns_record(self, domain: str, record_type: str, value: str) -> None:
        """
        Add a DNS record to the specified domain.
        :param domain: Domain name
        :param record_type: Type of DNS record (e.g., A, CNAME, MX, TXT)
        :param value: Value of the DNS record
        """
        if domain not in self.dns_records:
            self.dns_records[domain] = []
        
        record = {"type": record_type, "value": value}
        self.dns_records[domain].append(record)
        logging.info(f"Added DNS record to {domain}: {record}")

    def view_dns_records(self, domain: str) -> List[Dict[str, str]]:
        """
        View all DNS records for a specific domain.
        :param domain: Domain name
        :return: List of DNS records
        """
        if domain not in self.dns_records:
            logging.error(f"No DNS records found for domain: {domain}")
            return []
        return self.dns_records[domain]

    def delete_dns_record(self, domain: str, record_type: str, value: str) -> None:
        """
        Delete a specific DNS record from a domain.
        :param domain: Domain name
        :param record_type: Type of DNS record
        :param value: Value of the DNS record
        """
        if domain not in self.dns_records:
            logging.error(f"No DNS records found for domain: {domain}")
            return
        
        initial_count = len(self.dns_records[domain])
        self.dns_records[domain] = [record for record in self.dns_records[domain] if not (record["type"] == record_type and record["value"] == value)]
        
        if len(self.dns_records[domain]) < initial_count:
            logging.info(f"Deleted DNS record from {domain}: Type={record_type}, Value={value}")
        else:
            logging.warning(f"No matching DNS record found to delete in {domain}: Type={record_type}, Value={value}")

    # Mail Service Management
    def add_mail_account(self, email: str, password: str) -> None:
        """
        Add a mail account.
        :param email: Email address
        :param password: Password for the email account
        """
        if email in self.mail_accounts:
            logging.error(f"Mail account already exists: {email}")
            return
        
        self.mail_accounts[email] = {"password": password}
        logging.info(f"Mail account created: {email}")

    def view_mail_accounts(self) -> List[str]:
        """
        View all mail accounts.
        :return: List of email addresses
        """
        return list(self.mail_accounts.keys())

    def delete_mail_account(self, email: str) -> None:
        """
        Delete a mail account.
        :param email: Email address
        """
        if email in self.mail_accounts:
            del self.mail_accounts[email]
            logging.info(f"Mail account deleted: {email}")
        else:
            logging.error(f"Mail account not found: {email}")

# Main function for demonstration purposes
if __name__ == "__main__":
    # Instantiate the PleskManager
    plesk = PleskManager()

    # DNS Management Example
    plesk.add_dns_record("example.com", "A", "192.168.1.1")
    plesk.add_dns_record("example.com", "MX", "mail.example.com")
    print("DNS Records for example.com:", plesk.view_dns_records("example.com"))
    plesk.delete_dns_record("example.com", "A", "192.168.1.1")

    # Mail Service Management Example
    plesk.add_mail_account("user@example.com", "securepassword123")
    print("Mail Accounts:", plesk.view_mail_accounts())
    plesk.delete_mail_account("user@example.com")
```
