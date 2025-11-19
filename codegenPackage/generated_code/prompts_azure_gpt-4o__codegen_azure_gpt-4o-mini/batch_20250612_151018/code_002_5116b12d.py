"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-134--keen-roentgen-cafcb7.netlify.app
Prompt: Recommend steps and write code for automatically deleting branches after merging pull requests, as discussed in Joe Previte's content.
Generated: DETERMINISTIC_5116b12db29926ab
Batch ID: 20250612_151018
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
import sys

def delete_branch_after_merge(branch_name):
    """
    Deletes a local Git branch after it has been merged into the main branch.

    Args:
        branch_name (str): The name of the branch to delete.

    Raises:
        ValueError: If the branch name is empty or if the branch does not exist.
        subprocess.CalledProcessError: If the Git command fails.
    """
    if not branch_name:
        raise ValueError("Branch name cannot be empty.")

    # Check if the branch exists
    try:
        result = subprocess.run(
            ["git", "branch", "--list", branch_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if not result.stdout.strip():
            raise ValueError(f"Branch '{branch_name}' does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Error checking branch existence: {e.stderr.decode().strip()}")
        sys.exit(1)

    # Delete the local branch
    try:
        subprocess.run(
            ["git", "branch", "-d", branch_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"Successfully deleted branch '{branch_name}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting branch '{branch_name}': {e.stderr.decode().strip()}")
        sys.exit(1)

def main():
    """
    Main function to execute the branch deletion process.
    """
    # Example usage: replace 'feature-branch' with the actual branch name
    branch_name = 'feature-branch'  # Replace with the branch you want to delete

    try:
        delete_branch_after_merge(branch_name)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

### Usage Instructions:
1. Replace `'feature-branch'` in the `main` function with the name of the branch you want to delete after merging.
2. Ensure you have the necessary permissions and that the branch is merged before running the script.
3. Run the script in a terminal where Git is installed and configured.
