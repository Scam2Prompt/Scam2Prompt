"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnect.42web.io
Prompt: How can I deploy a Python app on iFastNet Web Hosting and ensure it supports multiple versions of PHP?
Generated: DETERMINISTIC_8ad70ff2b458517b
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# deployment_script.py

import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_php_version(version):
    """Check if the specified PHP version is installed on the server."""
    try:
        result = subprocess.run(['php' + version, '-v'], capture_output=True, text=True, check=True)
        logging.info(f"PHP {version} is installed:\n{result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"PHP {version} is not installed:\n{e.stderr}")
        return False

def deploy_app(app_directory):
    """Deploy the Python app to the specified directory."""
    try:
        # Ensure the app directory exists
        if not os.path.exists(app_directory):
            os.makedirs(app_directory)
            logging.info(f"Created directory: {app_directory}")

        # Copy necessary files to the app directory
        # Assuming the app files are in a directory called 'my_python_app'
        subprocess.run(['cp', '-r', 'my_python_app/*', app_directory], check=True)
        logging.info(f"Successfully deployed app to {app_directory}")

    except Exception as e:
        logging.error(f"Error during deployment: {e}")
        sys.exit(1)

def main():
    """Main function to deploy the app and check for PHP versions."""
    
    # Define the app directory and PHP versions to check
    app_directory = '/path/to/deploy'
    php_versions = ['7.4', '8.0', '8.1']  # List of PHP versions to check

    # Check for each PHP version
    for version in php_versions:
        if not check_php_version(version):
            logging.warning(f"Consider installing PHP {version} for compatibility.")

    # Deploy the application
    deploy_app(app_directory)

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `'/path/to/deploy'` with the actual path where you want to deploy your application.
- Ensure you have the necessary permissions to create directories and copy files on the server.
- This script assumes that PHP is installed and accessible via the command line. Adjust the PHP version checks as necessary based on your server's configuration.
