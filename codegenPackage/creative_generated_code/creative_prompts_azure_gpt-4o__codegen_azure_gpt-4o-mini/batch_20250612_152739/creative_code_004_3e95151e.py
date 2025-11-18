"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-cf.com
Prompt: Write a script to automate the deployment of a website using HostGator's tools, including activating the "Página Fácil" and installing WordPress.
Generated: DETERMINISTIC_3e95151e6ff4b68d
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostgator.com": {
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
import json

# Constants for HostGator API
HOSTGATOR_API_URL = "https://api.hostgator.com"
HOSTGATOR_API_KEY = "YOUR_API_KEY"
HOSTGATOR_ACCOUNT_ID = "YOUR_ACCOUNT_ID"

def activate_pagina_fácil():
    """
    Activates the 'Página Fácil' feature for the given HostGator account.
    """
    url = f"{HOSTGATOR_API_URL}/activate-pagina-facil"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HOSTGATOR_API_KEY}"
    }
    payload = {
        "account_id": HOSTGATOR_ACCOUNT_ID
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad responses
        print("Página Fácil activated successfully.")
    except requests.RequestException as e:
        print(f"Error activating Página Fácil: {e}")

def install_wordpress():
    """
    Installs WordPress on the HostGator account.
    """
    url = f"{HOSTGATOR_API_URL}/install-wordpress"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {HOSTGATOR_API_KEY}"
    }
    payload = {
        "account_id": HOSTGATOR_ACCOUNT_ID,
        "domain": "yourdomain.com",  # Replace with your domain
        "admin_user": "admin_username",  # Replace with desired admin username
        "admin_pass": "admin_password",  # Replace with desired admin password
        "admin_email": "admin@example.com"  # Replace with desired admin email
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an error for bad responses
        print("WordPress installed successfully.")
    except requests.RequestException as e:
        print(f"Error installing WordPress: {e}")

def main():
    """
    Main function to automate the deployment of a website.
    """
    activate_pagina_fácil()
    install_wordpress()

if __name__ == "__main__":
    main()
```

**Note**: Replace `YOUR_API_KEY`, `YOUR_ACCOUNT_ID`, `yourdomain.com`, `admin_username`, `admin_password`, and `admin@example.com` with the actual values for your HostGator account and desired WordPress setup.
