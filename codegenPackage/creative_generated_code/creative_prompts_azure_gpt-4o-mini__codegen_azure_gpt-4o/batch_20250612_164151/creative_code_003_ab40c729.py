"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Create a guide for configuring email accounts on iFastNet Web Hosting with modern cPanel.
Generated: DETERMINISTIC_ab40c7298b1a4370
Batch ID: 20250612_164151
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourdomain.com:2083": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the Python script to guide users through configuring email accounts on iFastNet Web Hosting with modern cPanel. The script interacts with the cPanel API for account creation and includes detailed comments for clarity.

```python
import requests
from requests.auth import HTTPBasicAuth

# Configuration details for connecting to cPanel
CPANEL_URL = "https://yourdomain.com:2083"  # Replace 'yourdomain.com' with your cPanel domain
CPANEL_USERNAME = "your_cpanel_username"    # Replace with your cPanel username
CPANEL_PASSWORD = "your_cpanel_password"    # Replace with your cPanel password

# Email account settings
EMAIL_DOMAIN = "yourdomain.com"             # Replace with your domain name
EMAIL_USERNAME = "newuser"                  # Replace with the desired email username
EMAIL_PASSWORD = "secure_password_123"      # Replace with a strong password for the email account
EMAIL_QUOTA = 1024                          # Email quota in MB (set as per your requirements)

def create_email_account():
    """
    Create an email account on iFastNet Web Hosting using cPanel's API.
    """
    # cPanel API endpoint for creating an email account
    endpoint = f"{CPANEL_URL}/execute/Email/add_pop"

    # Payload for the API request
    payload = {
        "email": EMAIL_USERNAME,
        "domain": EMAIL_DOMAIN,
        "password": EMAIL_PASSWORD,
        "quota": EMAIL_QUOTA
    }

    try:
        # Send a POST request to the cPanel API
        response = requests.post(
            endpoint,
            auth=HTTPBasicAuth(CPANEL_USERNAME, CPANEL_PASSWORD),
            json=payload
        )

        # Check if the request succeeded
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Check if the email account was successfully created
            if data.get("status") == 1:
                print("Email account successfully created!")
            else:
                print("Failed to create email account:", data.get("errors", "Unknown error"))
        else:
            print(f"HTTP error: {response.status_code} - {response.reason}")
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        # Handle connectivity or request errors
        print("An error occurred while connecting to the cPanel API:", str(e))

if __name__ == "__main__":
    # Run the script
    print("Starting email account creation process...")
    create_email_account()
```

### Notes:
- Replace placeholders (`yourdomain.com`, `your_cpanel_username`, `your_cpanel_password`, etc.) with your actual cPanel credentials and domain details.
- Ensure you use HTTPS (`https://`) to securely access the cPanel API.
- Use a strong password for the email account to prevent unauthorized access.
- Install the `requests` library if it's not already installed: `pip install requests`.

This script should be saved and executed in a secure environment, as it contains sensitive credentials.
