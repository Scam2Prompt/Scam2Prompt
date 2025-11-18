"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Provide a detailed example of using Plesk's GUI to manage cloud hosting services for a small business.
Generated: DETERMINISTIC_3d8023ef9819e5ba
Batch ID: 20250612_154339
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

Plesk's GUI is a graphical interface tool, and interacting with it directly does not involve programming code. However, if you need an example of automating tasks in Plesk using its API, here's a Python script that demonstrates how to manage cloud hosting services for a small business using Plesk XML-RPC API. 

```python
import requests
from xml.etree import ElementTree

# Configuration variables - Update these with your actual Plesk details
plesk_url = "https://your-plesk-server:8443/enterprise/control/agent.php"
plesk_username = "admin"
plesk_password = "your_password"

# XML templates for API requests
create_subscription_xml = """
<packet>
    <webspace>
        <add>
            <gen_setup>
                <name>{domain_name}</name>
                <owner-id>{owner_id}</owner-id>
                <ip-address>{ip_address}</ip-address>
            </gen_setup>
            <hosting>
                <vrt_hst>
                    <property>
                        <name>ftp_login</name>
                        <value>{ftp_login}</value>
                    </property>
                    <property>
                        <name>ftp_password</name>
                        <value>{ftp_password}</value>
                    </property>
                </vrt_hst>
            </hosting>
            <plan-name>{plan_name}</plan-name>
        </add>
    </webspace>
</packet>
"""

# Function to send requests to the Plesk API
def send_plesk_request(xml_data):
    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            plesk_url,
            data=xml_data,
            headers=headers,
            auth=(plesk_username, plesk_password),
            verify=False  # Disable SSL verification (not recommended for production)
        )

        if response.status_code != 200:
            raise Exception(f"Error: API request failed with status code {response.status_code}")
        
        return ElementTree.fromstring(response.content)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example: Create a subscription for a small business website
def create_subscription(domain_name, owner_id, ip_address, ftp_login, ftp_password, plan_name):
    xml_data = create_subscription_xml.format(
        domain_name=domain_name,
        owner_id=owner_id,
        ip_address=ip_address,
        ftp_login=ftp_login,
        ftp_password=ftp_password,
        plan_name=plan_name
    )
    response = send_plesk_request(xml_data)
    if response is not None:
        print(ElementTree.tostring(response, encoding="unicode"))
    else:
        print("Failed to create subscription.")

# Main execution
if __name__ == "__main__":
    # Example input - Update with actual values
    domain_name = "example.com"
    owner_id = "1"  # Owner ID in Plesk
    ip_address = "192.168.1.1"  # Replace with actual IP
    ftp_login = "exampleftp"
    ftp_password = "securepassword"
    plan_name = "SmallBusinessPlan"

    create_subscription(domain_name, owner_id, ip_address, ftp_login, ftp_password, plan_name)
```

### Notes:
- Replace `plesk_url`, `plesk_username`, and `plesk_password` with your actual Plesk server credentials.
- Customize the `create_subscription()` function parameters according to your small business hosting requirements.
- Ensure proper SSL certificates are installed on your Plesk server (avoid `verify=False` in production).

This script can interact with Plesk's API to automate the creation of subscriptions for cloud hosting services.
