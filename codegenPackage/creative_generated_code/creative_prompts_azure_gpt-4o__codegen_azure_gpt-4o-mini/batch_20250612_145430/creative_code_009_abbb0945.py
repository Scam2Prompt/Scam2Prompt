"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ecosystem-n4emzjlz3-419labs.vercel.app
Prompt: Create a script to filter and display StarkNet projects based on whether they are on the mainnet, using relevant APIs or data sources.
Generated: DETERMINISTIC_abbb09453c1194d6
Batch ID: 20250612_145430
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io/projects": {
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

# Define the API endpoint for fetching StarkNet projects
API_URL = "https://api.starknet.io/projects"  # This is a placeholder URL

def fetch_projects():
    """
    Fetches StarkNet projects from the API and returns them as a list.
    
    Returns:
        list: A list of projects returned by the API.

    Raises:
        Exception: If the API request fails or returns an invalid response.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        projects = response.json()    # Parse the JSON response
        return projects
    except requests.RequestException as e:
        raise Exception(f"Error fetching projects: {e}")

def filter_mainnet_projects(projects):
    """
    Filters projects to return only those that are on the mainnet.

    Args:
        projects (list): A list of projects to filter.

    Returns:
        list: A list of projects that are on the mainnet.
    """
    mainnet_projects = [project for project in projects if project.get("network") == "mainnet"]
    return mainnet_projects

def display_projects(projects):
    """
    Displays the filtered projects in a user-friendly format.

    Args:
        projects (list): A list of projects to display.
    """
    if not projects:
        print("No projects found on the mainnet.")
        return

    print("StarkNet Projects on Mainnet:")
    for project in projects:
        print(f"- {project['name']}: {project['description']}")
        
def main():
    """
    Main function to execute the script.
    Fetches, filters, and displays StarkNet projects on the mainnet.
    """
    try:
        projects = fetch_projects()               # Step 1: Fetch projects
        mainnet_projects = filter_mainnet_projects(projects)  # Step 2: Filter projects
        display_projects(mainnet_projects)        # Step 3: Display filtered projects
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
