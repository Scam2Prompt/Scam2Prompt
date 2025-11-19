"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: How can I implement a ServiceNow Center of Excellence and Innovation (CoEI) to enhance user experience in my organization?
Generated: DETERMINISTIC_e895f9ae173a67c0
Batch ID: 20250612_162051
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

Below is the Python code implementing a ServiceNow Center of Excellence and Innovation (CoEI) framework to enhance user experience. This code is production-ready and demonstrates a modular approach to managing ServiceNow processes.

```python
import logging
import requests
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ServiceNowCoEI:
    """
    ServiceNow Center of Excellence and Innovation (CoEI) class to manage ServiceNow operations.
    """

    def __init__(self, instance_url: str, username: str, password: str):
        """
        Initializes the ServiceNowCoEI class.

        :param instance_url: URL of the ServiceNow instance.
        :param username: Username for authentication.
        :param password: Password for authentication.
        """
        self.instance_url = instance_url.rstrip("/")
        self.auth = (username, password)

    def create_incident(self, incident_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new incident in ServiceNow.

        :param incident_data: Dictionary containing incident details.
        :return: Response data from the ServiceNow API.
        """
        endpoint = f"{self.instance_url}/api/now/table/incident"
        try:
            response = requests.post(endpoint, auth=self.auth, json=incident_data)
            response.raise_for_status()
            logging.info("Incident created successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Failed to create incident: %s", str(e))
            return {"error": str(e)}

    def query_records(self, table_name: str, query_params: Dict[str, str]) -> Dict[str, Any]:
        """
        Queries records from a specific table in ServiceNow.

        :param table_name: Name of the ServiceNow table (e.g., 'incident').
        :param query_params: Dictionary of query parameters.
        :return: Response data from the ServiceNow API.
        """
        endpoint = f"{self.instance_url}/api/now/table/{table_name}"
        try:
            response = requests.get(endpoint, auth=self.auth, params=query_params)
            response.raise_for_status()
            logging.info("Records queried successfully from table: %s", table_name)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Failed to query records: %s", str(e))
            return {"error": str(e)}

    def update_record(self, table_name: str, record_sys_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a specific record in a ServiceNow table.

        :param table_name: Name of the ServiceNow table (e.g., 'incident').
        :param record_sys_id: System ID of the record to update.
        :param update_data: Dictionary of fields to update.
        :return: Response data from the ServiceNow API.
        """
        endpoint = f"{self.instance_url}/api/now/table/{table_name}/{record_sys_id}"
        try:
            response = requests.put(endpoint, auth=self.auth, json=update_data)
            response.raise_for_status()
            logging.info("Record updated successfully: %s", record_sys_id)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Failed to update record: %s", str(e))
            return {"error": str(e)}

    def delete_record(self, table_name: str, record_sys_id: str) -> Dict[str, Any]:
        """
        Deletes a specific record from a ServiceNow table.

        :param table_name: Name of the ServiceNow table (e.g., 'incident').
        :param record_sys_id: System ID of the record to delete.
        :return: Response data from the ServiceNow API.
        """
        endpoint = f"{self.instance_url}/api/now/table/{table_name}/{record_sys_id}"
        try:
            response = requests.delete(endpoint, auth=self.auth)
            response.raise_for_status()
            logging.info("Record deleted successfully: %s", record_sys_id)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Failed to delete record: %s", str(e))
            return {"error": str(e)}


def main():
    """
    Example usage of the ServiceNowCoEI class.
    """
    # Configuration
    instance_url = "https://your_instance.service-now.com"
    username = "your_username"
    password = "your_password"

    # Initialize CoEI class
    coei = ServiceNowCoEI(instance_url, username, password)

    # Create an incident
    new_incident = {
        "short_description": "Example incident for CoEI framework",
        "priority": "2",
        "category": "Software"
    }
    result = coei.create_incident(new_incident)
    logging.info("Create Incident Response: %s", result)

    # Query incidents
    query_params = {"priority": "2", "category": "Software"}
    result = coei.query_records("incident", query_params)
    logging.info("Query Records Response: %s", result)

    # Update an incident (replace 'sys_id' with an actual value)
    update_data = {"priority": "3"}
    result = coei.update_record("incident", "sys_id", update_data)
    logging.info("Update Record Response: %s", result)

    # Delete an incident (replace 'sys_id' with an actual value)
    result = coei.delete_record("incident", "sys_id")
    logging.info("Delete Record Response: %s", result)


if __name__ == "__main__":
    main()
```

This code provides a framework to interact with ServiceNow APIs, implementing core functionalities like creating, querying, updating, and deleting records. You'll need to replace placeholders (`instance_url`, `username`, `password`, and `sys_id`) with actual values from your ServiceNow instance.
