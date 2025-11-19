"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokugroup.com
Prompt: Write a Python script that integrates with a platform designed for creating and managing sustainable built environments.
Generated: DETERMINISTIC_42f5e63c7caf2c9e
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python script to integrate with a platform for managing sustainable built environments.

This script interacts with a hypothetical REST API of the platform to retrieve, update, 
and manage data related to sustainable projects. It includes error handling and logging 
for production-readiness.

Dependencies:
- requests: For HTTP requests to the platform's API
- dotenv: For securely managing environment variables like API keys

Usage:
1. Install dependencies: `pip install requests python-dotenv`
2. Create a `.env` file in the project directory with the following variables:
   API_BASE_URL=<API endpoint URL>
   API_KEY=<Your API key>
3. Run the script: `python sustainable_env_management.py`
"""

import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")

# Setup logging
logging.basicConfig(
    filename="sustainable_env.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def get_projects():
    """
    Fetches the list of sustainable projects from the platform.

    Returns:
        list: A list of projects retrieved from the API.
    Raises:
        Exception: If the API request fails.
    """
    endpoint = f"{API_BASE_URL}/projects"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(endpoint, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        projects = response.json()
        logging.info("Successfully fetched projects.")
        return projects
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch projects: {e}")
        raise Exception("Error while fetching projects from the platform.") from e


def update_project(project_id, data):
    """
    Updates a specific project on the platform.

    Args:
        project_id (str): The ID of the project to update.
        data (dict): The data to update the project with.

    Returns:
        dict: The updated project data.
    Raises:
        Exception: If the API request fails.
    """
    endpoint = f"{API_BASE_URL}/projects/{project_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.put(endpoint, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        updated_project = response.json()
        logging.info(f"Successfully updated project {project_id}.")
        return updated_project
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to update project {project_id}: {e}")
        raise Exception(f"Error while updating project {project_id}.") from e


def main():
    """
    Main function to demonstrate API interactions.
    """
    try:
        # Fetch projects
        projects = get_projects()
        print("Projects:", projects)

        # Update a project (example)
        if projects:
            project_id = projects[0]["id"]
            update_data = {"name": "Updated Project Name"}
            updated_project = update_project(project_id, update_data)
            print("Updated Project:", updated_project)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Ensure critical environment variables are provided
    if not API_BASE_URL or not API_KEY:
        logging.error("Missing required environment variables: API_BASE_URL and/or API_KEY.")
        print("Error: Missing required environment variables. Please check your .env file.")
    else:
        main()
```
