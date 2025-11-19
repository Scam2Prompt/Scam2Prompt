"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shinemedia.com.ng
Prompt: How can I use Brainwave.io to manage multiple remote teams and projects effectively?
Generated: DETERMINISTIC_dace537738e07b8e
Batch ID: 20250612_163640
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.brainwave.io": {
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

class BrainwaveAPI:
    """
    A class to interact with the Brainwave.io API for managing remote teams and projects.
    """

    BASE_URL = "https://api.brainwave.io"

    def __init__(self, api_key):
        """
        Initializes the BrainwaveAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Brainwave.io API.
        """
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_teams(self):
        """
        Retrieves a list of teams managed in Brainwave.io.

        Returns:
            list: A list of teams if successful, otherwise raises an Exception.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/teams", headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def create_project(self, team_id, project_name, project_description):
        """
        Creates a new project under a specified team.

        Args:
            team_id (str): The ID of the team to create the project under.
            project_name (str): The name of the new project.
            project_description (str): A brief description of the project.

        Returns:
            dict: The created project details if successful, otherwise raises an Exception.
        """
        project_data = {
            'name': project_name,
            'description': project_description,
            'team_id': team_id
        }
        try:
            response = requests.post(f"{self.BASE_URL}/projects", json=project_data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def assign_team_member(self, team_id, member_id):
        """
        Assigns a team member to a specific team.

        Args:
            team_id (str): The ID of the team to assign the member to.
            member_id (str): The ID of the member to be assigned.

        Returns:
            dict: The updated team details if successful, otherwise raises an Exception.
        """
        assignment_data = {
            'member_id': member_id
        }
        try:
            response = requests.post(f"{self.BASE_URL}/teams/{team_id}/members", json=assignment_data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")


# Example usage (this part should be outside of the class in actual usage):
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    brainwave_api = BrainwaveAPI(API_KEY)

    # Retrieve teams
    try:
        teams = brainwave_api.get_teams()
        print("Teams:", teams)
    except Exception as e:
        print("Error retrieving teams:", e)

    # Create a new project (example usage)
    try:
        new_project = brainwave_api.create_project("team_id_here", "New Project", "This is a test project.")
        print("Created Project:", new_project)
    except Exception as e:
        print("Error creating project:", e)

    # Assign a team member (example usage)
    try:
        updated_team = brainwave_api.assign_team_member("team_id_here", "member_id_here")
        print("Updated Team:", updated_team)
    except Exception as e:
        print("Error assigning team member:", e)
```
