"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Provide an example of using Plesk to set up email services for a domain.
Generated: DETERMINISTIC_42cf408c2b3ea5db
Batch ID: 20250612_155936
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is an example Python script to interact with the Plesk API to set up email services for a domain. This script assumes you have Plesk API credentials and the domain already configured in Plesk.

```python
import requests

# Plesk API credentials
PLESK_API_URL = "https://your-plesk-server:8443/api/v2"
PLESK_USERNAME = "your-plesk-username"
PLESK_PASSWORD = "your-plesk-password"

# Domain details
DOMAIN_NAME = "example.com"
EMAIL_ADDRESS = "info@example.com"
EMAIL_PASSWORD = "secure_password"

def setup_email_service(domain_name, email_address, email_password):
    """
    Sets up an email service for the specified domain in Plesk using the Plesk API.

    Args:
        domain_name (str): The domain name for which the email service is being configured.
        email_address (str): The email address to create.
        email_password (str): The password for the email account.

    Returns:
        dict: API response data containing the result of the setup.
    """
    # API endpoint to create an email address
    endpoint = f"{PLESK_API_URL}/email-addresses"

    # Payload for creating the email address
    payload = {
        "domain": domain_name,
        "email": email_address,
        "password": email_password
    }

    try:
        # Make the API call
        response = requests.post(
            endpoint,
            json=payload,
            auth=(PLESK_USERNAME, PLESK_PASSWORD),
            verify=False  # Set to False temporarily if using self-signed SSL certificates; change for production.
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Parse and return the response JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle any connection errors, HTTP errors, etc.
        raise RuntimeError(f"Error setting up email service: {str(e)}") from e
    except ValueError as e:
        # Handle JSON parsing errors
        raise RuntimeError(f"Error parsing the API response: {str(e)}") from e


# Main script
if __name__ == "__main__":
    try:
        # Set up the email service
        result = setup_email_service(DOMAIN_NAME, EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Print the result of the operation
        print("Email service setup successful!")
        print("API Response:", result)
    except RuntimeError as err:
        # Catch and log any errors during execution
        print("Failed to set up email service:", err)
```

### Notes:
- Replace `your-plesk-server`, `your-plesk-username`, and `your-plesk-password` with the actual values for your Plesk server.
- Replace `example.com` and `info@example.com` with your target domain name and desired email address.
- Ensure that SSL certificates on the Plesk server are properly configured for production, and set `verify=True` in the `requests.post` call.
- Install the required dependency (`requests`) using `pip install requests` before running the script.
