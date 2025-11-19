"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Write a code snippet to automate the deployment of a website using Plesk's API.
Generated: DETERMINISTIC_f285568165af6264
Batch ID: 20250612_161301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server.com:8443": {
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

class PleskDeployment:
    def __init__(self, host, username, password):
        """
        Initializes the PleskDeployment class with necessary credentials.

        :param host: The Plesk server URL.
        :param username: The Plesk API username.
        :param password: The Plesk API password.
        """
        self.host = host
        self.username = username
        self.password = password
        self.api_url = f"{host}/enterprise/control/agent.php"

    def make_request(self, data):
        """
        Makes a request to the Plesk API.

        :param data: The payload to be sent in the request.
        :return: The response from the Plesk API.
        """
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            response = requests.post(self.api_url, headers=headers, data=data, auth=(self.username, self.password))
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Plesk API: {e}")
            return None

    def deploy_website(self, domain, webspace_id):
        """
        Deploys a website using the Plesk API.

        :param domain: The domain name to be deployed.
        :param webspace_id: The ID of the webspace where the domain will be deployed.
        :return: The result of the deployment operation.
        """
        data = {
            'cmd': 'domain.add',
            'domain': {
                'name': domain,
                'webspace_id': webspace_id,
                'status': '0'  # 0 for active
            }
        }
        
        # Wrap the command in a request structure expected by Plesk
        payload = {
            'packet': {
                'domain': data
            }
        }

        response = self.make_request(json.dumps(payload))
        if response and 'errcode' not in response['packet']['domain']:
            print(f"Domain '{domain}' has been successfully deployed.")
            return response
        else:
            print(f"Failed to deploy domain '{domain}': {response['packet']['domain']['error']}")
            return None

if __name__ == "__main__":
    # Example usage
    HOST = "https://your-plesk-server.com:8443"
    USERNAME = "your_api_username"
    PASSWORD = "your_api_password"
    DOMAIN = "example.com"
    WEBSPACE_ID = 1  # Replace with actual webspace ID

    deployment = PleskDeployment(HOST, USERNAME, PASSWORD)
    deployment.deploy_website(DOMAIN, WEBSPACE_ID)
```
