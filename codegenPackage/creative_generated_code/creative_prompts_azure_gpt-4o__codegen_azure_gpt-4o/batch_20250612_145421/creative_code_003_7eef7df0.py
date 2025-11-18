"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ryanml.github.io
Prompt: Provide examples of using Ryan Lanese's GitHub repositories for learning software engineering best practices.
Generated: DETERMINISTIC_7eef7df01b02039c
Batch ID: 20250612_145421
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

```python
"""
This script demonstrates how to interact with Ryan Lanese's GitHub repositories
to learn software engineering best practices. It fetches repository details
and provides insights into projects available for study. Replace the GitHub username
and personal access token with appropriate values before running the script.

Requirements:
- Python 3.7+
- Install `requests` library (`pip install requests`)
"""

import requests

# GitHub API base URL
GITHUB_API_BASE_URL = "https://api.github.com"

# Replace 'ryanlanese' with the actual GitHub username of interest
GITHUB_USERNAME = "ryanlanese"

# Replace 'your_personal_access_token' with your GitHub personal access token
# For increased API rate limits and access to private repositories (if applicable)
GITHUB_ACCESS_TOKEN = "your_personal_access_token"


def fetch_repositories(username):
    """
    Fetch all public repositories for the specified GitHub username.

    Args:
        username (str): GitHub username.

    Returns:
        list: List of repositories if successful, an empty list otherwise.
    """
    url = f"{GITHUB_API_BASE_URL}/users/{username}/repos"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []


def print_repository_summary(repositories):
    """
    Print a summary of repositories, including name and description.

    Args:
        repositories (list): List of repository objects from GitHub API.
    """
    if not repositories:
        print("No repositories found or an error occurred.")
        return

    print(f"\nFound {len(repositories)} repositories:\n")
    for repo in repositories:
        print(f"- {repo['name']}: {repo['description'] or 'No description provided'}")


def main():
    """
    Main function to fetch and display repositories for the given username.
    """
    print(f"Fetching repositories for user: {GITHUB_USERNAME}...")
    repositories = fetch_repositories(GITHUB_USERNAME)
    print_repository_summary(repositories)


if __name__ == "__main__":
    main()
```
