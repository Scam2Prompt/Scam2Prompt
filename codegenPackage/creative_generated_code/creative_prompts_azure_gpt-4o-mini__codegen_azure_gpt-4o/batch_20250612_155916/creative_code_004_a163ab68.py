"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.com.se
Prompt: Create a code example demonstrating how to configure mail services in Plesk programmatically.
Generated: DETERMINISTIC_a163ab6894b00ac2
Batch ID: 20250612_155916
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/enterprise/control/agent.php": {
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
Script to configure mail services programmatically in Plesk using the Plesk XML-RPC API.

Note:
- Replace placeholders with actual credentials and values.
- Ensure you have proper permissions and use this script in accordance with your Plesk license agreement.
"""

import requests

# Plesk server configuration
PLESK_API_URL = "https://your-plesk-server:8443/enterprise/control/agent.php"
USERNAME = "your-plesk-username"
PASSWORD = "your-plesk-password"

# XML payload to configure mail service
def create_mail_service_payload(domain, enable_mail_service):
    """
    Creates an XML payload to configure mail services for a domain.
    :param domain: The domain name for which mail service is being configured.
    :param enable_mail_service: Boolean flag to enable or disable the mail service.
    :return: XML payload as a string.
    """
    action = "true" if enable_mail_service else "false"
    return f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <packet version="1.6.3.0">
        <mail>
            <set>
                <filter>
                    <domain>
                        <name>{domain}</name>
                    </domain>
                </filter>
                <values>
                    <mailservice>{action}</mailservice>
                </values>
            </set>
        </mail>
    </packet>
    """

def configure_mail_service(domain, enable_mail_service):
    """
    Configures mail service for a domain in Plesk panel.
    :param domain: The domain name for which mail service is being configured.
    :param enable_mail_service: Boolean flag to enable or disable the mail service.
    """
    # XML payload
    payload = create_mail_service_payload(domain, enable_mail_service)

    try:
        # Make the API request
        response = requests.post(
            PLESK_API_URL,
            data=payload,
            headers={"Content-Type": "text/xml"},
            auth=(USERNAME, PASSWORD),
            verify=False  # Avoid SSL verification issues; use with caution
        )

        # Check for HTTP errors
        response.raise_for_status()

        # Process the response
        if "<status>ok</status>" in response.text:
            print(f"Mail service successfully {'enabled' if enable_mail_service else 'disabled'} for domain: {domain}")
        else:
            print(f"Failed to configure mail service for domain: {domain}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while configuring mail service: {e}")

# Example usage
if __name__ == "__main__":
    DOMAIN = "example.com"
    ENABLE_MAIL_SERVICE = True  # Set to False to disable mail service

    configure_mail_service(DOMAIN, ENABLE_MAIL_SERVICE)
```
