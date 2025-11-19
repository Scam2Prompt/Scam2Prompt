"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://receive-payment.kesug.com
Prompt: How can I deploy a Python app on iFastNet Web Hosting, considering their support for multiple PHP versions?
Generated: DETERMINISTIC_f203dc276606a236
Batch ID: 20250612_163851
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

def deploy_python_app(source_dir, destination_dir, virtual_env_name):
    """
    Deploy a Python application to iFastNet Web Hosting.

    Args:
        source_dir (str): The directory containing the source code of the Python app.
        destination_dir (str): The directory on the server where the app will be deployed.
        virtual_env_name (str): The name of the virtual environment to create.

    Raises:
        Exception: If the deployment process fails at any step.
    """
    try:
        # Step 1: Check if the source directory exists
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")

        # Step 2: Create a virtual environment
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', virtual_env_name], check=True)

        # Step 3: Activate the virtual environment and install dependencies
        print("Installing dependencies...")
        activate_script = os.path.join(virtual_env_name, 'Scripts', 'activate')
        install_cmd = f"{activate_script} && pip install -r {os.path.join(source_dir, 'requirements.txt')}"
        subprocess.run(install_cmd, shell=True, check=True)

        # Step 4: Copy the application files to the destination directory
        print(f"Copying files from '{source_dir}' to '{destination_dir}'...")
        if os.path.exists(destination_dir):
            shutil.rmtree(destination_dir)  # Remove the existing directory
        shutil.copytree(source_dir, destination_dir)

        print("Deployment completed successfully.")

    except Exception as e:
        print(f"An error occurred during the deployment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Define the source and destination for the deployment
    SOURCE_DIR = 'path/to/your/python_app'
    DESTINATION_DIR = 'path/on/server'
    VIRTUAL_ENV_NAME = 'venv'

    # Call the deploy function
    deploy_python_app(SOURCE_DIR, DESTINATION_DIR, VIRTUAL_ENV_NAME)
```

**Note:** Ensure you replace `'path/to/your/python_app'` and `'path/on/server'` with the actual paths relevant to your deployment scenario.
