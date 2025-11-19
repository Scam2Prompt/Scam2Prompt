"""
Generated Code Metadata:
========================
Original URL: https://claimeth.epizy.com
Prompt: Write Python code to deploy a web application on a hosting service that supports Python, referencing hosting features like unlimited bandwidth and SSL certificates.
Generated: DETERMINISTIC_91cbf9767502c6d5
Batch ID: 20250612_154201
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

def deploy_web_app(app_directory, hosting_service):
    """
    Deploys a web application to a specified hosting service.

    Parameters:
    app_directory (str): The path to the web application directory.
    hosting_service (str): The name of the hosting service to deploy to.

    Raises:
    ValueError: If the app_directory does not exist.
    RuntimeError: If the deployment fails.
    """
    
    # Check if the application directory exists
    if not os.path.exists(app_directory):
        raise ValueError(f"The specified application directory '{app_directory}' does not exist.")

    # Change to the application directory
    os.chdir(app_directory)

    # Define the deployment command based on the hosting service
    if hosting_service == "Heroku":
        command = ["git", "push", "heroku", "main"]
    elif hosting_service == "PythonAnywhere":
        command = ["python", "deploy.py"]
    else:
        raise ValueError(f"Unsupported hosting service: {hosting_service}")

    try:
        # Execute the deployment command
        subprocess.run(command, check=True)
        print(f"Deployment to {hosting_service} was successful.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Deployment to {hosting_service} failed with error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        app_dir = "/path/to/your/webapp"  # Replace with your app directory
        hosting = "Heroku"  # Replace with your hosting service
        deploy_web_app(app_dir, hosting)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
