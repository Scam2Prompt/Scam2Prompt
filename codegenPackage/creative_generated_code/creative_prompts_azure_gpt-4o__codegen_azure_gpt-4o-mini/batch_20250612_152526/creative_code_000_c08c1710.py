"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Write a script using the Plesk API to automate the creation of a new web hosting account, including DNS and mail service configurations.
Generated: DETERMINISTIC_c08c17102ef6cb5f
Batch ID: 20250612_152526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.host}:8443/enterprise/control/agent.php": {
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
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{self.host}:8443/enterprise/control/agent.php"
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def _make_request(self, data):
        """Makes a request to the Plesk API and handles errors."""
        try:
            response = requests.post(self.base_url, headers=self.headers, data=data, auth=(self.username, self.password), verify=False)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def create_web_hosting(self, domain, username, password):
        """Creates a new web hosting account."""
        data = f"""
        <packet>
            <webspace>
                <add>
                    <name>{domain}</name>
                    <property>
                        <name>ip_address</name>
                        <value>shared</value>
                    </property>
                </add>
            </webspace>
            <domain>
                <add>
                    <name>{domain}</name>
                    <displayName>{domain}</displayName>
                    <webspace-id>1</webspace-id>  <!-- Change to your webspace ID -->
                    <property>
                        <name>htype</name>
                        <value>vrt_hst</value>
                    </property>
                    <property>
                        <name>www_root</name>
                        <value>httpdocs</value>
                    </property>
                </add>
            </domain>
            <ftp_user>
                <add>
                    <domain>{domain}</domain>
                    <login>{username}</login>
                    <password>{password}</password>
                    <home>false</home>
                </add>
            </ftp_user>
            <mail>
                <add>
                    <domain>{domain}</domain>
                    <name>{username}</name>
                    <password>{password}</password>
                </add>
            </mail>
        </packet>
        """
        result = self._make_request(data)
        if result:
            print("Web hosting account created successfully.")
        else:
            print("Failed to create web hosting account.")

if __name__ == "__main__":
    # Replace with your actual Plesk API credentials and domain details
    PLESK_HOST = 'your-plesk-host.com'
    PLESK_USERNAME = 'your-username'
    PLESK_PASSWORD = 'your-password'
    
    DOMAIN_NAME = 'example.com'
    FTP_USERNAME = 'ftpuser'
    FTP_PASSWORD = 'strongpassword'

    # Create an instance of the PleskAPI class and create a new web hosting account
    plesk_api = PleskAPI(PLESK_HOST, PLESK_USERNAME, PLESK_PASSWORD)
    plesk_api.create_web_hosting(DOMAIN_NAME, FTP_USERNAME, FTP_PASSWORD)
```
