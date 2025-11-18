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
  "https://{host}:8443": {
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

class PleskAPI:
    """
    Class to interact with the Plesk API for managing cloud hosting services.
    """

    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI with host, username, and password.
        
        :param host: Plesk server host
        :param username: API username
        :param password: API password
        """
        self.base_url = f"https://{host}:8443"
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.headers.update({'Content-Type': 'application/xml'})

    def add_domain(self, domain_name):
        """
        Adds a new domain to the Plesk server.
        
        :param domain_name: Name of the domain to add
        :return: Response from the API
        """
        try:
            payload = f"""
            <packet>
                <domain>
                    <add>
                        <name>{domain_name}</name>
                        <id>0</id>
                    </add>
                </domain>
            </packet>
            """
            response = self.session.post(f"{self.base_url}/enterprise/control/agent.php", data=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while adding domain: {e}")
            return None

    def list_domains(self):
        """
        Retrieves a list of domains from the Plesk server.
        
        :return: List of domains or None if there's an error
        """
        try:
            payload = """
            <packet>
                <domain>
                    <get>
                        <filter>
                            <status>0</status>
                        </filter>
                        <dataset>
                            <limit>0</limit>
                        </dataset>
                    </get>
                </domain>
            </packet>
            """
            response = self.session.post(f"{self.base_url}/enterprise/control/agent.php", data=payload)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while listing domains: {e}")
            return None

    def remove_domain(self, domain_id):
        """
        Removes a domain from the Plesk server.
        
        :param domain_id: ID of the domain to remove
        :return: Response from the API
        """
        try:
            payload = f"""
            <packet>
                <domain>
                    <delete>
                        <domain-id>{domain_id}</domain-id>
                    </delete>
                </domain>
            </packet>
            """
            response = self.session.post(f"{self.base_url}/enterprise/control/agent.php", data=payload)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while removing domain: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    # Replace with your actual Plesk server details
    HOST = "your-plesk-server.com"
    USERNAME = "your-username"
    PASSWORD = "your-password"

    plesk = PleskAPI(HOST, USERNAME, PASSWORD)

    # Add a new domain
    print(plesk.add_domain("example.com"))

    # List existing domains
    print(plesk.list_domains())

    # Remove a domain (replace '123' with actual domain ID)
    print(plesk.remove_domain(123))
```
