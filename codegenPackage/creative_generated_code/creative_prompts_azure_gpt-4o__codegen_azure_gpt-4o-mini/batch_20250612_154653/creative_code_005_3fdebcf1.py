"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartvalidation.net
Prompt: Provide an example of how to use Smart Validation's VPS hosting environment to deploy a web application with enhanced security and dedicated resources.
Generated: DETERMINISTIC_3fdebcf1c2ecb13a
Batch ID: 20250612_154653
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def deploy_web_application(app_directory, server_ip, server_user, ssh_key_path):
    """
    Deploy a web application to a VPS hosting environment with enhanced security.

    Parameters:
    - app_directory (str): The local path to the web application directory.
    - server_ip (str): The IP address of the VPS server.
    - server_user (str): The username for SSH access to the server.
    - ssh_key_path (str): The path to the SSH private key for authentication.

    Raises:
    - Exception: If deployment fails due to any reason.
    """
    try:
        # Check if the application directory exists
        if not os.path.exists(app_directory):
            raise FileNotFoundError(f"Application directory {app_directory} does not exist.")

        # Create a tarball of the application for transfer
        tarball_name = "app_deploy.tar.gz"
        logging.info(f"Creating tarball {tarball_name} from {app_directory}.")
        subprocess.run(["tar", "-czf", tarball_name, "-C", app_directory, "."], check=True)

        # Upload the tarball to the server using SCP
        logging.info(f"Uploading {tarball_name} to {server_user}@{server_ip}:/var/www/myapp/")
        subprocess.run(["scp", "-i", ssh_key_path, tarball_name, f"{server_user}@{server_ip}:/var/www/myapp/"], check=True)

        # Connect to the server and extract the tarball
        logging.info("Connecting to the server to extract the application.")
        ssh_command = f"ssh -i {ssh_key_path} {server_user}@{server_ip} 'cd /var/www/myapp && tar -xzf {tarball_name} && rm {tarball_name}'"
        subprocess.run(ssh_command, shell=True, check=True)

        logging.info("Deployment completed successfully.")
    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
        raise
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during deployment: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    APP_DIRECTORY = "/path/to/your/web/application"
    SERVER_IP = "192.0.2.1"
    SERVER_USER = "your_username"
    SSH_KEY_PATH = "/path/to/your/private/key"

    deploy_web_application(APP_DIRECTORY, SERVER_IP, SERVER_USER, SSH_KEY_PATH)
```
