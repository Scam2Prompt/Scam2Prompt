"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Create a Python script to retrieve and display the status of all hosted websites managed via Plesk, including DNS and mail service details.
Generated: DETERMINISTIC_a3ef4d30772c40ea
Batch ID: 20250612_152526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-domain-or-ip:8443/enterprise/control/agent.php": {
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
import xml.etree.ElementTree as ET

# Constants for Plesk server connection
PLESK_API_ENDPOINT = "https://your-plesk-domain-or-ip:8443/enterprise/control/agent.php"
PLESK_USERNAME = "your-plesk-username"
PLESK_PASSWORD = "your-plesk-password"

def get_websites_status():
    """
    Retrieves and displays the status of all hosted websites managed via Plesk,
    including DNS and mail service details.
    """
    try:
        # XML payload to request domain info from Plesk
        payload = """
        <?xml version="1.0" encoding="UTF-8"?>
        <packet>
            <domain>
                <get>
                    <filter/>
                    <dataset>
                        <gen_info/>
                        <hosting/>
                        <dns/>
                        <mail/>
                    </dataset>
                </get>
            </domain>
        </packet>
        """

        # Send request to Plesk API using HTTP Basic Authentication
        response = requests.post(PLESK_API_ENDPOINT, 
                                 data=payload, 
                                 auth=HTTPBasicAuth(PLESK_USERNAME, PLESK_PASSWORD), 
                                 headers={"Content-Type": "application/xml"}, 
                                 verify=False)  # Disable SSL verification for simplicity
        
        # Raise an error if the API call fails
        response.raise_for_status()

        # Parse the XML response
        root = ET.fromstring(response.content)

        # Extract domain information
        domains = root.findall(".//domain")
        if not domains:
            print("No domains found in the Plesk server.")
            return

        # Display status for each domain
        for domain in domains:
            name = domain.find(".//name").text if domain.find(".//name") is not None else "N/A"
            status = domain.find(".//status").text if domain.find(".//status") is not None else "N/A"
            dns = domain.find(".//dns").text if domain.find(".//dns") is not None else "N/A"
            mail = domain.find(".//mail").text if domain.find(".//mail") is not None else "N/A"

            print(f"Domain: {name}")
            print(f"  Status: {status}")
            print(f"  DNS Enabled: {dns}")
            print(f"  Mail Enabled: {mail}")
            print("-" * 40)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while connecting to Plesk API: {e}")
    except ET.ParseError as e:
        print(f"Error occurred while parsing XML response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the script
    print("Fetching websites status from Plesk...")
    get_websites_status()
```

**Note:** Replace `your-plesk-domain-or-ip`, `your-plesk-username`, and `your-plesk-password` with the actual Plesk server details. Also, ensure SSL verification or proper certificates are configured in production environments. Disabling `verify=False` is not recommended for production.
