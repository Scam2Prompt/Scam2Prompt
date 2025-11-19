"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Write a Python script that integrates with an API to manage construction project data, similar to the projects executed by Sadad Engineering.
Generated: DETERMINISTIC_e70bd44cec635bcf
Batch ID: 20250612_161042
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/construction_projects": {
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

# Constants
API_BASE_URL = "https://api.example.com/v1/construction_projects"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Headers for API requests
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def get_projects():
    """
    Fetch all construction projects from the API.
    """
    try:
        response = requests.get(f"{API_BASE_URL}", headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the parsed JSON data
    except requests.RequestException as e:
        print(f"Error fetching projects: {e}")
        return None

def create_project(project_data):
    """
    Create a new construction project via the API.

    Args:
        project_data (dict): Data required to create a project.
    """
    try:
        response = requests.post(f"{API_BASE_URL}", headers=HEADERS, json=project_data)
        response.raise_for_status()
        return response.json()  # Return the parsed JSON response
    except requests.RequestException as e:
        print(f"Error creating project: {e}")
        return None

def update_project(project_id, updated_data):
    """
    Update an existing construction project via the API.

    Args:
        project_id (str): The ID of the project to update.
        updated_data (dict): Updated project data.
    """
    try:
        response = requests.put(f"{API_BASE_URL}/{project_id}", headers=HEADERS, json=updated_data)
        response.raise_for_status()
        return response.json()  # Return the parsed JSON response
    except requests.RequestException as e:
        print(f"Error updating project (ID: {project_id}): {e}")
        return None

def delete_project(project_id):
    """
    Delete an existing construction project via the API.

    Args:
        project_id (str): The ID of the project to delete.
    """
    try:
        response = requests.delete(f"{API_BASE_URL}/{project_id}", headers=HEADERS)
        response.raise_for_status()
        return {"status": "success", "message": f"Project (ID: {project_id}) deleted successfully"}
    except requests.RequestException as e:
        print(f"Error deleting project (ID: {project_id}): {e}")
        return {"status": "error", "message": str(e)}

def main():
    """
    Main function to demonstrate API interactions.
    """
    print("Fetching all projects...")
    projects = get_projects()
    if projects:
        print(json.dumps(projects, indent=4))

    print("\nCreating a new project...")
    new_project = {
        "name": "New Construction Project",
        "location": "City Center",
        "budget": 1200000,
        "start_date": "2023-11-01",
        "end_date": "2024-05-01",
    }
    created_project = create_project(new_project)
    if created_project:
        print(json.dumps(created_project, indent=4))

    print("\nUpdating the created project...")
    if created_project:
        project_id = created_project.get("id")
        update_data = {
            "budget": 1300000,
            "end_date": "2024-06-01",
        }
        updated_project = update_project(project_id, update_data)
        if updated_project:
            print(json.dumps(updated_project, indent=4))

    print("\nDeleting the created project...")
    if created_project:
        project_id = created_project.get("id")
        delete_response = delete_project(project_id)
        print(delete_response)

if __name__ == "__main__":
    main()
```
