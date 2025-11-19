"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Write a Python script that automates the deployment of a web application on a hosting platform, similar to the services offered by Alshehhi.Net.
Generated: DETERMINISTIC_2582ca001f828e94
Batch ID: 20250622_205236
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
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebAppDeployer:
    def __init__(self, app_directory, remote_host, remote_user, remote_path):
        """
        Initialize the WebAppDeployer with necessary parameters.

        :param app_directory: Local path to the web application directory
        :param remote_host: Remote server hostname or IP address
        :param remote_user: Username for SSH authentication
        :param remote_path: Path on the remote server where the app will be deployed
        """
        self.app_directory = Path(app_directory)
        self.remote_host = remote_host
        self.remote_user = remote_user
        self.remote_path = remote_path

    def check_directory(self):
        """Check if the application directory exists."""
        if not self.app_directory.is_dir():
            logging.error(f"Application directory {self.app_directory} does not exist.")
            sys.exit(1)

    def build_application(self):
        """Build the application if necessary (e.g., for Python web apps)."""
        try:
            logging.info("Building the application...")
            subprocess.run(["python", "setup.py", "build"], check=True, cwd=self.app_directory)
            logging.info("Application built successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to build the application: {e}")
            sys.exit(1)

    def deploy_application(self):
        """Deploy the application to the remote server using SCP."""
        try:
            logging.info("Deploying the application...")
            subprocess.run(["scp", "-r", str(self.app_directory), f"{self.remote_user}@{self.remote_host}:{self.remote_path}"], check=True)
            logging.info("Application deployed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to deploy the application: {e}")
            sys.exit(1)

    def restart_remote_service(self):
        """Restart the web service on the remote server."""
        try:
            logging.info("Restarting the web service on the remote server...")
            subprocess.run(["ssh", f"{self.remote_user}@{self.remote_host}", "sudo systemctl restart my_web_service"], check=True)
            logging.info("Web service restarted successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to restart the web service: {e}")
            sys.exit(1)

    def run(self):
        """Run the deployment process."""
        self.check_directory()
        self.build_application()
        self.deploy_application()
        self.restart_remote_service()

if __name__ == "__main__":
    # Example usage: python deploy.py /path/to/app remote_host remote_user /path/on/remote
    if len(sys.argv) != 5:
        logging.error("Usage: python deploy.py <app_directory> <remote_host> <remote_user> <remote_path>")
        sys.exit(1)

    app_directory = sys.argv[1]
    remote_host = sys.argv[2]
    remote_user = sys.argv[3]
    remote_path = sys.argv[4]

    deployer = WebAppDeployer(app_directory, remote_host, remote_user, remote_path)
    deployer.run()
```
