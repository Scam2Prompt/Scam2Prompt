"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisvvap.run
Prompt: Write a script to automate the deployment of a website on a server managed by Ispmanager.
Generated: DETERMINISTIC_a311544e32d2a1b8
Batch ID: 20250612_161059
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
import sys

# Setting up logging for the script
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("deployment.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def execute_command(command):
    """
    Executes a shell command and returns the output.
    Raises an exception if the command fails.

    :param command: Command to execute
    :return: Command output
    """
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command output: {result.stdout}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}")
        logging.error(f"Error: {e.stderr}")
        raise e


def create_website_domain(domain_name):
    """
    Creates a new website domain in ISPmanager.

    :param domain_name: Domain name to create
    """
    try:
        logging.info(f"Creating domain: {domain_name}")
        command = f"mgrctl webdomain.edit elid='new' name='{domain_name}'"
        execute_command(command)
        logging.info(f"Domain {domain_name} created successfully.")
    except Exception as e:
        logging.error(f"Failed to create domain: {domain_name}, Error: {e}")
        raise e


def upload_website_files(domain_name, source_directory):
    """
    Uploads website files to the server directory managed by ISPmanager.

    :param domain_name: Domain name where files should be uploaded
    :param source_directory: Local directory containing website files
    """
    try:
        target_directory = f"/var/www/{domain_name}/data/www/{domain_name}"
        logging.info(f"Uploading files from {source_directory} to {target_directory}")
        
        if not os.path.exists(source_directory):
            raise FileNotFoundError(f"Source directory {source_directory} does not exist.")
        
        command = f"rsync -av --progress {source_directory}/ {target_directory}/"
        execute_command(command)
        logging.info(f"Files uploaded successfully to {target_directory}")
    except Exception as e:
        logging.error(f"Failed to upload website files for domain: {domain_name}, Error: {e}")
        raise e


def set_permissions(domain_name):
    """
    Sets appropriate permissions for the website directory.

    :param domain_name: Domain name whose directory permissions are being modified
    """
    try:
        target_directory = f"/var/www/{domain_name}/data/www/{domain_name}"
        logging.info(f"Setting permissions for {target_directory}")
        
        command = f"chown -R {domain_name}:{domain_name} {target_directory}"
        execute_command(command)
        logging.info(f"Permissions set successfully for {target_directory}")
    except Exception as e:
        logging.error(f"Failed to set permissions for domain: {domain_name}, Error: {e}")
        raise e


def deploy_website(domain_name, source_directory):
    """
    Automates the deployment process of a website on an ISPmanager server.

    :param domain_name: Domain name to deploy
    :param source_directory: Local directory containing website files
    """
    try:
        logging.info(f"Starting deployment process for domain: {domain_name}")
        
        # Step 1: Create the domain in ISPmanager
        create_website_domain(domain_name)
        
        # Step 2: Upload website files
        upload_website_files(domain_name, source_directory)
        
        # Step 3: Set permissions
        set_permissions(domain_name)
        
        logging.info(f"Deployment completed successfully for domain: {domain_name}")
    except Exception as e:
        logging.error(f"Deployment failed for domain: {domain_name}, Error: {e}")
        raise e


if __name__ == "__main__":
    # Example usage of the script:
    try:
        domain_name = input("Enter the domain name: ").strip()
        source_directory = input("Enter the local source directory path: ").strip()

        deploy_website(domain_name, source_directory)
    except Exception as e:
        logging.error(f"Error during script execution: {e}")
        sys.exit(1)
```
