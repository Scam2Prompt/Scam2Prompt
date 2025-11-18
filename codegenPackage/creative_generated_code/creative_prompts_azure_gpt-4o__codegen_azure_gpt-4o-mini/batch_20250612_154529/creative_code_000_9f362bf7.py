"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-pancakeswap.epizy.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python apps, as described on the iFastNet hosting page.
Generated: DETERMINISTIC_9f362bf75e00051c
Batch ID: 20250612_154529
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

class WebAppDeployer:
    """
    A class to handle the deployment of a web application to iFastNet hosting.
    """

    def __init__(self, project_dir, ftp_host, ftp_user, ftp_password):
        """
        Initializes the WebAppDeployer with project directory and FTP credentials.

        :param project_dir: The local directory of the web application.
        :param ftp_host: The FTP host address.
        :param ftp_user: The FTP username.
        :param ftp_password: The FTP password.
        """
        self.project_dir = project_dir
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_password = ftp_password

    def _check_directory(self):
        """Check if the project directory exists."""
        if not os.path.isdir(self.project_dir):
            raise FileNotFoundError(f"The project directory '{self.project_dir}' does not exist.")

    def _run_command(self, command):
        """
        Run a shell command and handle errors.

        :param command: The command to run.
        :raises RuntimeError: If the command fails.
        """
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Command '{command}' failed with error: {e}")

    def install_dependencies(self):
        """Installs dependencies listed in requirements.txt."""
        requirements_file = os.path.join(self.project_dir, 'requirements.txt')
        if os.path.isfile(requirements_file):
            print("Installing dependencies from requirements.txt...")
            self._run_command(f"pip install -r {requirements_file}")

    def deploy(self):
        """Deploy the web application to iFastNet hosting via FTP."""
        self._check_directory()
        print(f"Deploying from {self.project_dir} to {self.ftp_host}...")

        # Change to the project directory
        os.chdir(self.project_dir)

        # Install dependencies
        self.install_dependencies()

        # FTP deployment command
        ftp_command = f"lftp -u {self.ftp_user},{self.ftp_password} {self.ftp_host} -e 'mirror -R . /public_html; bye'"
        
        # Run the deployment command
        self._run_command(ftp_command)

        print("Deployment completed successfully.")

if __name__ == "__main__":
    # Replace these values with your actual project directory and FTP credentials
    PROJECT_DIR = '/path/to/your/webapp'
    FTP_HOST = 'ftp.yourhostingprovider.com'
    FTP_USER = 'ftp_username'
    FTP_PASSWORD = 'ftp_password'

    try:
        deployer = WebAppDeployer(PROJECT_DIR, FTP_HOST, FTP_USER, FTP_PASSWORD)
        deployer.deploy()
    except Exception as e:
        print(f"An error occurred during deployment: {e}", file=sys.stderr)
        sys.exit(1)
```

**Note**: Ensure that the `lftp` tool is installed on your system to execute the FTP deployment command. Update the `PROJECT_DIR`, `FTP_HOST`, `FTP_USER`, and `FTP_PASSWORD` with actual values before running the script.
