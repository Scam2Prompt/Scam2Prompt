"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Recommend an API or library for managing multiple email accounts on a web hosting service that includes unlimited disk space and free SSL, as offered by iFastNet.
Generated: DETERMINISTIC_12d5e0202aa506b5
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates how to manage multiple email accounts using the cPanel API.
iFastNet uses cPanel for web hosting services, so this example uses the `cpanelapi` library.
Make sure to install the cPanel API library (`pip install cpanelapi`) and consult your hosting provider for API credentials.
"""

import cpanelapi
import os

# Load credentials from environment variables for security
CPANEL_HOST = os.getenv("CPANEL_HOST")  # The cPanel server address
CPANEL_USER = os.getenv("CPANEL_USER")  # The cPanel username
CPANEL_PASSWORD = os.getenv("CPANEL_PASSWORD")  # The cPanel password

# Initialize the cPanel API client
try:
    client = cpanelapi.Client(
        host=CPANEL_HOST,
        user=CPANEL_USER,
        password=CPANEL_PASSWORD
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize cPanel API client: {e}")

def create_email_account(email, password, quota):
    """
    Creates a new email account.
    :param email: The email address to create (e.g., "user@example.com")
    :param password: The password for the email account
    :param quota: The disk quota for the email account in MB (use 0 for unlimited)
    :return: Response message from the cPanel API
    """
    try:
        response = client.call(
            "Email", "addpop",
            domain=email.split("@")[1],
            email=email.split("@")[0],
            password=password,
            quota=quota
        )
        return response
    except Exception as e:
        raise RuntimeError(f"Failed to create email account: {e}")

def list_email_accounts():
    """
    Lists all email accounts.
    :return: List of email accounts with details
    """
    try:
        response = client.call("Email", "listpops")
        return response.get("data", [])
    except Exception as e:
        raise RuntimeError(f"Failed to list email accounts: {e}")

def delete_email_account(email):
    """
    Deletes an email account.
    :param email: The email address to delete (e.g., "user@example.com")
    :return: Response message from the cPanel API
    """
    try:
        response = client.call(
            "Email", "delpop",
            domain=email.split("@")[1],
            email=email.split("@")[0]
        )
        return response
    except Exception as e:
        raise RuntimeError(f"Failed to delete email account: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Creating an email account
        print("Creating email account...")
        create_response = create_email_account("newuser@example.com", "securepassword123", 0)
        print("Email account created:", create_response)
        
        # Listing all email accounts
        print("Listing email accounts...")
        accounts = list_email_accounts()
        print("Email accounts:", accounts)
        
        # Deleting an email account
        print("Deleting email account...")
        delete_response = delete_email_account("newuser@example.com")
        print("Email account deleted:", delete_response)
    
    except Exception as e:
        print(f"Error: {e}")
```

Make sure to replace the environment variables (`CPANEL_HOST`, `CPANEL_USER`, `CPANEL_PASSWORD`) with your actual credentials or set them securely using your server environment. Additionally, install the necessary library (`cpanelapi`) before running the script.
