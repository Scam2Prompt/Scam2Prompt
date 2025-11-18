"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Write a step-by-step guide for automating web app deployment on a traditional hosting server using Plesk's management tools.
Generated: DETERMINISTIC_607d386b3a30af6e
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

Below is an example of a Python script that automates web app deployment using Plesk's XML API. This script assumes you have the API credentials for your Plesk server and the application files ready to be transferred.

```python
import requests
import os
import xml.etree.ElementTree as ET
from requests.auth import HTTPBasicAuth

# Configuration
plesk_url = "https://your-plesk-server:8443/enterprise/control/agent.php"
plesk_username = "admin"  # Plesk admin username
plesk_password = "password"  # Plesk password
domain_name = "example.com"  # Domain to deploy the app
app_local_path = "/path/to/your/web_app"  # Path to your local web app files
app_remote_path = "/httpdocs"  # Remote path in Plesk where files will be uploaded

# Function to create XML request payload for Plesk API
def create_plesk_xml_request(action, params):
    """
    Create an XML request payload for the Plesk API.

    :param action: Action name for the API call (e.g., 'site', 'file-manager')
    :param params: Additional parameters for the API call
    :return: XML payload string
    """
    root = ET.Element("packet")
    action_tag = ET.SubElement(root, action)
    for key, value in params.items():
        param_tag = ET.SubElement(action_tag, key)
        param_tag.text = str(value)
    return ET.tostring(root, encoding="utf-8").decode("utf-8")

# Function to call Plesk API
def call_plesk_api(payload):
    """
    Send a request to the Plesk API.

    :param payload: XML request payload
    :return: Response object
    """
    try:
        response = requests.post(
            plesk_url,
            data=payload,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=HTTPBasicAuth(plesk_username, plesk_password),
            verify=False  # Set to True if you use a valid SSL certificate
        )
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Plesk API: {e}")
        return None

# Step 1: Verify domain existence in Plesk
print("Checking domain existence...")
domain_payload = create_plesk_xml_request("site", {"get": {"filter": {"name": domain_name}}})
domain_response = call_plesk_api(domain_payload)
if domain_response and "error" in domain_response.lower():
    print("Domain does not exist on the Plesk server.")
    exit(1)

# Step 2: Upload web app files to Plesk server
print("Uploading web app files...")
for root, dirs, files in os.walk(app_local_path):
    for file_name in files:
        local_file_path = os.path.join(root, file_name)
        relative_path = os.path.relpath(local_file_path, app_local_path)
        remote_file_path = os.path.join(app_remote_path, relative_path).replace("\\", "/")
        
        # Plesk file upload XML payload
        file_upload_payload = create_plesk_xml_request("file-manager", {
            "create-file": {
                "site-id": domain_name,
                "path": remote_file_path,
                "content": open(local_file_path, "rb").read().decode("utf-8")
            }
        })
        upload_response = call_plesk_api(file_upload_payload)
        if upload_response and "error" in upload_response.lower():
            print(f"Failed to upload file {file_name}: {upload_response}")
            exit(1)

print("Web app files uploaded successfully.")

# Step 3: Configure domain settings (optional)
print("Configuring domain settings...")
domain_settings_payload = create_plesk_xml_request("site", {
    "set": {
        "filter": {"name": domain_name},
        "values": {
            "hosting": {
                "web": {
                    "status": "enabled",
                    "document-root": app_remote_path
                }
            }
        }
    }
})
settings_response = call_plesk_api(domain_settings_payload)
if settings_response and "error" in settings_response.lower():
    print(f"Failed to configure domain settings: {settings_response}")
    exit(1)

print("Domain settings configured successfully.")

# Step 4: Verify deployment
print("Verifying deployment...")
verification_payload = create_plesk_xml_request("file-manager", {"get": {"site-id": domain_name}})
verification_response = call_plesk_api(verification_payload)
if verification_response and "error" in verification_response.lower():
    print("Failed to verify deployment.")
    exit(1)

print("Deployment verified successfully. Web app is live!")
```

**Usage Notes:**
- Replace `plesk_url`, `plesk_username`, `plesk_password`, `domain_name`, `app_local_path`, and `app_remote_path` with appropriate values.
- Ensure the local files exist and the Plesk server allows API access for the provided credentials.

**Dependencies:** Install the `requests` library (`pip install requests`) if not already installed.
