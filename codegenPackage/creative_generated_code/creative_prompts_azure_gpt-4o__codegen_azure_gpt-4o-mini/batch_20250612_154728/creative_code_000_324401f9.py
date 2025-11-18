"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks-rewards.epizy.com
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python apps, referencing features like unlimited disk space and bandwidth.
Generated: DETERMINISTIC_324401f9f6b929b3
Batch ID: 20250612_154728
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

class WebAppDeployer:
    def __init__(self, app_directory, hosting_service):
        """
        Initializes the WebAppDeployer with the application directory and hosting service.
        
        :param app_directory: Path to the web application directory
        :param hosting_service: Hosting service API or CLI tool name
        """
        self.app_directory = app_directory
        self.hosting_service = hosting_service

    def check_app_directory(self):
        """
        Checks if the application directory exists and is valid.
        
        :raises FileNotFoundError: If the application directory does not exist
        """
        if not os.path.isdir(self.app_directory):
            logging.error(f"Application directory {self.app_directory} does not exist.")
            raise FileNotFoundError(f"Application directory {self.app_directory} not found.")
        logging.info(f"Application directory {self.app_directory} is valid.")

    def deploy(self):
        """
        Deploys the web application to the hosting service.
        It uses a subprocess to call the hosting service's deployment command.
        
        :raises Exception: If the deployment fails
        """
        self.check_app_directory()
        logging.info(f"Starting deployment of {self.app_directory} to {self.hosting_service}.")

        try:
            # Command to deploy the application (assuming a hypothetical CLI command)
            # Replace with the actual command specific to your hosting service
            command = f"{self.hosting_service} deploy {self.app_directory}"
            logging.info(f"Executing command: {command}")

            # Execute the deployment command
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                logging.info("Deployment successful.")
                logging.info(result.stdout)
            else:
                logging.error("Deployment failed.")
                logging.error(result.stderr)
                raise Exception(f"Deployment failed with error: {result.stderr}")

        except subprocess.CalledProcessError as e:
            logging.error("An error occurred during deployment.")
            logging.error(e.output)
            raise Exception(f"An error occurred during deployment: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise

if __name__ == "__main__":
    # Define the application directory and hosting service
    APP_DIRECTORY = "/path/to/your/webapp"  # Change this to your app's path
    HOSTING_SERVICE = "your_hosting_service_cli"  # Change this to your hosting service command

    deployer = WebAppDeployer(APP_DIRECTORY, HOSTING_SERVICE)

    try:
        deployer.deploy()
    except Exception as e:
        logging.critical(f"Deployment process failed: {e}")
```

Ensure to replace `/path/to/your/webapp` and `your_hosting_service_cli` with the actual path to your web application and the command for your hosting service.
