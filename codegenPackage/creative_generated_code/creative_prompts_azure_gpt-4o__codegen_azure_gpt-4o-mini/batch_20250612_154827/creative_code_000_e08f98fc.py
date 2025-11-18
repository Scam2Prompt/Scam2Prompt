"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoin.rf.gd
Prompt: Write a Python script to deploy a web application on a hosting service that supports Python, Node.js, and multiple PHP versions, as described on iFastNet hosting.
Generated: DETERMINISTIC_e08f98fc8f96f468
Batch ID: 20250612_154827
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

def run_command(command):
    """
    Run a shell command and handle errors.
    
    Args:
        command (str): The command to run in the shell.
    
    Returns:
        str: The output from the command.
    
    Raises:
        RuntimeError: If the command fails.
    """
    try:
        logging.info(f'Executing command: {command}')
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logging.info(f'Command output: {result.stdout.strip()}')
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f'Command failed with error: {e.stderr.strip()}')
        raise RuntimeError(f'Command failed: {e}')

def deploy_web_app(app_directory, hosting_credentials):
    """
    Deploy a web application to iFastNet hosting service.

    Args:
        app_directory (str): The path to the web application directory.
        hosting_credentials (dict): A dictionary containing hosting credentials.

    Raises:
        RuntimeError: If deployment fails.
    """
    # Step 1: Change directory to the application directory
    if not os.path.isdir(app_directory):
        logging.error(f"Application directory '{app_directory}' does not exist.")
        raise RuntimeError(f"Invalid application directory: {app_directory}")

    os.chdir(app_directory)
    
    # Step 2: Install necessary dependencies
    # Assuming we have a requirements.txt for Python
    if os.path.exists('requirements.txt'):
        run_command('pip install -r requirements.txt')

    # Step 3: Build the Node.js application if applicable
    if os.path.exists('package.json'):
        run_command('npm install')
        run_command('npm run build')

    # Step 4: Deploy the application to the hosting service
    # This is a simulated deploy command, replace it with actual deployment logic
    deployment_command = f"ssh {hosting_credentials['user']}@{hosting_credentials['host']} 'cd {hosting_credentials['remote_directory']} && git pull && python app.py'"
    
    try:
        run_command(deployment_command)
        logging.info("Deployment completed successfully.")
    except RuntimeError as e:
        logging.error(f"Deployment failed: {e}")
        raise

# Example usage
if __name__ == "__main__":
    app_directory = '/path/to/your/web/app'
    hosting_credentials = {
        'user': 'your_username',
        'host': 'your_host',
        'remote_directory': '/path/on/server'
    }

    try:
        deploy_web_app(app_directory, hosting_credentials)
    except RuntimeError as e:
        logging.critical(f"Deployment process failed: {e}")
```

Make sure to replace the placeholders (like `/path/to/your/web/app`, `your_username`, and `your_host`) with actual values before running the script.
