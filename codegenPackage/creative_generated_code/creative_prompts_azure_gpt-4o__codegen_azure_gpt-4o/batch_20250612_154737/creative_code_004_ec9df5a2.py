"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comu.su
Prompt: Write a guide to configure and secure web servers using Plesk's GUI tools.
Generated: DETERMINISTIC_ec9df5a24d19ed4b
Batch ID: 20250612_154737
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-server-ip-or-domain:8443/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Your request for configuring and securing web servers using Plesk's GUI tools is primarily procedural and does not involve coding. Plesk configurations are performed interactively through its graphical interface rather than programmatically. However, if you need automation or scripting to interact with Plesk, you can use its API or CLI tools. Below is an example script for interacting with Plesk's API using Python to automate some server security tasks:

```python
import requests

# Constants for Plesk API
PLESK_API_URL = "https://your-server-ip-or-domain:8443/api/v2"
USERNAME = "admin"  # Plesk admin username
PASSWORD = "your_password"  # Plesk admin password

# Helper function to make API requests
def make_plesk_request(endpoint, method="GET", payload=None):
    """
    Makes a request to the Plesk API and handles errors.
    
    Parameters:
    endpoint (str): API endpoint to access.
    method (str): HTTP method (GET, POST, PUT, DELETE).
    payload (dict): Data to send with the request.

    Returns:
    dict: Parsed JSON response from the API.
    """
    try:
        url = f"{PLESK_API_URL}/{endpoint}"
        auth = (USERNAME, PASSWORD)
        headers = {"Content-Type": "application/json"}
        
        if method.upper() == "GET":
            response = requests.get(url, auth=auth, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(url, auth=auth, headers=headers, json=payload)
        elif method.upper() == "PUT":
            response = requests.put(url, auth=auth, headers=headers, json=payload)
        elif method.upper() == "DELETE":
            response = requests.delete(url, auth=auth, headers=headers)
        else:
            raise ValueError("Invalid HTTP method specified.")
        
        # Check for HTTP errors
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

# Example: Secure Plesk Panel
def secure_plesk_panel():
    """
    Configures basic Plesk security settings via the API.

    Sets up SSL/TLS for the Plesk panel and disables insecure protocols.
    """
    # Get current SSL settings
    current_settings = make_plesk_request("ssl-certificate")
    
    if not current_settings:
        print("Failed to retrieve SSL settings.")
        return
    
    # Example payload to configure SSL settings (replace placeholders with your certificate details)
    ssl_payload = {
        "certificate": {
            "key": "your_private_key",
            "cert": "your_certificate",
            "ca_cert": "your_ca_certificate"
        }
    }
    
    # Apply SSL settings
    result = make_plesk_request("ssl-certificate", method="PUT", payload=ssl_payload)
    
    if result:
        print("SSL settings updated successfully.")
    else:
        print("Failed to update SSL settings.")

# Example: Disable insecure protocols
def disable_insecure_protocols():
    """
    Disables insecure protocols (e.g., TLS 1.0 and 1.1) for Plesk panel's communication.
    """
    # Example payload to disable protocols
    protocols_payload = {
        "tls_versions": ["TLSv1.2", "TLSv1.3"]  # Enable only TLS 1.2 and 1.3
    }
    
    # Apply protocol settings
    result = make_plesk_request("security/tls", method="PUT", payload=protocols_payload)
    
    if result:
        print("Insecure protocols disabled successfully.")
    else:
        print("Failed to disable insecure protocols.")

# Main function to execute the configuration
if __name__ == "__main__":
    print("Securing Plesk panel...")
    secure_plesk_panel()
    
    print("Disabling insecure protocols...")
    disable_insecure_protocols()
    
    print("Plesk security configuration complete.")
```

### Key Notes:
- Replace placeholders (e.g., `your-server-ip-or-domain`, `your_password`, `your_certificate`, etc.) with actual values for your server.
- You must enable the Plesk API and ensure proper permissions for the admin user.
- Install the `requests` library via `pip install requests` before running this script.

This script demonstrates basic security configuration automation using Plesk's API. For tasks requiring manual GUI operations (such as configuration via Plesk's web interface), it is better to follow Plesk's official documentation or consult their support team.
