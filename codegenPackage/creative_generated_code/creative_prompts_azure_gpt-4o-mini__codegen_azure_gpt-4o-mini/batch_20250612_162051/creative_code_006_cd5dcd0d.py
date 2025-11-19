"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ux4mation.com
Prompt: Write a tutorial on using ServiceNow for managing business relationship processes effectively.
Generated: DETERMINISTIC_cd5dcd0dda941155
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

```python
"""
ServiceNow Business Relationship Management (BRM) Tutorial
=========================================================

This script outlines the basic methods for managing business relationship processes 
effectively using ServiceNow's REST API. 

Requirements:
- Python 3.x
- `requests` library (install via `pip install requests`)

Usage:
- The script demonstrates how to create, read, update, and delete BRM records in ServiceNow.
"""

import requests
import json

# Set your ServiceNow instance details
INSTANCE = 'https://your_instance.service-now.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Define the headers for the API requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Base URL for the Business Relationship Management table
BRM_TABLE_URL = f"{INSTANCE}/api/now/table/business_relationship"

def create_brm_record(data):
    """
    Create a new Business Relationship Management record.

    Args:
    - data (dict): A dictionary containing the necessary data to create a BRM record.

    Returns:
    - dict: The response from the ServiceNow API.
    """
    try:
        response = requests.post(BRM_TABLE_URL, auth=(USERNAME, PASSWORD), headers=HEADERS, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")  # Log the error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other errors


def get_brm_record(record_id):
    """
    Retrieve a Business Relationship Management record by its ID.

    Args:
    - record_id (str): The ID of the BRM record to retrieve.

    Returns:
    - dict: The response from the ServiceNow API.
    """
    try:
        response = requests.get(f"{BRM_TABLE_URL}/{record_id}", auth=(USERNAME, PASSWORD), headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def update_brm_record(record_id, data):
    """
    Update an existing Business Relationship Management record.

    Args:
    - record_id (str): The ID of the BRM record to update.
    - data (dict): The updated data for the BRM record.

    Returns:
    - dict: The response from the ServiceNow API.
    """
    try:
        response = requests.patch(f"{BRM_TABLE_URL}/{record_id}", auth=(USERNAME, PASSWORD), headers=HEADERS, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def delete_brm_record(record_id):
    """
    Delete a Business Relationship Management record by its ID.

    Args:
    - record_id (str): The ID of the BRM record to delete.

    Returns:
    - dict: The response from the ServiceNow API.
    """
    try:
        response = requests.delete(f"{BRM_TABLE_URL}/{record_id}", auth=(USERNAME, PASSWORD), headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


# Example Usage
if __name__ == "__main__":
    # Sample data for creating a BRM record
    sample_data = {
        "name": "New Business Relationship",
        "description": "This relationship is about managing business processes.",
        "status": "Active"
    }
    
    # Create a new BRM record
    new_record = create_brm_record(sample_data)
    print("Created BRM Record:", new_record)

    # Assuming the new record ID is obtained from the response
    record_id = new_record.get('result', {}).get('sys_id')

    # Retrieve the BRM record by ID
    retrieved_record = get_brm_record(record_id)
    print("Retrieved BRM Record:", retrieved_record)

    # Update the BRM record
    updated_data = {"status": "Inactive"}
    updated_record = update_brm_record(record_id, updated_data)
    print("Updated BRM Record:", updated_record)

    # Delete the BRM record
    deleted_record_response = delete_brm_record(record_id)
    print("Deleted BRM Record Response:", deleted_record_response)
```
