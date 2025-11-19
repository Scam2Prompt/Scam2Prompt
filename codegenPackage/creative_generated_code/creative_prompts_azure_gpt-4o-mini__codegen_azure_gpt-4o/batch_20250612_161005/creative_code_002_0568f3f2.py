"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comu.su
Prompt: What are the key features of Plesk for managing DNS and mail services in a hosting environment?
Generated: DETERMINISTIC_0568f3f222892971
Batch ID: 20250612_161005
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server.example.com/api/v2": {
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
"""
Plesk Features for Managing DNS and Mail Services
This script demonstrates the key features of Plesk for managing DNS and mail services
in a hosting environment using Python. It provides an example of interacting with a 
Plesk API simulation to retrieve and manage DNS and mail services.
"""

import requests

# Constants for the Plesk API URL and authentication
PLESK_API_URL = "https://your-plesk-server.example.com/api/v2"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Function to list DNS zones
def list_dns_zones():
    """
    Retrieve a list of DNS zones from the Plesk server.
    Returns:
        list: A list of DNS zone names.
    """
    try:
        response = requests.get(
            f"{PLESK_API_URL}/dns/zones",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        dns_zones = response.json()
        return dns_zones
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving DNS zones: {e}")
        return []

# Function to add a DNS record
def add_dns_record(zone, record_type, name, value):
    """
    Add a DNS record to a specified DNS zone.

    Args:
        zone (str): The DNS zone name.
        record_type (str): The type of DNS record (e.g., "A", "CNAME", "MX").
        name (str): The record name.
        value (str): The record value.

    Returns:
        bool: True if the record was successfully added, False otherwise.
    """
    try:
        payload = {
            "type": record_type,
            "name": name,
            "value": value
        }
        response = requests.post(
            f"{PLESK_API_URL}/dns/zones/{zone}/records",
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error adding DNS record: {e}")
        return False

# Function to list mail accounts
def list_mail_accounts():
    """
    Retrieve a list of mail accounts from the Plesk server.
    Returns:
        list: A list of mail account details.
    """
    try:
        response = requests.get(
            f"{PLESK_API_URL}/mail/accounts",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()
        mail_accounts = response.json()
        return mail_accounts
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving mail accounts: {e}")
        return []

# Function to create a new mail account
def create_mail_account(email, password, mailbox_size):
    """
    Create a new mail account on the Plesk server.

    Args:
        email (str): The email address for the new account.
        password (str): The password for the new account.
        mailbox_size (int): The mailbox size in MB.

    Returns:
        bool: True if the mail account was successfully created, False otherwise.
    """
    try:
        payload = {
            "email": email,
            "password": password,
            "mailbox_size": mailbox_size
        }
        response = requests.post(
            f"{PLESK_API_URL}/mail/accounts",
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error creating mail account: {e}")
        return False

# Main function to demonstrate usage of Plesk features
def main():
    # List DNS zones
    print("Listing DNS Zones...")
    dns_zones = list_dns_zones()
    print(f"DNS Zones: {dns_zones}")

    # Add a DNS record
    print("Adding a DNS Record...")
    if add_dns_record("example.com", "A", "www", "192.168.1.1"):
        print("DNS record added successfully.")
    else:
        print("Failed to add DNS record.")

    # List mail accounts
    print("Listing Mail Accounts...")
    mail_accounts = list_mail_accounts()
    print(f"Mail Accounts: {mail_accounts}")

    # Create a new mail account
    print("Creating a Mail Account...")
    if create_mail_account("newuser@example.com", "securepassword123", 500):
        print("Mail account created successfully.")
    else:
        print("Failed to create mail account.")

if __name__ == "__main__":
    main()
```
