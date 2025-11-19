"""
Generated Code Metadata:
========================
Original URL: https://arcaem.com
Prompt: "How to configure a Plesk server for a new domain using Plesk's XML API?"
Generated: DETERMINISTIC_b39e3c6b01b3a713
Batch ID: 20250622_211350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import xml.etree.ElementTree as ET
import requests
import argparse

def configure_plesk_domain(api_url, api_key, domain, ip_address):
    """
    Configures a Plesk server for a new domain using Plesk's XML API.

    Args:
        api_url (str): The URL of the Plesk XML API.
        api_key (str): The API key for authentication.
        domain (str): The domain name to configure.
        ip_address (str): The IP address to assign to the domain.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """

    # Create the XML request
    root = ET.Element("packet")
    domain_element = ET.SubElement(root, "domain")
    domain_element.set("name", domain)

    # Create the create domain request
    create_element = ET.SubElement(domain_element, "create")
    create_element.text = ""

    # Set the IP address
    ip_element = ET.SubElement(create_element, "ip")
    ip_element.text = ip_address

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Convert the XML tree to a string
    xml_string = ET.tostring(tree.getroot(), encoding="unicode")

    # Set the API request headers
    headers = {
        "Content-Type": "application/xml",
        "HTTP-Auth": f"Basic {api_key}",
    }

    try:
        # Send the request to the Plesk API
        response = requests.post(api_url, headers=headers, data=xml_string)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the XML response
            response_root = ET.fromstring(response.content)

            # Check if the response contains an error
            error_element = response_root.find(".//error")
            if error_element is not None:
                print(f"Error: {error_element.text}")
                return False

            return True
        else:
            print(f"Failed to configure domain. Status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configure a Plesk server for a new domain")
    parser.add_argument("--api_url", required=True, help="The URL of the Plesk XML API")
    parser.add_argument("--api_key", required=True, help="The API key for authentication")
    parser.add_argument("--domain", required=True, help="The domain name to configure")
    parser.add_argument("--ip_address", required=True, help="The IP address to assign to the domain")

    args = parser.parse_args()

    success = configure_plesk_domain(args.api_url, args.api_key, args.domain, args.ip_address)
    print(f"Configuration successful: {success}")
```
