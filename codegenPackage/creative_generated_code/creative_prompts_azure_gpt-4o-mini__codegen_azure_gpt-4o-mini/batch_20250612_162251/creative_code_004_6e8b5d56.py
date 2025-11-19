"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ryanml.github.io
Prompt: Write a script that automates the deployment of a website using GitHub, referencing Ryan Lanese's approach.
Generated: DETERMINISTIC_6e8b5d56dd578c43
Batch ID: 20250612_162251
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/username/repo.git": {
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
import os
import subprocess
import sys

class WebsiteDeployer:
    def __init__(self, repo_url, branch='main', local_dir='website'):
        """
        Initialize the WebsiteDeployer with repository URL, branch, and local directory.

        :param repo_url: URL of the GitHub repository to deploy
        :param branch: Branch of the repository to deploy (default is 'main')
        :param local_dir: Local directory to clone the repository (default is 'website')
        """
        self.repo_url = repo_url
        self.branch = branch
        self.local_dir = local_dir

    def run_command(self, command):
        """
        Run a shell command and handle potential errors.

        :param command: Command to execute as a list
        :raises RuntimeError: If the command fails
        """
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            print(f"Return code: {e.returncode}")
            print(f"Output: {e.output}")
            print(f"Error message: {e.stderr}")
            raise RuntimeError(f"Command failed: {' '.join(command)}") from e

    def clone_repository(self):
        """
        Clone the specified GitHub repository into the local directory.
        """
        print(f"Cloning repository {self.repo_url} to {self.local_dir}...")
        self.run_command(['git', 'clone', self.repo_url, self.local_dir])
        os.chdir(self.local_dir)
        print(f"Switched to directory: {self.local_dir}")

    def checkout_branch(self):
        """
        Checkout the specified branch in the local repository.
        """
        print(f"Checking out branch {self.branch}...")
        self.run_command(['git', 'checkout', self.branch])

    def build_website(self):
        """
        Build the website using npm (assuming a Node.js project).
        Modify this method based on your specific build requirements.
        """
        print("Building the website...")
        self.run_command(['npm', 'install'])
        self.run_command(['npm', 'run', 'build'])

    def deploy(self):
        """
        Perform the deployment steps: clone, checkout branch, and build the website.
        """
        try:
            self.clone_repository()
            self.checkout_branch()
            self.build_website()
            print("Deployment completed successfully.")
        except Exception as e:
            print(f"Deployment failed: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Replace with your GitHub repository URL and desired branch
    REPO_URL = 'https://github.com/username/repo.git'
    BRANCH = 'main'

    deployer = WebsiteDeployer(repo_url=REPO_URL, branch=BRANCH)
    deployer.deploy()
```
