"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Provide code examples for automating the setup of Nginx Proxy Manager through its admin panel API for managing multiple hosts.
Generated: DETERMINISTIC_ebecbad7a1f882ee
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://<NGINX_PROXY_MANAGER_URL>/api": {
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
import json

# Configuration
API_BASE_URL = "http://<NGINX_PROXY_MANAGER_URL>/api"
ADMIN_EMAIL = "<ADMIN_EMAIL>"
ADMIN_PASSWORD = "<ADMIN_PASSWORD>"

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

def authenticate(email, password):
    """
    Authenticate with the Nginx Proxy Manager API and return the access token.
    """
    auth_url = f"{API_BASE_URL}/tokens"
    payload = {
        "identity": email,
        "secret": password
    }
    try:
        response = requests.post(auth_url, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()["token"]  # Access token
    except requests.RequestException as e:
        raise SystemExit(f"Authentication failed: {e}")

def create_proxy_host(token, domain_name, forward_host, forward_port):
    """
    Create a new proxy host for a given domain name.
    """
    url = f"{API_BASE_URL}/nginx/proxy-hosts"
    
    # Updated headers with token
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    
    payload = {
        "domain_names": [domain_name],
        "forward_host": forward_host,
        "forward_port": forward_port,
        "access_list_id": 0,  # Public access
        "certificate_id": 0,  # No SSL by default
        "ssl_forced": False,
        "meta": {
            "letsencrypt_agree": False,  # Disable Let's Encrypt for this example
        },
        "advanced_config": "",
        "locations": [],
        "block_exploits": False,
        "caching_enabled": False,
        "allow_websocket_upgrade": False,
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()  # Proxy host details
    except requests.RequestException as e:
        raise SystemExit(f"Failed to create proxy host: {e}")

def main():
    """
    Main function to authenticate and create multiple proxy hosts.
    """
    # Authenticate and get the token
    token = authenticate(ADMIN_EMAIL, ADMIN_PASSWORD)

    # Define hosts to create
    hosts = [
        {"domain_name": "example1.com", "forward_host": "192.168.1.101", "forward_port": 80},
        {"domain_name": "example2.com", "forward_host": "192.168.1.102", "forward_port": 8080},
        {"domain_name": "example3.com", "forward_host": "192.168.1.103", "forward_port": 3000},
    ]

    # Create proxy hosts
    for host in hosts:
        try:
            result = create_proxy_host(token, host["domain_name"], host["forward_host"], host["forward_port"])
            print(f"Successfully created proxy host: {result}")
        except SystemExit as err:
            print(err)
            continue

if __name__ == "__main__":
    main()
```
