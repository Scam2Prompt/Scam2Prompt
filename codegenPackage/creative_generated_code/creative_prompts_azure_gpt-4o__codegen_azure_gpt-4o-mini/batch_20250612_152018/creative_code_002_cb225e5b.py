"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-link.net
Prompt: Recommend libraries or tools for interacting programmatically with Nginx Proxy Manager to manage proxy hosts.
Generated: DETERMINISTIC_cb225e5bd4ca20f4
Batch ID: 20250612_152018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://upstream-server:port": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://your-nginx-proxy-manager-url": {
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

class NginxProxyManagerClient:
    """
    A client for interacting with the Nginx Proxy Manager API.
    """

    def __init__(self, base_url: str, username: str, password: str):
        """
        Initializes the NginxProxyManagerClient with the base URL and credentials.

        :param base_url: The base URL of the Nginx Proxy Manager instance.
        :param username: The username for authentication.
        :param password: The password for authentication.
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def get_proxy_hosts(self):
        """
        Retrieves a list of proxy hosts from the Nginx Proxy Manager.

        :return: A list of proxy hosts.
        :raises Exception: If the request to the API fails.
        """
        try:
            response = self.session.get(f"{self.base_url}/api/nginx/proxy-hosts")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch proxy hosts: {e}")

    def create_proxy_host(self, domain: str, upstream: str):
        """
        Creates a new proxy host in the Nginx Proxy Manager.

        :param domain: The domain name for the proxy host.
        :param upstream: The upstream server URL.
        :return: The created proxy host details.
        :raises Exception: If the request to the API fails.
        """
        proxy_host_data = {
            "domain": domain,
            "upstream": upstream,
            "enabled": True,
        }
        try:
            response = self.session.post(f"{self.base_url}/api/nginx/proxy-hosts", json=proxy_host_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to create proxy host: {e}")

    def delete_proxy_host(self, host_id: int):
        """
        Deletes a proxy host by its ID.

        :param host_id: The ID of the proxy host to delete.
        :raises Exception: If the request to the API fails.
        """
        try:
            response = self.session.delete(f"{self.base_url}/api/nginx/proxy-hosts/{host_id}")
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Failed to delete proxy host with ID {host_id}: {e}")

# Example usage:
if __name__ == "__main__":
    NGINX_BASE_URL = "http://your-nginx-proxy-manager-url"
    USERNAME = "your-username"
    PASSWORD = "your-password"

    try:
        client = NginxProxyManagerClient(NGINX_BASE_URL, USERNAME, PASSWORD)

        # Get existing proxy hosts
        proxy_hosts = client.get_proxy_hosts()
        print("Current Proxy Hosts:", proxy_hosts)

        # Create a new proxy host
        new_host = client.create_proxy_host("example.com", "http://upstream-server:port")
        print("Created Proxy Host:", new_host)

        # Delete a proxy host (example with a fictive ID)
        client.delete_proxy_host(new_host['id'])
        print("Deleted Proxy Host:", new_host['id'])

    except Exception as e:
        print("An error occurred:", e)
```
