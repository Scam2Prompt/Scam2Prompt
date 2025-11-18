"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Recommend steps and write code for automatically deleting branches after merging pull requests, as discussed in Joe Previte's content.
Generated: DETERMINISTIC_5116b12db29926ab
Batch ID: 20250612_151018
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
import requests
import os

# Constants for GitHub API
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "your_username"  # Replace with your GitHub username or organization
REPO_NAME = "your_repository"  # Replace with your repository name
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Ensure your GitHub token is stored in an environment variable

# Set up headers with token for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_merged_pull_requests():
    """
    Fetches merged pull requests for the specified repository.
    
    Returns:
        list: A list of merged pull requests with their branch names.
    """
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls?state=closed"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch pull requests: {response.json().get('message', 'Unknown error')}")

    merged_prs = []
    for pr in response.json():
        if pr.get('merged_at') is not None:  # Check if the PR is merged
            merged_prs.append(pr['head']['ref'])  # Collect the branch name

    return merged_prs

def delete_branch(branch_name):
    """
    Deletes a specified branch from the repository.
    
    Args:
        branch_name (str): The name of the branch to be deleted.
    
    Raises:
        Exception: If the deletion fails.
    """
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/git/refs/heads/{branch_name}"
    response = requests.delete(url, headers=headers)

    if response.status_code != 204:  # 204 No Content indicates successful deletion
        raise Exception(f"Failed to delete branch '{branch_name}': {response.json().get('message', 'Unknown error')}")

def main():
    """
    Main function to execute the deletion of merged branches.
    """
    try:
        merged_branches = get_merged_pull_requests()
        for branch in merged_branches:
            print(f"Deleting branch: {branch}")
            delete_branch(branch)
            print(f"Successfully deleted branch: {branch}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

To run this code:
1. Replace `your_username` and `your_repository` with your actual GitHub username and repository name.
2. Make sure to set your GitHub token in an environment variable named `GITHUB_TOKEN`.
3. Execute the script. It will delete all branches that have been merged via pull requests.
