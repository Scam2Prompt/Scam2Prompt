"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zkisync.com
Prompt: Explain how to set up a GitLab repository and manage user permissions effectively.
Generated: DETERMINISTIC_82262c0120f4be9e
Batch ID: 20250612_163807
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import subprocess
import os

class GitLabRepoManager:
    """
    A class to manage GitLab repositories and user permissions.
    """

    def __init__(self, gitlab_url, private_token):
        """
        Initializes the GitLabRepoManager with a given GitLab URL and a private token.

        :param gitlab_url: URL of the GitLab instance
        :param private_token: Personal access token for authentication
        """
        self.gitlab_url = gitlab_url
        self.private_token = private_token

    def create_repository(self, repo_name):
        """
        Creates a new GitLab repository.

        :param repo_name: Name of the repository to be created
        :raises Exception: If the repository creation fails
        """
        try:
            response = subprocess.run(
                [
                    "curl",
                    "--request", "POST",
                    f"{self.gitlab_url}/api/v4/projects?name={repo_name}",
                    "--header", f"PRIVATE-TOKEN: {self.private_token}"
                ],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"Repository '{repo_name}' created successfully.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to create repository: {e.stderr.strip()}")

    def manage_user_permissions(self, repo_name, user_id, access_level):
        """
        Manages user permissions for a given repository.

        :param repo_name: Name of the repository
        :param user_id: ID of the user to manage permissions for
        :param access_level: Desired access level (e.g., 'developer', 'maintainer')
        :raises Exception: If the permission management fails
        """
        access_levels = {
            'guest': 10,
            'reporter': 20,
            'developer': 30,
            'maintainer': 40,
            'owner': 50
        }

        if access_level not in access_levels:
            raise ValueError("Invalid access level provided.")

        try:
            response = subprocess.run(
                [
                    "curl",
                    "--request", "POST",
                    f"{self.gitlab_url}/api/v4/projects/{repo_name}/members",
                    "--header", f"PRIVATE-TOKEN: {self.private_token}",
                    "--data", f"user_id={user_id}&access_level={access_levels[access_level]}"
                ],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"User {user_id} granted {access_level} access to '{repo_name}'.")
        except subprocess.CalledProcessError as e:
            raise Exception(f"Failed to manage user permissions: {e.stderr.strip()}")

# Example usage
if __name__ == "__main__":
    GITLAB_URL = os.getenv('GITLAB_URL')  # GitLab URL from environment variable
    PRIVATE_TOKEN = os.getenv('PRIVATE_TOKEN')  # Private token from environment variable

    manager = GitLabRepoManager(GITLAB_URL, PRIVATE_TOKEN)

    # Create a new repository
    manager.create_repository("my_new_repo")

    # Manage user permissions
    manager.manage_user_permissions("my_new_repo", user_id=123456, access_level='developer')
```
