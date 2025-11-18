"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Create a tutorial for using the Plesk API to manage DNS records programmatically for multiple domains hosted on the platform.
Generated: DETERMINISTIC_d7e7861135393c42
Batch ID: 20250612_152526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com:8443": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-plesk-server:8443": {
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
    A class to interact with the Plesk API for managing DNS records.
    """

    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI with the given host, username, and password.

        :param host: The Plesk server URL (e.g., https://example.com:8443)
        :param username: The Plesk API username
        :param password: The Plesk API password
        """
        self.host = host
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/xml'
        }

    def _send_request(self, method, endpoint, data=None):
        """
        Sends a request to the Plesk API.

        :param method: The HTTP method (e.g., 'GET', 'POST')
        :param endpoint: The API endpoint to send the request to
        :param data: The XML data to send with the request (optional)
        :return: The response from the API
        """
        url = f"{self.host}/enterprise/control/agent.php"
        response = requests.request(method, url, headers=self.headers, data=data, auth=(self.username, self.password))

        # Raise an error for bad responses
        try:
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

        return response

    def list_dns_records(self, domain):
        """
        Lists DNS records for the specified domain.

        :param domain: The domain to list DNS records for
        :return: The list of DNS records or None if an error occurred
        """
        # Construct the request XML
        data = f"""
        <packet>
            <dns>
                <get>
                    <filter>
                        <domain>{domain}</domain>
                    </filter>
                    <dataset>
                        <dns>
                            <domain/>
                            <type/>
                            <host/>
                            <value/>
                            <ttl/>
                        </dns>
                    </dataset>
                </get>
            </dns>
        </packet>
        """
        
        response = self._send_request('POST', 'dns/get', data)
        return response.content if response else None

    def add_dns_record(self, domain, record_type, host, value, ttl=3600):
        """
        Adds a DNS record for the specified domain.

        :param domain: The domain to add the DNS record to
        :param record_type: The type of DNS record (e.g., 'A', 'CNAME')
        :param host: The host name for the DNS record
        :param value: The value for the DNS record
        :param ttl: Time to live for the DNS record (default is 3600 seconds)
        :return: True if the operation was successful, False otherwise
        """
        # Construct the request XML
        data = f"""
        <packet>
            <dns>
                <add>
                    <domain>{domain}</domain>
                    <type>{record_type}</type>
                    <host>{host}</host>
                    <value>{value}</value>
                    <ttl>{ttl}</ttl>
                </add>
            </dns>
        </packet>
        """
        
        response = self._send_request('POST', 'dns/add', data)
        return response is not None

    def delete_dns_record(self, domain, record_id):
        """
        Deletes a DNS record by its ID for the specified domain.

        :param domain: The domain from which to delete the DNS record
        :param record_id: The ID of the DNS record to delete
        :return: True if the operation was successful, False otherwise
        """
        # Construct the request XML
        data = f"""
        <packet>
            <dns>
                <del>
                    <id>{record_id}</id>
                </del>
            </dns>
        </packet>
        """
        
        response = self._send_request('POST', 'dns/delete', data)
        return response is not None

# Example usage:
if __name__ == "__main__":
    # Replace with your Plesk server details
    PLESK_HOST = 'https://your-plesk-server:8443'
    PLESK_USERNAME = 'your-username'
    PLESK_PASSWORD = 'your-password'

    plesk_api = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)

    # Example: List DNS records
    domain_to_query = 'example.com'
    dns_records = plesk_api.list_dns_records(domain_to_query)
    if dns_records:
        print("DNS Records:", dns_records)

    # Example: Add a DNS record
    success = plesk_api.add_dns_record(domain_to_query, 'A', 'newhost', '192.168.1.10')
    print("Add DNS Record Success:", success)

    # Example: Delete a DNS record (replace 'record_id' with the actual ID)
    record_id_to_delete = 12345
    success = plesk_api.delete_dns_record(domain_to_query, record_id_to_delete)
    print("Delete DNS Record Success:", success)
```
