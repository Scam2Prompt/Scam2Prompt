"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claytonventuresnew.free.nf
Prompt: Write a Python script to deploy a web application on a hosting platform that supports Python and Node.js, referencing hosting features like unlimited disk space and bandwidth.
Generated: DETERMINISTIC_3bbd10afd720419f
Batch ID: 20250612_151414
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_command_exists(command):
    """Check if a command exists in the system."""
    return subprocess.call(f"which {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_requirements(requirements_file):
    """Install required packages from a requirements file."""
    logging.info(f"Installing requirements from {requirements_file}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing requirements: {e}")
        sys.exit(1)

def deploy_application(app_directory):
    """Deploy the web application to a specified directory."""
    logging.info(f"Deploying application from {app_directory}")
    os.chdir(app_directory)

    # Install Python requirements
    if os.path.exists('requirements.txt'):
        install_requirements('requirements.txt')

    # Build and start Node.js application if present
    if os.path.exists('package.json'):
        logging.info("Detected Node.js application. Installing Node.js dependencies...")
        try:
            subprocess.check_call(['npm', 'install'])
            subprocess.check_call(['npm', 'run', 'build'])
            subprocess.Popen(['npm', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error during Node.js build/start: {e}")
            sys.exit(1)

    logging.info("Deployment completed successfully.")

def main():
    """Main function to deploy the web application."""
    app_directory = input("Enter the path to your web application directory: ").strip()
    
    # Validate input
    if not os.path.isdir(app_directory):
        logging.error("Provided path is not a valid directory.")
        sys.exit(1)

    # Check if Python and Node.js are installed
    if not check_command_exists('python3') or not check_command_exists('node'):
        logging.error("Python3 or Node.js is not installed. Please install them before deploying.")
        sys.exit(1)

    deploy_application(app_directory)

if __name__ == "__main__":
    main()
```

Make sure to run this script in an environment where you have the necessary permissions and the required tools (Python, Node.js, npm) installed. Additionally, ensure your application structure includes both `requirements.txt` for Python libraries and `package.json` for Node.js dependencies where applicable.
