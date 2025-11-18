"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Write Python code to automate EPA environmental reporting tasks, including permit management and emergency plan creation, as described on the iSi Environmental website.
Generated: DETERMINISTIC_5061b0d849186b59
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

# Constants
DATA_DIRECTORY = "environmental_data"
PERMIT_FILE = "permits.json"
EMERGENCY_PLAN_FILE = "emergency_plan.json"

# Helper functions
def load_data(file_name):
    """
    Load JSON data from the given file.
    
    :param file_name: Name of the file to load data from
    :return: Parsed JSON data or an empty dictionary if the file does not exist
    """
    try:
        file_path = os.path.join(DATA_DIRECTORY, file_name)
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from {file_name}: {e}")

def save_data(file_name, data):
    """
    Save JSON data to the given file.
    
    :param file_name: Name of the file to save data to
    :param data: Dictionary to save as JSON
    """
    try:
        file_path = os.path.join(DATA_DIRECTORY, file_name)
        os.makedirs(DATA_DIRECTORY, exist_ok=True)  # Ensure the directory exists
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise IOError(f"Error saving data to {file_name}: {e}")

# Permit management functions
def add_permit(permit_id, facility_name, expiration_date):
    """
    Add a new permit to the system.
    
    :param permit_id: Unique identifier for the permit
    :param facility_name: Name of the facility associated with the permit
    :param expiration_date: Expiration date of the permit in YYYY-MM-DD format
    """
    permits = load_data(PERMIT_FILE)
    if permit_id in permits:
        raise ValueError(f"Permit ID {permit_id} already exists.")
    
    permits[permit_id] = {
        "facility_name": facility_name,
        "expiration_date": expiration_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_data(PERMIT_FILE, permits)
    print(f"Permit {permit_id} added successfully.")

def list_permits():
    """
    List all permits with their details.
    """
    permits = load_data(PERMIT_FILE)
    if not permits:
        print("No permits found.")
        return
    
    for permit_id, details in permits.items():
        print(f"Permit ID: {permit_id}")
        print(f"Facility Name: {details['facility_name']}")
        print(f"Expiration Date: {details['expiration_date']}")
        print(f"Created At: {details['created_at']}")
        print("-" * 20)

# Emergency plan creation functions
def create_emergency_plan(plan_id, facility_name, contact_info, procedures):
    """
    Create a new emergency plan.
    
    :param plan_id: Unique identifier for the emergency plan
    :param facility_name: Name of the facility associated with the plan
    :param contact_info: Emergency contact information
    :param procedures: List of procedures for emergency handling
    """
    emergency_plans = load_data(EMERGENCY_PLAN_FILE)
    if plan_id in emergency_plans:
        raise ValueError(f"Emergency Plan ID {plan_id} already exists.")
    
    emergency_plans[plan_id] = {
        "facility_name": facility_name,
        "contact_info": contact_info,
        "procedures": procedures,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_data(EMERGENCY_PLAN_FILE, emergency_plans)
    print(f"Emergency Plan {plan_id} created successfully.")

def list_emergency_plans():
    """
    List all emergency plans with their details.
    """
    emergency_plans = load_data(EMERGENCY_PLAN_FILE)
    if not emergency_plans:
        print("No emergency plans found.")
        return
    
    for plan_id, details in emergency_plans.items():
        print(f"Plan ID: {plan_id}")
        print(f"Facility Name: {details['facility_name']}")
        print(f"Contact Info: {details['contact_info']}")
        print(f"Procedures: {', '.join(details['procedures'])}")
        print(f"Created At: {details['created_at']}")
        print("-" * 20)

# Main function to demonstrate functionality
if __name__ == "__main__":
    try:
        # Example usage of permit management
        add_permit("P001", "Facility A", "2024-12-31")
        add_permit("P002", "Facility B", "2025-06-30")
        list_permits()
        
        # Example usage of emergency plan creation
        create_emergency_plan(
            "E001", 
            "Facility A", 
            "John Doe - 123-456-7890", 
            ["Evacuate building", "Call emergency services", "Secure hazardous materials"]
        )
        create_emergency_plan(
            "E002", 
            "Facility B", 
            "Jane Smith - 987-654-3210", 
            ["Activate alarm", "Contact fire department", "Provide first aid"]
        )
        list_emergency_plans()
    except Exception as e:
        print(f"Error: {e}")
```
