"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Write a tutorial on using GitHub for version control, inspired by the various FOSS@RIT members who actively contribute to GitHub.
Generated: DETERMINISTIC_6b83de41009ae2c1
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is a Python script that demonstrates the usage of GitHub's API for version control tasks like creating repositories, listing repositories, and handling commits. This script uses the `requests` library for HTTP requests and interacts with GitHub's REST API. Note that you need a GitHub personal access token for authentication.

```python
import requests
import json
import os
from typing import Optional

# Constants
GITHUB_API_URL = "https://api.github.com"
TOKEN_ENV_VARIABLE = "GITHUB_TOKEN"  # Set your GitHub token in environment variable

# Helper function to load the GitHub token securely
def load_github_token() -> str:
    """
    Load the GitHub personal access token from an environment variable.
    Returns:
        str: The GitHub token.
    Raises:
        ValueError: If the token is not found in the environment variables.
    """
    token = os.getenv(TOKEN_ENV_VARIABLE)
    if not token:
        raise ValueError(f"GitHub token not found in the environment variable '{TOKEN_ENV_VARIABLE}'!")
    return token

# Helper function to make authenticated requests
def make_request(
    endpoint: str, 
    method: str = "GET", 
    data: Optional[dict] = None
) -> dict:
    """
    Make an authenticated HTTP request to the GitHub API.
    Args:
        endpoint (str): The endpoint of the API.
        method (str): HTTP method, e.g., 'GET', 'POST', etc.
        data (Optional[dict]): Data to send in the request body.
    Returns:
        dict: Parsed JSON response from GitHub API.
    Raises:
        Exception: If the response has an error status code.
    """
    token = load_github_token()
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"{GITHUB_API_URL}/{endpoint}"

    response = requests.request(method, url, headers=headers, json=data)

    # Raise an exception for HTTP errors
    if response.status_code >= 400:
        raise Exception(f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}")

    return response.json()

# Function to list all repositories for the authenticated user
def list_repositories():
    """
    List all repositories for the authenticated GitHub user.
    Returns:
        None
    """
    print("Fetching repositories...")
    repos = make_request("user/repos")
    for repo in repos:
        print(f"- {repo['name']} (Private: {repo['private']}, URL: {repo['html_url']})")

# Function to create a new repository
def create_repository(repo_name: str, description: Optional[str] = None, private: bool = True):
    """
    Create a new repository on GitHub.
    Args:
        repo_name (str): Name of the repository.
        description (Optional[str]): Description of the repository.
        private (bool): Whether the repository is private.
    Returns:
        None
    """
    print(f"Creating repository '{repo_name}'...")
    repo_data = {
        "name": repo_name,
        "description": description or "",
        "private": private
    }
    response = make_request("user/repos", method="POST", data=repo_data)
    print(f"Repository '{repo_name}' created successfully! URL: {response['html_url']}")

# Function to delete a repository
def delete_repository(owner: str, repo_name: str):
    """
    Delete a repository from GitHub.
    Args:
        owner (str): GitHub username or organization name.
        repo_name (str): Name of the repository to delete.
    Returns:
        None
    """
    print(f"Deleting repository '{repo_name}'...")
    endpoint = f"repos/{owner}/{repo_name}"
    make_request(endpoint, method="DELETE")
    print(f"Repository '{repo_name}' deleted successfully.")

# Main tutorial function
def github_tutorial():
    """
    Tutorial function demonstrating GitHub API usage.
    Returns:
        None
    """
    print("Starting GitHub API tutorial...\n")

    # Step 1: List repositories
    print("Step 1: Listing repositories...\n")
    list_repositories()

    # Step 2: Create a new repository
    print("\nStep 2: Creating a repository...\n")
    new_repo_name = "github-api-tutorial-demo"
    create_repository(new_repo_name, description="Demo repository created via GitHub API.")

    # Step 3: Delete the repository (for cleanup purposes)
    print("\nStep 3: Cleaning up by deleting the repository...\n")
    username = "YOUR_GITHUB_USERNAME"  # Replace with your GitHub username
    delete_repository(username, new_repo_name)

    print("\nTutorial completed!")

# Entry-point for the script
if __name__ == "__main__":
    try:
        github_tutorial()
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes on Usage
1. Replace `"YOUR_GITHUB_USERNAME"` with your actual GitHub username in the `delete_repository` function call.
2. Store your GitHub personal access token in a secure environment variable named `GITHUB_TOKEN`.
3. Install the `requests` library if not already installed: `pip install requests`.
