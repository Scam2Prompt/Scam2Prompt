"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Suggest a way to contribute to the Fantom programming language on GitHub, and provide an example of a pull request that adds a new feature to the system library.
Generated: DETERMINISTIC_98c79c2474c5c530
Batch ID: 20250612_150040
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/refs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/refs/heads": {
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
# This script demonstrates how to contribute to the Fantom programming language 
# on GitHub by creating a pull request that adds a new feature to the system library.

import requests

# GitHub repository details
REPO_OWNER = "fantom-io"
REPO_NAME = "fantom"
BRANCH_NAME = "feature/system-lib-enhancement"
TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub personal access token

# New feature details for the system library
new_feature = {
    "name": "New Utility Function",
    "description": "Adds a utility function to the system library for improved string manipulation.",
}

# Function to create a new branch
def create_branch():
    try:
        # Get the master branch's latest commit SHA
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/refs/heads"
        response = requests.get(url, headers={"Authorization": f"token {TOKEN}"})
        response.raise_for_status()
        
        master_branch = next((item for item in response.json() if item['ref'] == 'refs/heads/master'), None)
        master_sha = master_branch['object']['sha']

        # Create a new branch from master
        new_branch = {
            "ref": f"refs/heads/{BRANCH_NAME}",
            "sha": master_sha
        }
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/refs"
        response = requests.post(url, json=new_branch, headers={"Authorization": f"token {TOKEN}"})
        response.raise_for_status()
        print(f"Branch '{BRANCH_NAME}' created successfully.")
    except requests.exceptions.HTTPError as err:
        print(f"Error creating branch: {err}")

# Function to create a new file with the new feature
def create_file():
    try:
        # Define the file path and content
        file_path = "lib/system/new_utility.fan"
        file_content = f"""// New utility function in the system library

package system

// Adds two strings and returns the concatenated result
func concatenateStrings(a: String, b: String): String {{
    return a + b
}}
"""

        # Create a new file in the repository
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
        commit_message = "Add new utility function to system library"
        data = {
            "message": commit_message,
            "content": file_content.encode("utf-8").hex(),  # Encode the content to hex
            "branch": BRANCH_NAME
        }
        response = requests.put(url, json=data, headers={"Authorization": f"token {TOKEN}"})
        response.raise_for_status()
        print(f"File '{file_path}' created successfully.")
    except requests.exceptions.HTTPError as err:
        print(f"Error creating file: {err}")

# Function to create a pull request
def create_pull_request():
    try:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
        pr_data = {
            "title": "Add New Utility Function to System Library",
            "body": "This pull request adds a new utility function for string manipulation.",
            "head": BRANCH_NAME,
            "base": "master"
        }
        response = requests.post(url, json=pr_data, headers={"Authorization": f"token {TOKEN}"})
        response.raise_for_status()
        pr_url = response.json().get('html_url')
        print(f"Pull request created successfully: {pr_url}")
    except requests.exceptions.HTTPError as err:
        print(f"Error creating pull request: {err}")

# Main function to execute the contribution process
def main():
    create_branch()
    create_file()
    create_pull_request()

if __name__ == "__main__":
    main()
```

Make sure to replace `YOUR_GITHUB_TOKEN` with your actual GitHub personal access token before running the code.
