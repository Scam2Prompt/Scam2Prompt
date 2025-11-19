"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasegift.epizy.com
Prompt: Write a code snippet that demonstrates how to set up multiple email accounts using the iFastNet Web Hosting cPanel.
Generated: DETERMINISTIC_053cf022a223e636
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import imaplib
import smtplib
import ssl

# Configuration for email accounts
EMAIL_ACCOUNTS = [
    {
        "email": "example1@yourdomain.com",
        "password": "password1",
        "smtp_server": "smtp.yourdomain.com",
        "imap_server": "imap.yourdomain.com",
        "port": 587
    },
    {
        "email": "example2@yourdomain.com",
        "password": "password2",
        "smtp_server": "smtp.yourdomain.com",
        "imap_server": "imap.yourdomain.com",
        "port": 587
    },
    # Add additional accounts if needed
]

def setup_email_account(account):
    """
    Sets up and verifies an email account using SMTP and IMAP.
    
    Parameters:
    account (dict): A dictionary containing the email account details.
    """
    try:
        # Establish connection to the SMTP server
        context = ssl.create_default_context()
        with smtplib.SMTP(account["smtp_server"], account["port"]) as smtp:
            smtp.starttls(context=context)  # Secure connection using TLS
            smtp.login(account["email"], account["password"])
            print(f"SMTP setup successful for {account['email']}")

        # Establish connection to the IMAP server
        with imaplib.IMAP4_SSL(account["imap_server"]) as imap:
            imap.login(account["email"], account["password"])
            print(f"IMAP setup successful for {account['email']}")

    except Exception as e:
        print(f"Error setting up account {account['email']}: {e}")


def setup_all_email_accounts(accounts):
    """
    Iterates through all email accounts and sets them up.
    
    Parameters:
    accounts (list): List of dictionaries containing email account details.
    """
    for account in accounts:
        setup_email_account(account)


if __name__ == "__main__":
    # Run setup for all email accounts
    setup_all_email_accounts(EMAIL_ACCOUNTS)
```
