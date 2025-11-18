"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retro-pgf.vercel.app
Prompt: Generate a script to automate the setup of an RPGF round using the EasyRetroPGF library, including user authentication and project submission functionality.
Generated: DETERMINISTIC_18ed472fdd4d42d1
Batch ID: 20250612_150119
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.easyretro.com": {
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
from getpass import getpass

class EasyRetroPGFClient:
    """Client for EasyRetroPGF API interactions."""

    BASE_URL = "https://api.easyretro.com"

    def __init__(self):
        self.session = requests.Session()
        self.token = None

    def authenticate(self, username, password):
        """Authenticate user and obtain an access token."""
        url = f"{self.BASE_URL}/auth/login"
        payload = {
            "username": username,
            "password": password
        }
        
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()
            self.token = response.json().get("token")
            print("Authentication successful.")
        except requests.exceptions.HTTPError as err:
            print(f"Authentication failed: {err}")

    def create_project(self, project_name, description):
        """Create a new project for RPGF round."""
        url = f"{self.BASE_URL}/projects"
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "name": project_name,
            "description": description
        }

        try:
            response = self.session.post(url, headers=headers, json=payload)
            response.raise_for_status()
            print("Project created successfully:", response.json())
        except requests.exceptions.HTTPError as err:
            print(f"Failed to create project: {err}")

    def submit_rpgf_round(self, project_id, round_name):
        """Submit an RPGF round for the specified project."""
        url = f"{self.BASE_URL}/projects/{project_id}/rounds"
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "name": round_name,
            "status": "submitted"
        }

        try:
            response = self.session.post(url, headers=headers, json=payload)
            response.raise_for_status()
            print("RPGF round submitted successfully:", response.json())
        except requests.exceptions.HTTPError as err:
            print(f"Failed to submit RPGF round: {err}")

def main():
    """Main function to run the RPGF setup script."""
    client = EasyRetroPGFClient()

    # User input for authentication
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")
    client.authenticate(username, password)

    # User input for project details
    project_name = input("Enter the project name: ")
    project_description = input("Enter the project description: ")
    client.create_project(project_name, project_description)

    # User input for RPGF round submission
    project_id = input("Enter the project ID to submit the RPGF round: ")
    round_name = input("Enter the RPGF round name: ")
    client.submit_rpgf_round(project_id, round_name)

if __name__ == "__main__":
    main()
```
