"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Generate a Python script that utilizes a project management API to track construction projects in the civil engineering sector, focusing on heavy construction and industrial projects.
Generated: DETERMINISTIC_669e9184cb8fee73
Batch ID: 20250612_155223
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1": {
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
Python Script to Interact with a Project Management API for Tracking Construction Projects
Focus: Heavy Construction and Industrial Projects
Requirements: Python 3.7+
"""

import requests
import logging
from typing import List, Dict, Any

# Setup logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
API_BASE_URL = "https://api.example.com/v1"  # Replace with actual API base URL
API_KEY = "your_api_key_here"               # Replace with your API key
TIMEOUT = 10                                # Timeout for API requests in seconds

# Function to handle API requests
def make_api_request(endpoint: str, method: str = "GET", payload: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Makes an API request to the project management system.

    :param endpoint: API endpoint (relative to API_BASE_URL).
    :param method: HTTP method to use (GET, POST, etc.).
    :param payload: Data to send in the request body (for POST/PUT requests).
    :return: JSON response as a dictionary.
    """
    url = f"{API_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload, timeout=TIMEOUT)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=payload, timeout=TIMEOUT)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, timeout=TIMEOUT)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return {"error": str(e)}

# Function to list projects
def list_projects() -> List[Dict[str, Any]]:
    """
    Retrieves the list of all projects.

    :return: List of projects as dictionaries.
    """
    endpoint = "/projects"
    response = make_api_request(endpoint)
    if "error" in response:
        logging.error("Failed to retrieve projects.")
        return []
    return response.get("data", [])

# Function to create a new project
def create_project(project_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates a new project in the system.

    :param project_data: Dictionary containing project details (e.g., name, type, start_date).
    :return: Response from the API.
    """
    endpoint = "/projects"
    response = make_api_request(endpoint, method="POST", payload=project_data)
    if "error" in response:
        logging.error("Failed to create project.")
    return response

# Function to update a project
def update_project(project_id: str, updated_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates an existing project.

    :param project_id: ID of the project to update.
    :param updated_data: Dictionary with updated project details.
    :return: Response from the API.
    """
    endpoint = f"/projects/{project_id}"
    response = make_api_request(endpoint, method="PUT", payload=updated_data)
    if "error" in response:
        logging.error(f"Failed to update project with ID {project_id}.")
    return response

# Function to delete a project
def delete_project(project_id: str) -> Dict[str, Any]:
    """
    Deletes a project from the system.

    :param project_id: ID of the project to delete.
    :return: Response from the API.
    """
    endpoint = f"/projects/{project_id}"
    response = make_api_request(endpoint, method="DELETE")
    if "error" in response:
        logging.error(f"Failed to delete project with ID {project_id}.")
    return response

# Example usage
if __name__ == "__main__":
    # List all projects
    projects = list_projects()
    logging.info(f"Projects retrieved: {projects}")

    # Create a new project
    new_project = {
        "name": "Industrial Park Construction",
        "type": "Heavy Construction",
        "start_date": "2024-01-15",
        "end_date": "2025-12-31",
        "budget": 1500000
    }
    created_project = create_project(new_project)
    logging.info(f"Created project: {created_project}")

    # Update a project
    if projects:
        project_id = projects[0]["id"]
        updated_data = {
            "end_date": "2026-01-31",
            "budget": 1600000
        }
        updated_project = update_project(project_id, updated_data)
        logging.info(f"Updated project: {updated_project}")

    # Delete a project
    if projects:
        project_id = projects[0]["id"]
        delete_response = delete_project(project_id)
        logging.info(f"Deleted project response: {delete_response}")
```
