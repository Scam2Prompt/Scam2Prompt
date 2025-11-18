"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://confinance.info
Prompt: Create a Python program to open issues in a repository for a conservation finance project, inspired by the repository functionality on https://confinance.info.
Generated: DETERMINISTIC_f4464be85459734c
Batch ID: 20250612_154428
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues": {
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
import json

class GitHubIssueManager:
    """
    A class to manage issues in a GitHub repository for a conservation finance project.
    """

    def __init__(self, repo_owner, repo_name, access_token):
        """
        Initialize the GitHubIssueManager.

        :param repo_owner: The owner of the GitHub repository.
        :param repo_name: The name of the GitHub repository.
        :param access_token: The GitHub Personal Access Token for authentication.
        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.access_token = access_token
        self.api_url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues"

    def create_issue(self, title, body):
        """
        Create a new issue in the specified repository.

        :param title: The title of the issue.
        :param body: The body content of the issue.
        :return: The response from the GitHub API.
        """
        # Prepare the issue data
        issue_data = {
            "title": title,
            "body": body
        }

        # Set up the headers for authentication
        headers = {
            "Authorization": f"token {self.access_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        try:
            # Send a POST request to create the issue
            response = requests.post(self.api_url, headers=headers, data=json.dumps(issue_data))
            response.raise_for_status()  # Raise an error for bad responses

            # Return the response JSON if successful
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors

        return None  # Return None if there was an error

if __name__ == "__main__":
    # Example usage
    GITHUB_ACCESS_TOKEN = "your_github_access_token"  # Replace with your access token
    REPO_OWNER = "your_repo_owner"  # Replace with the repository owner's name
    REPO_NAME = "your_repo_name"  # Replace with the repository name

    issue_manager = GitHubIssueManager(REPO_OWNER, REPO_NAME, GITHUB_ACCESS_TOKEN)

    # Create a new issue
    issue_title = "New Feature Request"
    issue_body = "We need to implement a new feature for tracking donations."

    created_issue = issue_manager.create_issue(issue_title, issue_body)

    if created_issue:
        print(f"Issue created successfully: {created_issue['html_url']}")
    else:
        print("Failed to create the issue.")
```
