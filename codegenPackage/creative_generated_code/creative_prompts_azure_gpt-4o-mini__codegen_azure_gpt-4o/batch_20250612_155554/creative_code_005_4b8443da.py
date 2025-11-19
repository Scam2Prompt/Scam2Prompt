"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vilavi.online
Prompt: How does Plesk enhance the management of web hosting businesses, and what API calls can I use to leverage this?
Generated: DETERMINISTIC_4b8443da80868927
Batch ID: 20250612_155554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://<your-plesk-server>/enterprise/control/agent.php": {
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
This script demonstrates how to use the Plesk XML API to manage a web hosting business.
Plesk enhances web hosting management by providing a centralized control panel for 
managing websites, domains, email accounts, databases, and other hosting resources.
The script includes sample API calls to demonstrate basic functionality.

Prerequisites:
1. Install the `requests` library using `pip install requests`.
2. Ensure you have Plesk API credentials and enable API access.

NOTE: Replace placeholders (host, username, password, etc.) with actual values.
"""

import requests
from requests.auth import HTTPBasicAuth

# Plesk API endpoint and credentials
plesk_url = "https://<your-plesk-server>/enterprise/control/agent.php"
plesk_username = "<your-username>"
plesk_password = "<your-password>"

def create_domain(domain_name, ip_address):
    """
    Create a new domain in Plesk using the XML API.

    :param domain_name: The name of the domain to create.
    :param ip_address: The IP address for the domain.
    :return: Response from the Plesk API.
    """
    # XML payload for creating a domain
    xml_payload = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <packet version="1.6.3.0">
        <domain>
            <add>
                <gen_setup>
                    <name>{domain_name}</name>
                    <ip_address>{ip_address}</ip_address>
                </gen_setup>
                <hosting>
                    <vrt_hst>
                        <property>
                            <name>php</name>
                            <value>true</value>
                        </property>
                    </vrt_hst>
                </hosting>
            </add>
        </domain>
    </packet>
    """
    try:
        # Make the API call with basic authentication
        response = requests.post(
            plesk_url,
            data=xml_payload,
            auth=HTTPBasicAuth(plesk_username, plesk_password),
            headers={"Content-Type": "application/xml"}
        )
        
        # Check for HTTP response errors
        response.raise_for_status()
        
        # Return the API response
        return response.text
    except requests.exceptions.RequestException as e:
        # Log and handle any errors
        print(f"Error creating domain: {e}")
        return None

def get_domains():
    """
    Retrieve the list of domains from Plesk.

    :return: Response from the Plesk API.
    """
    # XML payload for retrieving domains
    xml_payload = """
    <?xml version="1.0" encoding="UTF-8"?>
    <packet version="1.6.3.0">
        <domain>
            <get>
                <filter/>
            </get>
        </domain>
    </packet>
    """
    try:
        # Make the API call with basic authentication
        response = requests.post(
            plesk_url,
            data=xml_payload,
            auth=HTTPBasicAuth(plesk_username, plesk_password),
            headers={"Content-Type": "application/xml"}
        )
        
        # Check for HTTP response errors
        response.raise_for_status()
        
        # Return the API response
        return response.text
    except requests.exceptions.RequestException as e:
        # Log and handle any errors
        print(f"Error retrieving domains: {e}")
        return None

# Example usage of the functions
if __name__ == "__main__":
    # Create a new domain
    domain_response = create_domain("example.com", "192.168.1.1")
    print("Create Domain Response:")
    print(domain_response)

    # Retrieve the list of domains
    domains_response = get_domains()
    print("Get Domains Response:")
    print(domains_response)
```

*Note: Replace `<your-plesk-server>`, `<your-username>`, and `<your-password>` with your actual Plesk server details and credentials.*
