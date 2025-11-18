"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vilavi.online
Prompt: Provide an example of using Plesk's GUI to manage cloud hosting services for a small business.
Generated: DETERMINISTIC_bf35756939d9593a
Batch ID: 20250612_153424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-host:8443": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Plesk is primarily managed through its GUI and not via API-based programming in most cases. However, if the request is to integrate or automate a task using Plesk’s API for managing cloud hosting services, here's an example Python script leveraging Plesk's XML-RPC API to create a new domain for a small business. This script assumes you have appropriate credentials and API access enabled on your Plesk server.

```python
import xmlrpc.client
import sys

# Set up Plesk API credentials and server information
PLESK_SERVER_URL = "https://your-plesk-host:8443"
PLESK_API_USERNAME = "admin"
PLESK_API_PASSWORD = "your-password"

def create_domain(domain_name, ip_address, client_id):
    """
    Creates a new domain on the Plesk server using the XML-RPC API.

    Args:
        domain_name (str): The domain name to be created.
        ip_address (str): The IP address to assign to the domain.
        client_id (int): The client ID under which the domain will be created.

    Returns:
        dict: Result of the domain creation process.
    """
    try:
        # Connect to the Plesk XML-RPC API
        client = xmlrpc.client.ServerProxy(PLESK_SERVER_URL, allow_none=True)

        # Build the request payload
        request_payload = f"""
        <packet>
            <domain>
                <add>
                    <gen_setup>
                        <name>{domain_name}</name>
                        <ip_address>{ip_address}</ip_address>
                    </gen_setup>
                    <hosting>
                        <vrt_hst>
                            <property>
                                <name>ftp_login</name>
                                <value>{domain_name}_ftp</value>
                            </property>
                            <property>
                                <name>ftp_password</name>
                                <value>secure_password</value>
                            </property>
                        </vrt_hst>
                    </hosting>
                    <client_id>{client_id}</client_id>
                </add>
            </domain>
        </packet>
        """

        # Send the request to Plesk API
        response = client.operator.request(request_payload)

        # Parse the response
        if "status" in response and response["status"] == "ok":
            return {"success": True, "message": "Domain created successfully."}
        else:
            return {
                "success": False,
                "message": response.get("errtext", "Unknown error occurred."),
            }
    except Exception as e:
        return {"success": False, "message": str(e)}

if __name__ == "__main__":
    # Example usage
    DOMAIN_NAME = "example-business.com"
    IP_ADDRESS = "192.168.1.100"
    CLIENT_ID = 1  # Replace with your actual client ID

    result = create_domain(DOMAIN_NAME, IP_ADDRESS, CLIENT_ID)
    if result["success"]:
        print("Success:", result["message"])
    else:
        print("Error:", result["message"])
```

**Notes:**
- Replace placeholder values like `your-plesk-host`, `your-password`, and `secure_password` with actual values from your environment.
- Make sure the Plesk API is enabled, and the credentials provided have the necessary permissions.
- Always secure sensitive information (e.g., passwords) using environment variables or secret management tools in actual production environments.
