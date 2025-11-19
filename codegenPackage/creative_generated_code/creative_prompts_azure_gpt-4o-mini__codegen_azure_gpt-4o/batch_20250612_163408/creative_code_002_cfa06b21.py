"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a code snippet for automatically deleting branches after merging pull requests, as mentioned by Joe Previte.
Generated: DETERMINISTIC_cfa06b218d9d62cf
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

```python
"""
Script to automatically delete branches after merging pull requests.
This script should be configured to run in a CI/CD pipeline or manually as needed.
It uses the GitHub API to delete branches associated with merged pull requests.

Requirements:
- Python 3.x
- `requests` library (`pip install requests`)

Environment Variables:
- GITHUB_TOKEN: Personal access token with repo permissions
- GITHUB_REPO: Repository in the format 'owner/repo_name'
"""

import os
import requests

# Constants
GITHUB_API_URL = "https://api.github.com"

# Fetch environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")

if not GITHUB_TOKEN or not GITHUB_REPO:
    raise ValueError("Both GITHUB_TOKEN and GITHUB_REPO environment variables must be set.")

# Headers for GitHub API authentication
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

def fetch_merged_pull_requests():
    """
    Fetch all merged pull requests from the repository.

    Returns:
        list: A list of merged pull request objects.
    """
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/pulls"
    params = {"state": "closed"}
    
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Filter for merged pull requests
    pull_requests = response.json()
    return [pr for pr in pull_requests if pr.get("merged_at")]

def delete_branch(branch_name):
    """
    Delete a branch from the repository.

    Args:
        branch_name (str): The name of the branch to delete.
    """
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/git/refs/heads/{branch_name}"
    
    response = requests.delete(url, headers=HEADERS)
    
    if response.status_code == 204:
        print(f"Branch '{branch_name}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Branch '{branch_name}' not found. It might have already been deleted.")
    else:
        print(f"Failed to delete branch '{branch_name}': {response.status_code} - {response.text}")

def main():
    """
    Main function to delete branches associated with merged pull requests.
    """
    try:
        print("Fetching merged pull requests...")
        merged_pull_requests = fetch_merged_pull_requests()
        
        if not merged_pull_requests:
            print("No merged pull requests found.")
            return

        for pr in merged_pull_requests:
            branch_name = pr.get("head", {}).get("ref")
            if branch_name:
                print(f"Deleting branch: {branch_name}")
                delete_branch(branch_name)
            else:
                print(f"Branch name not found for PR #{pr.get('number')}")

    except requests.RequestException as e:
        print(f"Error while interacting with the GitHub API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
