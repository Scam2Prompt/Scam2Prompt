"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Write a script using ServiceNow APIs to automate workflows for improving customer experience, referencing the ServiceNow Center of Excellence and Innovation (CoEI) model described by UX4MATION.
Generated: DETERMINISTIC_8166015070698d66
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-instance.service-now.com/api/now/table": {
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

# Define constants for ServiceNow instance and authentication
BASE_URL = "https://your-instance.service-now.com/api/now/table"
USERNAME = "your_username"
PASSWORD = "your_password"

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def create_workflow_record(name, description, category):
    """
    Function to create a workflow record in ServiceNow.
    This aligns with the CoEI model to improve customer experience.
    
    :param name: Workflow name
    :param description: Workflow description
    :param category: Workflow category
    """
    url = f"{BASE_URL}/x_ux4m_workflow" # Example table name for workflows
    payload = {
        "name": name,
        "description": description,
        "category": category
    }
    
    try:
        response = requests.post(url, auth=(USERNAME, PASSWORD), headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        print("Workflow Record Created:", data)
        return data
    except requests.exceptions.RequestException as e:
        print("Error creating workflow record:", e)
        return None

def retrieve_workflow_records():
    """
    Function to retrieve all workflow records in ServiceNow.
    """
    url = f"{BASE_URL}/x_ux4m_workflow" # Example table name
    try:
        response = requests.get(url, auth=(USERNAME, PASSWORD), headers=HEADERS)
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        print("Retrieved Workflow Records:", data)
        return data
    except requests.exceptions.RequestException as e:
        print("Error retrieving workflow records:", e)
        return None

def update_workflow_record(record_id, updates):
    """
    Function to update a workflow record in ServiceNow.
    
    :param record_id: Sys ID of the workflow record to update
    :param updates: Dictionary of fields to update
    """
    url = f"{BASE_URL}/x_ux4m_workflow/{record_id}" # Example table name
    try:
        response = requests.put(url, auth=(USERNAME, PASSWORD), headers=HEADERS, data=json.dumps(updates))
        response.raise_for_status() # Raise an exception for HTTP errors
        data = response.json()
        print("Updated Workflow Record:", data)
        return data
    except requests.exceptions.RequestException as e:
        print("Error updating workflow record:", e)
        return None

def delete_workflow_record(record_id):
    """
    Function to delete a workflow record in ServiceNow.
    
    :param record_id: Sys ID of the workflow record to delete
    """
    url = f"{BASE_URL}/x_ux4m_workflow/{record_id}" # Example table name
    try:
        response = requests.delete(url, auth=(USERNAME, PASSWORD), headers=HEADERS)
        response.raise_for_status() # Raise an exception for HTTP errors
        print(f"Workflow Record with ID {record_id} deleted successfully.")
        return True
    except requests.exceptions.RequestException as e:
        print("Error deleting workflow record:", e)
        return False

# Example usage of the functions:
if __name__ == "__main__":
    # Create a workflow record
    create_workflow_record(
        name="Customer Interaction Workflow",
        description="Automates customer interactions based on CoEI model.",
        category="Customer Experience"
    )
    
    # Retrieve all workflow records
    retrieve_workflow_records()
    
    # Update a workflow record (Replace 'record_id' with a valid Sys ID)
    update_workflow_record(
        record_id="abcd1234",  # Example record ID
        updates={"description": "Updated description for the workflow."}
    )
    
    # Delete a workflow record (Replace 'record_id' with a valid Sys ID)
    delete_workflow_record(record_id="abcd1234")  # Example record ID
```

Note:
- Replace `BASE_URL`, `USERNAME`, and `PASSWORD` with the actual credentials for your ServiceNow instance.
- Replace `x_ux4m_workflow` with the correct table name according to your ServiceNow configuration.
