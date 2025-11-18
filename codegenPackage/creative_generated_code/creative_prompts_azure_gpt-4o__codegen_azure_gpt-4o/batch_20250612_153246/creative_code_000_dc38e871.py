"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dedicatusit.com
Prompt: Write a Python script to automate the migration process to Microsoft 365, referencing the services offered by Dedicatus-IT for Office 365 administration.
Generated: DETERMINISTIC_dc38e87125ad18e6
Batch ID: 20250612_153246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://graph.microsoft.com/.default": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.dedicatus-it.example.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.microsoft.com/v1.0/users": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://login.microsoftonline.com/{MICROSOFT_365_TENANT_ID": {
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
Automated Migration Script to Microsoft 365
This script helps automate the migration process to Microsoft 365, referencing the services offered by Dedicatus-IT
for Office 365 administration.

Dependencies:
- `requests` for HTTP requests
- `msal` for Microsoft authentication
- `logging` for proper logging
- Ensure that Dedicatus-IT API endpoint and credentials are pre-configured.

Usage:
- Configure the constants and authentication details as necessary.
- Run the script in a Python 3.x environment.

Author: Professional Software Developer
"""

import logging
import requests
from msal import ConfidentialClientApplication

# Configure logging
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("migration.log"),
        logging.StreamHandler()
    ]
)

# Constants (Update these as per requirements)
DEDICATUS_IT_API_BASE_URL = "https://api.dedicatus-it.example.com/v1"
MICROSOFT_365_TENANT_ID = "your_tenant_id"
MICROSOFT_365_CLIENT_ID = "your_client_id"
MICROSOFT_365_CLIENT_SECRET = "your_client_secret"
DEDICATUS_IT_API_KEY = "your_api_key"

# Authentication scope for Microsoft 365
MICROSOFT_365_SCOPES = ["https://graph.microsoft.com/.default"]

# Function to authenticate with Microsoft 365
def authenticate_with_microsoft_365():
    """
    Authenticates with Microsoft 365 using MSAL (Microsoft Authentication Library).
    Returns a valid access token.
    """
    try:
        app = ConfidentialClientApplication(
            client_id=MICROSOFT_365_CLIENT_ID,
            client_credential=MICROSOFT_365_CLIENT_SECRET,
            authority=f"https://login.microsoftonline.com/{MICROSOFT_365_TENANT_ID}"
        )
        
        result = app.acquire_token_for_client(scopes=MICROSOFT_365_SCOPES)
        
        if "access_token" not in result:
            logging.error("Failed to acquire Microsoft 365 access token.")
            raise Exception("Authentication failed")
        
        logging.info("Successfully authenticated with Microsoft 365.")
        return result["access_token"]
    except Exception as e:
        logging.exception("Error during Microsoft 365 authentication.")
        raise

# Function to interact with Dedicatus-IT services
def call_dedicatus_it_api(endpoint, method="GET", payload=None):
    """
    Calls the Dedicatus-IT API endpoint for Office 365 administration.
    Args:
        endpoint (str): API endpoint to call.
        method (str): HTTP method ("GET", "POST", etc.).
        payload (dict): Payload for POST requests.
    Returns:
        dict: Parsed JSON response from the API.
    Raises:
        Exception: If the API call fails.
    """
    url = f"{DEDICATUS_IT_API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {DEDICATUS_IT_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.request(method, url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        logging.info(f"API call to {endpoint} succeeded.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API call to {endpoint} failed: {e}")
        raise

# Main function for migration
def migrate_to_microsoft_365():
    """
    Automates the migration process to Microsoft 365.
    Uses Dedicatus-IT services for Office 365 administration.
    """
    try:
        # Authenticate with Microsoft 365
        access_token = authenticate_with_microsoft_365()
        
        # Example: Get list of users from Dedicatus-IT
        users = call_dedicatus_it_api("users")
        
        for user in users:
            user_email = user.get("email")
            logging.info(f"Starting migration for user: {user_email}")
            
            # Example: Create user in Microsoft 365
            create_user_payload = {
                "displayName": user.get("name"),
                "mailNickname": user.get("username"),
                "userPrincipalName": user_email,
                "passwordProfile": {
                    "forceChangePasswordNextSignIn": True,
                    "password": user.get("temporary_password")
                },
                "accountEnabled": True
            }
            
            try:
                response = requests.post(
                    "https://graph.microsoft.com/v1.0/users",
                    headers={"Authorization": f"Bearer {access_token}"},
                    json=create_user_payload
                )
                response.raise_for_status()
                logging.info(f"User {user_email} successfully migrated to Microsoft 365.")
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to migrate user {user_email}: {e}")
    except Exception as e:
        logging.exception("Migration process failed.")
        raise

# Entry point
if __name__ == "__main__":
    try:
        logging.info("Starting migration process to Microsoft 365...")
        migrate_to_microsoft_365()
        logging.info("Migration process completed successfully.")
    except Exception as e:
        logging.error("Migration process terminated with errors.")
```
