"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Suggest ServiceNow APIs for transforming digital operations into adaptive technology, focusing on technology excellence as discussed by UX4MATION.
Generated: DETERMINISTIC_7e6cf8923f9c7c35
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your_instance.service-now.com": {
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

class ServiceNowAPIClient:
    """
    A client for interacting with ServiceNow APIs to transform digital operations
    into adaptive technology.
    """

    def __init__(self, instance_url, username, password):
        """
        Initialize the ServiceNow API client.

        :param instance_url: The base URL of the ServiceNow instance
        :param username: ServiceNow username
        :param password: ServiceNow password
        """
        self.instance_url = instance_url
        self.username = username
        self.password = password

    def _make_request(self, method, endpoint, data=None):
        """
        Make an HTTP request to the ServiceNow API.

        :param method: HTTP method (GET, POST, PUT, DELETE)
        :param endpoint: API endpoint
        :param data: Data to be sent with the request (for POST, PUT)
        :return: JSON response from the ServiceNow API
        """
        url = f"{self.instance_url}/{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            if method == "GET":
                response = requests.get(url, auth=(self.username, self.password), headers=headers)
            elif method == "POST":
                response = requests.post(url, auth=(self.username, self.password), headers=headers, data=json.dumps(data))
            elif method == "PUT":
                response = requests.put(url, auth=(self.username, self.password), headers=headers, data=json.dumps(data))
            elif method == "DELETE":
                response = requests.delete(url, auth=(self.username, self.password), headers=headers)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
        except Exception as err:
            print(f"An error occurred: {err}")  # Log general error

        return None  # Return None if an error occurred

    def get_incidents(self):
        """
        Retrieve a list of incidents from ServiceNow.

        :return: List of incidents or None if an error occurs
        """
        return self._make_request("GET", "api/now/table/incident")

    def create_incident(self, incident_data):
        """
        Create a new incident in ServiceNow.

        :param incident_data: Dictionary containing incident details
        :return: Response from the ServiceNow API or None if an error occurs
        """
        return self._make_request("POST", "api/now/table/incident", incident_data)

    def update_incident(self, incident_id, incident_data):
        """
        Update an existing incident in ServiceNow.

        :param incident_id: ID of the incident to update
        :param incident_data: Dictionary containing updated incident details
        :return: Response from the ServiceNow API or None if an error occurs
        """
        return self._make_request("PUT", f"api/now/table/incident/{incident_id}", incident_data)

    def delete_incident(self, incident_id):
        """
        Delete an incident from ServiceNow.

        :param incident_id: ID of the incident to delete
        :return: Response from the ServiceNow API or None if an error occurs
        """
        return self._make_request("DELETE", f"api/now/table/incident/{incident_id}")

# Example usage:
if __name__ == "__main__":
    # Replace these with your actual ServiceNow instance details
    instance_url = "https://your_instance.service-now.com"
    username = "your_username"
    password = "your_password"

    client = ServiceNowAPIClient(instance_url, username, password)

    # Retrieve incidents
    incidents = client.get_incidents()
    print(incidents)

    # Create a new incident
    new_incident_data = {
        "short_description": "Example incident created via API",
        "description": "This incident is created for demonstration purposes."
    }
    new_incident = client.create_incident(new_incident_data)
    print(new_incident)

    # Example for updating an incident
    if new_incident and 'result' in new_incident:
        incident_id = new_incident['result']['sys_id']
        updated_incident_data = {
            "short_description": "Updated incident description"
        }
        updated_incident = client.update_incident(incident_id, updated_incident_data)
        print(updated_incident)

    # Example for deleting an incident
    if new_incident and 'result' in new_incident:
        client.delete_incident(incident_id)
```
