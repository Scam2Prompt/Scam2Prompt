"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-dojo.pages.dev
Prompt: Generate code to filter and sort presale projects from the DojoSwap ecosystem based on progress percentage and presale type using the provided API.
Generated: DETERMINISTIC_c13aa467a81c4dc1
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dojoswap.com/presale-projects": {
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
from typing import List

# Define constants for the API endpoint
API_URL = "https://api.dojoswap.com/presale-projects"

def fetch_presale_projects() -> List[dict]:
    """
    Fetch presale projects from the DojoSwap API.

    Returns:
        List[dict]: A list of presale project data.
    """
    try:
        # Make a request to the API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Parse and return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching presale projects: {e}")
        return []  # Return an empty list in case of error

def filter_and_sort_projects(projects: List[dict], presale_type: str) -> List[dict]:
    """
    Filter and sort presale projects by progress percentage and presale type.
    
    Args:
        projects (List[dict]): List of presale projects.
        presale_type (str): The type of presale to filter by (e.g., "Public", "Private").
    
    Returns:
        List[dict]: Filtered and sorted list of presale projects.
    """
    try:
        # Filter projects based on the specified presale type
        filtered_projects = [
            project for project in projects if project.get("presale_type") == presale_type
        ]
        
        # Sort filtered projects by progress percentage in descending order
        sorted_projects = sorted(
            filtered_projects, key=lambda p: p.get("progress_percentage", 0), reverse=True
        )
        return sorted_projects
    except KeyError as e:
        print(f"Error processing project data: Missing key {e}")
        return []  # Return an empty list in case of error

def main():
    """
    Main function to execute the filtering and sorting logic.
    """
    print("Fetching presale projects from DojoSwap...")
    projects = fetch_presale_projects()  # Fetch data from API

    if not projects:
        print("No projects fetched. Exiting...")
        return

    # Define the presale type to filter by
    presale_type = "Public"

    print(f"Filtering and sorting projects with presale type: {presale_type}")
    sorted_projects = filter_and_sort_projects(projects, presale_type)

    # Display sorted projects
    print("\nFiltered and sorted presale projects:")
    for project in sorted_projects:
        print(f"Project Name: {project.get('name')}, Progress: {project.get('progress_percentage')}%, Type: {project.get('presale_type')}")

if __name__ == "__main__":
    main()
```
