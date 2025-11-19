"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Provide a code snippet for automatically deleting branches after merging pull requests, as mentioned by Joe Previte.
Generated: DETERMINISTIC_cfa06b218d9d62cf
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import argparse

def get_merged_prs(repo, username):
    """
    Fetch a list of merged pull requests for a given repository and username.

    Args:
        repo (str): The repository name (e.g., 'owner/repo').
        username (str): The GitHub username.

    Returns:
        list: A list of merged pull request numbers.
    """
    try:
        # Use GitHub API to fetch merged PRs
        cmd = f"gh api /repos/{repo}/pulls --method GET --field state=closed,merged --paginate"
        output = subprocess.check_output(cmd, shell=True)
        merged_prs = []
        for line in output.decode('utf-8').splitlines():
            try:
                pr_data = json.loads(line)
                if pr_data['merged'] and pr_data['user']['login'] == username:
                    merged_prs.append(pr_data['number'])
            except json.JSONDecodeError:
                pass
        return merged_prs
    except subprocess.CalledProcessError as e:
        print(f"Error fetching merged PRs: {e}")
        return []

def get_branch_name(repo, pr_number):
    """
    Fetch the branch name for a given pull request number.

    Args:
        repo (str): The repository name (e.g., 'owner/repo').
        pr_number (int): The pull request number.

    Returns:
        str: The branch name.
    """
    try:
        # Use GitHub API to fetch PR data
        cmd = f"gh api /repos/{repo}/pulls/{pr_number} --method GET --field head"
        output = subprocess.check_output(cmd, shell=True)
        pr_data = json.loads(output.decode('utf-8'))
        return pr_data['head']['ref']['name']
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Error fetching PR data: {e}")
        return None

def delete_branch(repo, branch_name):
    """
    Delete a branch for a given repository and branch name.

    Args:
        repo (str): The repository name (e.g., 'owner/repo').
        branch_name (str): The branch name.
    """
    try:
        # Use Git to delete the branch
        cmd = f"git push origin --delete {branch_name}"
        subprocess.check_call(cmd, shell=True)
        print(f"Deleted branch {branch_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting branch {branch_name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Auto-delete branches after merging pull requests")
    parser.add_argument("--repo", required=True, help="Repository name (e.g., 'owner/repo')")
    parser.add_argument("--username", required=True, help="GitHub username")
    args = parser.parse_args()

    merged_prs = get_merged_prs(args.repo, args.username)
    for pr_number in merged_prs:
        branch_name = get_branch_name(args.repo, pr_number)
        if branch_name:
            delete_branch(args.repo, branch_name)

if __name__ == "__main__":
    import json
    main()
```
