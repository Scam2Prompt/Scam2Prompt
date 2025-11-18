"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syneoshealthls.com
Prompt: Provide a step-by-step Python script to add email users to a domain hosted on a Plesk server, referencing Media Temple's instructions.
Generated: DETERMINISTIC_d0cae448d16f019f
Batch ID: 20250612_151639
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server-url:8443/enterprise/control/agent.php": {
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
from requests.auth import HTTPBasicAuth

# Configuration
PLESK_API_URL = "https://your-plesk-server-url:8443/enterprise/control/agent.php"
PLESK_USERNAME = "your-plesk-username"
PLESK_PASSWORD = "your-plesk-password"
DOMAIN_NAME = "example.com"  # Replace with your domain name

# Function to create an email address
def create_email_address(email_address, password, mailbox_size_mb):
    """
    Create an email address on the specified domain in Plesk.

    :param email_address: Full email address (e.g., user@example.com)
    :param password: Password for the email account
    :param mailbox_size_mb: Mailbox size in MB
    :return: Response from the Plesk API
    """
    # Compose XML body for the API request
    xml_body = f"""
    <packet>
        <mail>
            <create>
                <filter>
                    <site-id>{DOMAIN_NAME}</site-id>
                </filter>
                <mailname>
                    <name>{email_address.split('@')[0]}</name>
                    <mailbox>
                        <enabled>true</enabled>
                        <quota>{mailbox_size_mb}</quota>
                    </mailbox>
                    <password>
                        <value>{password}</value>
                        <type>plain</type>
                    </password>
                </mailname>
            </create>
        </mail>
    </packet>
    """

    try:
        # Make the API request
        response = requests.post(
            PLESK_API_URL,
            data=xml_body,
            auth=HTTPBasicAuth(PLESK_USERNAME, PLESK_PASSWORD),
            headers={"Content-Type": "text/xml"}
        )

        # Check if the response is successful
        response.raise_for_status()
        return response.text

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    # Email account details
    email = "user@example.com"
    password = "securepassword123"  # Ensure this meets Plesk's password requirements
    mailbox_size = 1024  # Mailbox size in MB

    # Create the email user
    result = create_email_address(email, password, mailbox_size)

    # Print the result
    if result:
        print("Response from Plesk API:")
        print(result)
```

Note:
- Replace `your-plesk-server-url`, `your-plesk-username`, and `your-plesk-password` with actual server credentials.
- Ensure the `DOMAIN_NAME` variable matches your Plesk domain name.
- The script assumes Plesk's XML API is accessible and properly configured for use.
