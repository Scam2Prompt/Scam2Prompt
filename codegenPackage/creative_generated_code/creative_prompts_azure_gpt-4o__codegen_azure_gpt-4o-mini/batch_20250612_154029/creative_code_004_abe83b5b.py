"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apiym.com
Prompt: Write a script to clone a GitHub repository via SSH and troubleshoot SSH permission issues, referencing the "通过 SSH 克隆 GitHub 仓库权限问题" section on https://apiym.com.
Generated: DETERMINISTIC_abe83b5bd1819eee
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

def clone_github_repo(repo_url, clone_dir):
    """
    Clone a GitHub repository via SSH.

    Args:
        repo_url (str): The SSH URL of the GitHub repository.
        clone_dir (str): The directory where the repository will be cloned.

    Raises:
        subprocess.CalledProcessError: If the clone command fails.
    """
    try:
        # Ensure the target directory does not already exist
        if os.path.exists(clone_dir):
            raise FileExistsError(f"The directory '{clone_dir}' already exists. Please remove it or choose a different directory.")

        # Run the git clone command
        subprocess.run(['git', 'clone', repo_url, clone_dir], check=True)
        print(f"Successfully cloned the repository to '{clone_dir}'")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to clone the repository.")
        print("Details:", e)
        troubleshoot_ssh_permissions()
        sys.exit(1)
    except FileExistsError as e:
        print("Error:", e)
        sys.exit(1)

def troubleshoot_ssh_permissions():
    """
    Provide troubleshooting steps for SSH permission issues.
    """
    print("\nTroubleshooting SSH Permission Issues:")
    print("1. Ensure you have added your SSH key to your GitHub account.")
    print("   You can check your SSH keys in GitHub settings under 'SSH and GPG keys'.")
    print("2. Check if the SSH agent is running and has your key loaded:")
    print("   Run: 'ssh-add -l' to list keys. If no keys are listed, run 'ssh-add ~/.ssh/id_rsa'.")
    print("3. Test your SSH connection to GitHub:")
    print("   Run: 'ssh -T git@github.com'. You should see a success message.")
    print("4. Make sure your SSH key has the correct permissions:")
    print("   Run: 'chmod 600 ~/.ssh/id_rsa' to set the right permissions.")
    print("5. Verify the SSH config file at ~/.ssh/config (if it exists) for any misconfigurations.")

if __name__ == "__main__":
    # Example usage: replace with your own repository and desired clone directory
    REPO_URL = "git@github.com:username/repo.git"
    CLONE_DIR = "repo"
    
    clone_github_repo(REPO_URL, CLONE_DIR)
```
