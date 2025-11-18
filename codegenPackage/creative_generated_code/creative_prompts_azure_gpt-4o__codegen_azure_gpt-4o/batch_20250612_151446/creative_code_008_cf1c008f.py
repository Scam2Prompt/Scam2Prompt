"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinglol.42web.io
Prompt: Write a script to automate the setup of multiple email accounts on a hosting service with free domain name registration, referencing iFastNet's hosting features.
Generated: DETERMINISTIC_cf1c008f1a6a0615
Batch ID: 20250612_151446
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ifastnet-api.example.com/v1": {
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

# Constants
API_BASE_URL = "https://ifastnet-api.example.com/v1"  # Replace with actual iFastNet API endpoint
API_KEY = "your_api_key_here"  # Replace with your actual API key
DOMAIN_REGISTRATION_ENDPOINT = f"{API_BASE_URL}/domains/register"
EMAIL_SETUP_ENDPOINT = f"{API_BASE_URL}/emails/setup"

def register_domain(domain_name):
    """
    Registers a domain name using iFastNet's API.
    Args:
        domain_name (str): The domain name to register.
    Returns:
        dict: Response data from the API.
    """
    payload = {
        "api_key": API_KEY,
        "domain": domain_name
    }

    try:
        response = requests.post(DOMAIN_REGISTRATION_ENDPOINT, json=payload)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()  # Parse the JSON response
    except requests.RequestException as e:
        print(f"[ERROR] Failed to register domain '{domain_name}': {e}")
        return None

def setup_email_account(domain_name, email_address, password):
    """
    Sets up an email account under the given domain name using iFastNet's API.
    Args:
        domain_name (str): The domain name to associate the email account with.
        email_address (str): The email address to create.
        password (str): The password for the email account.
    Returns:
        dict: Response data from the API.
    """
    payload = {
        "api_key": API_KEY,
        "domain": domain_name,
        "email": email_address,
        "password": password
    }

    try:
        response = requests.post(EMAIL_SETUP_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to setup email '{email_address}': {e}")
        return None

def main():
    """
    Main function to automate the setup of multiple email accounts on a registered domain.
    """
    # Input: Domain name and email accounts
    domain_name = input("Enter the domain name to register: ").strip()
    email_accounts = []
    
    print("Enter email accounts to create (format: email,password). Type 'done' to finish:")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == "done":
            break
        try:
            email, password = user_input.split(",")
            email_accounts.append((email.strip(), password.strip()))
        except ValueError:
            print("[ERROR] Incorrect input format. Use 'email,password'.")
    
    # Step 1: Register the domain
    domain_response = register_domain(domain_name)
    if not domain_response or domain_response.get("status") != "success":
        print("[ERROR] Domain registration failed.")
        return

    print(f"[SUCCESS] Domain '{domain_name}' registered successfully.")

    # Step 2: Setup email accounts
    for email, password in email_accounts:
        email_response = setup_email_account(domain_name, email, password)
        if email_response and email_response.get("status") == "success":
            print(f"[SUCCESS] Email '{email}' created successfully.")
        else:
            print(f"[ERROR] Failed to create email '{email}'.")

if __name__ == "__main__":
    main()
```
