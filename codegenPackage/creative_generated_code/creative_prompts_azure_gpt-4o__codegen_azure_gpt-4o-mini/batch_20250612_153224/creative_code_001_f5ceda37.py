"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.syncsitebuilder.xyz
Prompt: Generate a script to automate website deployment using DreamHost's hosting platform.
Generated: DETERMINISTIC_f5ceda3719f2977c
Batch ID: 20250612_153224
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

class DreamHostDeployer:
    """A class to automate the deployment of a website on DreamHost."""

    def __init__(self, domain, local_directory, ssh_key_path):
        """
        Initializes the deployer with necessary credentials.

        Parameters:
            domain (str): The domain of the website.
            local_directory (str): The local directory of the website files.
            ssh_key_path (str): The path to the SSH key for authentication.
        """
        self.domain = domain
        self.local_directory = local_directory
        self.ssh_key_path = ssh_key_path
        self.remote_directory = f"/home/{self.domain}/"

    def run_command(self, command):
        """Executes a shell command and handles errors.

        Parameters:
            command (str): The command to be executed.

        Raises:
            RuntimeError: If the command fails.
        """
        try:
            result = subprocess.run(command, check=True, shell=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.stderr}")
            raise RuntimeError(f"Command failed: {command}")

    def sync_files(self):
        """Syncs local files to the remote DreamHost server using rsync."""
        command = f"rsync -avz -e 'ssh -i {self.ssh_key_path}' {self.local_directory}/ {self.domain}:~/{self.remote_directory}"
        self.run_command(command)

    def deploy(self):
        """Main deployment method to execute the deployment process."""
        print(f"Deploying website to {self.domain}...")
        self.sync_files()
        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Ensure proper usage of the script
    if len(sys.argv) != 4:
        print("Usage: python deploy.py <domain> <local_directory> <ssh_key_path>")
        sys.exit(1)

    # Assign command-line arguments to variables
    domain = sys.argv[1]
    local_directory = sys.argv[2]
    ssh_key_path = sys.argv[3]

    # Instantiate the deployer and run deployment
    deployer = DreamHostDeployer(domain, local_directory, ssh_key_path)

    try:
        deployer.deploy()
    except RuntimeError as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)
```

Make sure to replace the placeholders with your actual domain, local directory, and SSH key path when running the script.
