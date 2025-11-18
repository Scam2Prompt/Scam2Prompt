"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xn--fixdfloat-23a.com
Prompt: Provide an example of using Plesk's API to manage server resources for traditional hosting environments.
Generated: DETERMINISTIC_1f4a2031c65a1dd4
Batch ID: 20250612_145459
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server.com": {
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
    def __init__(self, host, username, password):
        """
        Initializes the PleskAPI instance with the provided host, username, and password.
        
        :param host: Plesk server host URL
        :param username: API username
        :param password: API password
        """
        self.host = host
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/xml',
            'Accept': 'application/xml'
        }

    def make_request(self, method, endpoint, data=None):
        """
        Makes an API request to the Plesk server.
        
        :param method: HTTP method (GET, POST, etc.)
        :param endpoint: API endpoint
        :param data: XML data to send with the request (optional)
        :return: Response from the server
        """
        url = f'{self.host}/enterprise/control/route.php'
        try:
            response = requests.request(method, url, headers=self.headers, auth=(self.username, self.password), data=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error in API request: {e}")
            return None

    def get_server_info(self):
        """
        Retrieves information about the server resources.
        
        :return: Server information or None if an error occurs
        """
        data = """<?xml version="1.0"?>
        <packet>
            <server>
                <get>
                    <filter>
                        <status>0</status>
                    </filter>
                </get>
            </server>
        </packet>"""
        
        return self.make_request('POST', '/enterprise/control/route.php', data)

    def create_website(self, domain, client_id):
        """
        Creates a new website on the Plesk server.
        
        :param domain: The domain for the new website
        :param client_id: The client ID to associate with the website
        :return: Response from the server or None if an error occurs
        """
        data = f"""<?xml version="1.0"?>
        <packet>
            <webspace>
                <add>
                    <domain>
                        <name>{domain}</name>
                        <client-id>{client_id}</client-id>
                    </domain>
                </add>
            </webspace>
        </packet>"""
        
        return self.make_request('POST', '/enterprise/control/route.php', data)

    def delete_website(self, domain_id):
        """
        Deletes a website from the Plesk server.
        
        :param domain_id: The ID of the domain to delete
        :return: Response from the server or None if an error occurs
        """
        data = f"""<?xml version="1.0"?>
        <packet>
            <webspace>
                <del>
                    <domain>
                        <id>{domain_id}</id>
                    </domain>
                </del>
            </webspace>
        </packet>"""
        
        return self.make_request('POST', '/enterprise/control/route.php', data)


# Example Usage
if __name__ == "__main__":
    # Configure your Plesk server credentials
    PLESK_HOST = 'https://your-plesk-server.com'
    PLESK_USERNAME = 'your-username'
    PLESK_PASSWORD = 'your-password'
    
    plesk = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)
    
    # Get server info
    server_info = plesk.get_server_info()
    print(server_info)
    
    # Create a new website
    new_website_response = plesk.create_website('example.com', '1')
    print(new_website_response)
    
    # Delete a website
    delete_response = plesk.delete_website('2')
    print(delete_response)
```
