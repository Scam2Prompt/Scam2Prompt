"""
Generated Code Metadata:
========================
Original URL: https://stonegarden.dev
Prompt: Provide an example of using Stonegarden.dev v0.2.1 for managing project versioning across multiple repositories.
Generated: DETERMINISTIC_30ad022aec89422c
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import subprocess
import json
from typing import List

class VersionManager:
    """
    A class to manage project versioning across multiple repositories using Stonegarden.dev.
    """

    def __init__(self, repos: List[str], version_file: str):
        """
        Initializes the VersionManager with a list of repositories and a version file.

        :param repos: List of repository paths.
        :param version_file: Path to the version file (JSON format).
        """
        self.repos = repos
        self.version_file = version_file
        self.version = self.load_version()

    def load_version(self) -> str:
        """
        Loads the current version from the version file.

        :return: The current version as a string.
        """
        try:
            with open(self.version_file, 'r') as file:
                data = json.load(file)
                return data.get("version", "0.0.0")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading version file: {e}")
            return "0.0.0"

    def update_version(self, new_version: str):
        """
        Updates the version in the version file and commits the change to all repositories.

        :param new_version: The new version to set.
        """
        self.version = new_version
        self.save_version()
        self.commit_version_to_repos()

    def save_version(self):
        """
        Saves the current version to the version file.
        """
        try:
            with open(self.version_file, 'w') as file:
                json.dump({"version": self.version}, file, indent=4)
        except IOError as e:
            print(f"Error saving version file: {e}")

    def commit_version_to_repos(self):
        """
        Commits the version change to all specified repositories.
        """
        for repo in self.repos:
            try:
                self._commit_version(repo)
            except Exception as e:
                print(f"Error committing version to {repo}: {e}")

    def _commit_version(self, repo: str):
        """
        Commits the version change to a specific repository.

        :param repo: The repository path.
        """
        # Change to the repository directory
        os.chdir(repo)

        # Add the version file to the staging area
        subprocess.run(["git", "add", self.version_file], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", f"Update version to {self.version}"], check=True)

        # Push the changes to the remote repository
        subprocess.run(["git", "push"], check=True)

        print(f"Version {self.version} committed to {repo}")

# Example usage
if __name__ == "__main__":
    # Define the repositories and version file
    repositories = [
        "/path/to/repo1",
        "/path/to/repo2",
        "/path/to/repo3"
    ]
    version_file_path = "/path/to/version.json"

    # Create a VersionManager instance
    version_manager = VersionManager(repos=repositories, version_file=version_file_path)

    # Update the version
    new_version = "1.0.0"
    version_manager.update_version(new_version)
```
