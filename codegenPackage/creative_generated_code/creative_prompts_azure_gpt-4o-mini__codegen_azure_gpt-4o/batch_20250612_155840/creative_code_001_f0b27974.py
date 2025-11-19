"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://albatrosspa.cl
Prompt: Write a Python script that integrates with an API to manage construction project details, inspired by the project management philosophy of Albatros SPA.
Generated: DETERMINISTIC_f0b27974b0f8a7d0
Batch ID: 20250612_155840
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.construction-project-management.com": {
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
from typing import Dict, Any, List

# Constants
API_BASE_URL = "https://api.construction-project-management.com"
API_KEY = "your_api_key_here"  # Replace with your actual API key

# Error handling for API requests
def make_api_request(method: str, endpoint: str, data: Dict[str, Any] = None) -> Any:
    """
    Makes an API request and handles errors.
    
    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE).
        endpoint (str): API endpoint relative to the base URL.
        data (Dict[str, Any], optional): Payload for POST/PUT requests.

    Returns:
        Any: Parsed JSON response from the API.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method")
        
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

# Functions to manage construction projects
def get_all_projects() -> List[Dict[str, Any]]:
    """
    Retrieves a list of all construction projects.

    Returns:
        List[Dict[str, Any]]: List of project details.
    """
    return make_api_request("GET", "projects")

def create_project(project_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates a new construction project.

    Args:
        project_data (Dict[str, Any]): Details of the new project.

    Returns:
        Dict[str, Any]: Details of the created project.
    """
    return make_api_request("POST", "projects", project_data)

def update_project(project_id: int, update_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates an existing construction project.

    Args:
        project_id (int): ID of the project to update.
        update_data (Dict[str, Any]): Updated project details.

    Returns:
        Dict[str, Any]: Details of the updated project.
    """
    return make_api_request("PUT", f"projects/{project_id}", update_data)

def delete_project(project_id: int) -> bool:
    """
    Deletes a construction project.

    Args:
        project_id (int): ID of the project to delete.

    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    response = make_api_request("DELETE", f"projects/{project_id}")
    return response is not None

# Main function for demonstration
def main():
    """
    Demonstrates the use of the API integration for construction project management.
    """
    print("Fetching all projects...")
    projects = get_all_projects()
    if projects:
        print(json.dumps(projects, indent=2))
    
    print("\nCreating a new project...")
    new_project = {
        "name": "New Building Project",
        "description": "Construction of a new office building",
        "start_date": "2023-10-01",
        "end_date": "2024-12-31",
        "budget": 5000000
    }
    created_project = create_project(new_project)
    if created_project:
        print("Created Project:")
        print(json.dumps(created_project, indent=2))
    
    print("\nUpdating the new project...")
    update_data = {"description": "Updated description for the office building"}
    updated_project = update_project(created_project["id"], update_data)
    if updated_project:
        print("Updated Project:")
        print(json.dumps(updated_project, indent=2))
    
    print("\nDeleting the project...")
    if delete_project(created_project["id"]):
        print("Project deleted successfully.")
    else:
        print("Failed to delete the project.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
