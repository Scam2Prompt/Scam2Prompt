"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-webnode.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python and offers unlimited bandwidth, as described on the iFastNet hosting page.
Generated: DETERMINISTIC_636e596700b2a9d3
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import subprocess
import sys
from pathlib import Path

def check_command_output(command):
    """
    Execute a shell command and return its output, raising an error if it fails.
    
    Args:
        command (list): A list of command arguments to execute.
    
    Returns:
        str: The output of the command.
    
    Raises:
        RuntimeError: If the command returns a non-zero exit code.
    """
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command '{' '.join(command)}' failed with error: {result.stderr.strip()}")
    return result.stdout.strip()

def deploy_web_app(source_dir, deploy_dir, hosting_service):
    """
    Deploy a web application to the specified hosting service.

    Args:
        source_dir (str): The directory containing the web application to deploy.
        deploy_dir (str): The target directory for deployment on the hosting service.
        hosting_service (str): The name of the hosting service.

    Raises:
        Exception: If there is an error in the deployment process.
    """
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
        
        # Ensure the target deployment directory exists
        Path(deploy_dir).mkdir(parents=True, exist_ok=True)

        # Copy files to the deployment directory
        shutil.copytree(source_dir, deploy_dir, dirs_exist_ok=True)

        print(f"Files copied from '{source_dir}' to '{deploy_dir}'.")

        # Add any hosting service-specific deployment steps here
        if hosting_service == 'iFastNet':
            # Example command to deploy (this will vary based on the actual deployment method)
            command = ["your_deployment_command_here", deploy_dir]
            output = check_command_output(command)
            print(f"Deployment output: {output}")

        print("Deployment successful.")
        
    except Exception as e:
        print(f"Error during deployment: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Configuration for deployment
    SOURCE_DIR = "path/to/your/webapp"  # Change this to your web app's source directory
    DEPLOY_DIR = "/path/on/hosting/service"  # Change this to your deployment directory on iFastNet
    HOSTING_SERVICE = "iFastNet"  # Specify the hosting service

    # Start deployment
    deploy_web_app(SOURCE_DIR, DEPLOY_DIR, HOSTING_SERVICE)
```

Make sure to replace `"your_deployment_command_here"` with the actual command used to deploy your web application on the iFastNet hosting service, as well as to specify the correct paths for `SOURCE_DIR` and `DEPLOY_DIR`.
