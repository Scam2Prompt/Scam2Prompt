"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Write a Python script that interacts with an API to fetch and display recent construction projects similar to those completed by ECOLUX, including details like location and project type.
Generated: DETERMINISTIC_ee4fcf3b239d3901
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.constructionprojects.com/v1/projects": {
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

class EcoluxConstructionAPI:
    """
    A class to interact with the Construction Projects API to fetch recent projects similar to ECOLUX.
    """
    
    BASE_URL = 'https://api.constructionprojects.com/v1/projects'  # Example base URL for the API

    def __init__(self, api_key):
        """
        Initialize the API client with the necessary API key.
        
        Parameters:
        api_key (str): The API key for authentication.
        """
        self.api_key = api_key

    def fetch_recent_projects(self):
        """
        Fetches recent construction projects from the API.
        
        Returns:
        list: A list of dictionaries containing project details.
        """
        try:
            response = requests.get(
                self.BASE_URL,
                headers={'Authorization': f'Bearer {self.api_key}'}
            )
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            projects = response.json().get('projects', [])
            return projects

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request exception occurred: {req_err}")  # Log other request exceptions
        except Exception as e:
            print(f"An error occurred: {e}")  # Log any other exceptions
        
        return []  # Return an empty list in case of an error

    def display_projects(self, projects):
        """
        Displays the project details in a formatted manner.
        
        Parameters:
        projects (list): A list of project dictionaries to display.
        """
        if not projects:
            print("No projects found.")
            return
        
        print(f"{'Location':<30} {'Project Type':<25} {'Project Name'}")
        print("=" * 80)

        for project in projects:
            location = project.get('location', 'N/A')
            project_type = project.get('type', 'N/A')
            project_name = project.get('name', 'N/A')
            print(f"{location:<30} {project_type:<25} {project_name}")

def main():
    """
    Main function to run the script.
    """
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    
    api_client = EcoluxConstructionAPI(api_key)
    
    # Fetch recent projects
    recent_projects = api_client.fetch_recent_projects()
    
    # Display the fetched projects
    api_client.display_projects(recent_projects)

if __name__ == "__main__":
    main()
```
