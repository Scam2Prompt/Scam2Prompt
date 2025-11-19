"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bytnox.com
Prompt: Generate a code snippet for a project management tool that integrates with the Études Architect App for seamless collaboration among architects.
Generated: DETERMINISTIC_b52c5fe25ab51722
Batch ID: 20250612_160703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etudesarchitect.com/v1": {
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
from datetime import datetime

# Constants for Études Architect API
BASE_URL = "https://api.etudesarchitect.com/v1"
API_KEY = "your_api_key_here"  # Replace with your valid API key

# Custom exceptions for error handling
class ÉtudesArchitectAPIError(Exception):
    """Custom exception for Études Architect API errors."""
    pass

# Function to authenticate and validate API key
def authenticate_api_key(api_key):
    """
    Validates the provided API key with Études Architect API.
    """
    try:
        response = requests.get(f"{BASE_URL}/auth/validate", headers={"Authorization": f"Bearer {api_key}"})
        if response.status_code == 200:
            return True
        else:
            raise ÉtudesArchitectAPIError(f"API Key validation failed: {response.json().get('error', 'Unknown error')}")
    except requests.RequestException as e:
        raise ÉtudesArchitectAPIError(f"Network error during API key validation: {e}")

# Function to create a project in Études Architect
def create_project(name, description, start_date, end_date):
    """
    Creates a new project in Études Architect.

    Parameters:
        name (str): Name of the project.
        description (str): Project description.
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.

    Returns:
        dict: Details of the created project.
    """
    payload = {
        "name": name,
        "description": description,
        "start_date": start_date,
        "end_date": end_date
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.post(f"{BASE_URL}/projects", json=payload, headers=headers)
        if response.status_code == 201:  # HTTP Status Code for Created
            return response.json()
        else:
            raise ÉtudesArchitectAPIError(f"Failed to create project: {response.json().get('error', 'Unknown error')}")
    except requests.RequestException as e:
        raise ÉtudesArchitectAPIError(f"Network error during project creation: {e}")

# Function to list all projects
def list_projects():
    """
    Fetches the list of all projects in Études Architect.

    Returns:
        list: List of projects.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(f"{BASE_URL}/projects", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise ÉtudesArchitectAPIError(f"Failed to fetch projects: {response.json().get('error', 'Unknown error')}")
    except requests.RequestException as e:
        raise ÉtudesArchitectAPIError(f"Network error during project listing: {e}")

# Main script for demonstration purposes
if __name__ == "__main__":
    try:
        # Authenticate API key
        if authenticate_api_key(API_KEY):
            print("API Key validated successfully.")

        # Creating a new project
        project_name = "Modern Architecture Design"
        project_description = "Collaboration project for modern architectural designs."
        project_start_date = datetime.now().strftime("%Y-%m-%d")
        project_end_date = "2024-12-31"
        
        created_project = create_project(project_name, project_description, project_start_date, project_end_date)
        print("Project created successfully:", created_project)

        # Listing all projects
        projects = list_projects()
        print("Projects:", projects)

    except ÉtudesArchitectAPIError as api_error:
        print("API error occurred:", str(api_error))
    except Exception as general_error:
        print("An unexpected error occurred:", str(general_error))
```
