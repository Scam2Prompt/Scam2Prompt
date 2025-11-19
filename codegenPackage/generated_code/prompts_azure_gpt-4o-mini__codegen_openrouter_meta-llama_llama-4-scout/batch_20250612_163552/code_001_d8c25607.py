"""
Generated Code Metadata:
========================
Original URL: https://resolveprocess.com
Prompt: Write a code snippet that integrates Resolve Automation Exchange with a cloud service to streamline IT operations.
Generated: DETERMINISTIC_d8c2560726150b7d
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
import requests
from requests.auth import HTTPBasicAuth

class ResolveAutomationExchange:
    def __init__(self, resolve_url, resolve_api_key, resolve_username):
        """
        Initialize Resolve Automation Exchange API connection.

        Args:
        - resolve_url (str): URL of Resolve Automation Exchange instance.
        - resolve_api_key (str): API key for Resolve Automation Exchange.
        - resolve_username (str): Username for Resolve Automation Exchange.
        """
        self.resolve_url = resolve_url
        self.resolve_api_key = resolve_api_key
        self.resolve_username = resolve_username

    def get_auth_token(self):
        """
        Obtain authentication token for Resolve Automation Exchange.

        Returns:
        - auth_token (str): Authentication token.
        """
        try:
            response = requests.post(
                f"{self.resolve_url}/api/auth/token",
                auth=HTTPBasicAuth(self.resolve_username, self.resolve_api_key)
            )
            response.raise_for_status()
            return response.json()["token"]
        except requests.exceptions.RequestException as e:
            print(f"Error obtaining auth token: {e}")
            return None

    def create_incident(self, incident_data):
        """
        Create a new incident in Resolve Automation Exchange.

        Args:
        - incident_data (dict): Incident data.

        Returns:
        - incident_id (str): ID of created incident.
        """
        auth_token = self.get_auth_token()
        if auth_token is None:
            return None

        try:
            headers = {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
            response = requests.post(
                f"{self.resolve_url}/api/incidents",
                headers=headers,
                data=json.dumps(incident_data)
            )
            response.raise_for_status()
            return response.json()["id"]
        except requests.exceptions.RequestException as e:
            print(f"Error creating incident: {e}")
            return None


class CloudService:
    def __init__(self, cloud_service_url, cloud_service_api_key):
        """
        Initialize cloud service API connection.

        Args:
        - cloud_service_url (str): URL of cloud service instance.
        - cloud_service_api_key (str): API key for cloud service.
        """
        self.cloud_service_url = cloud_service_url
        self.cloud_service_api_key = cloud_service_api_key

    def get_instance_data(self, instance_id):
        """
        Retrieve instance data from cloud service.

        Args:
        - instance_id (str): ID of instance.

        Returns:
        - instance_data (dict): Instance data.
        """
        try:
            headers = {"Authorization": f"Bearer {self.cloud_service_api_key}", "Content-Type": "application/json"}
            response = requests.get(
                f"{self.cloud_service_url}/api/instances/{instance_id}",
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving instance data: {e}")
            return None


def integrate_resolve_with_cloud(resolve_url, resolve_api_key, resolve_username, cloud_service_url, cloud_service_api_key, instance_id):
    """
    Integrate Resolve Automation Exchange with cloud service.

    Args:
    - resolve_url (str): URL of Resolve Automation Exchange instance.
    - resolve_api_key (str): API key for Resolve Automation Exchange.
    - resolve_username (str): Username for Resolve Automation Exchange.
    - cloud_service_url (str): URL of cloud service instance.
    - cloud_service_api_key (str): API key for cloud service.
    - instance_id (str): ID of instance.

    Returns:
    - incident_id (str): ID of created incident.
    """
    resolve = ResolveAutomationExchange(resolve_url, resolve_api_key, resolve_username)
    cloud_service = CloudService(cloud_service_url, cloud_service_api_key)

    instance_data = cloud_service.get_instance_data(instance_id)
    if instance_data is None:
        return None

    incident_data = {
        "title": f"Instance {instance_id} issue",
        "description": json.dumps(instance_data)
    }

    incident_id = resolve.create_incident(incident_data)
    return incident_id


if __name__ == "__main__":
    resolve_url = os.environ.get("RESOLVE_URL")
    resolve_api_key = os.environ.get("RESOLVE_API_KEY")
    resolve_username = os.environ.get("RESOLVE_USERNAME")
    cloud_service_url = os.environ.get("CLOUD_SERVICE_URL")
    cloud_service_api_key = os.environ.get("CLOUD_SERVICE_API_KEY")
    instance_id = os.environ.get("INSTANCE_ID")

    incident_id = integrate_resolve_with_cloud(
        resolve_url, resolve_api_key, resolve_username, cloud_service_url, cloud_service_api_key, instance_id
    )
    print(f"Created incident with ID: {incident_id}")
```
