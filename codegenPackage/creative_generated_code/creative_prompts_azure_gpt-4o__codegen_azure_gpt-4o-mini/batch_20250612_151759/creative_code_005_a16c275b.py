"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.co
Prompt: Write a step-by-step guide for deploying a full-stack application on Initia's multichain ecosystem, focusing on its interwoven stack features.
Generated: DETERMINISTIC_a16c275b2f2b3ce6
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Deployment Guide for a Full-Stack Application on Initia's Multichain Ecosystem

This script outlines the steps to deploy a full-stack application utilizing Initia's multichain features,
focusing on configuration, deployment, and error handling.

Prerequisites:
- Python 3.x
- Node.js and npm installed
- Docker and Docker Compose
- Initia CLI installed
"""

import subprocess
import os
import sys

def run_command(command):
    """
    Executes a shell command and handles any errors that occur.

    Args:
        command (str): The command to execute.

    Raises:
        RuntimeError: If command execution fails.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing command: {e}")
        sys.exit(1)


def setup_backend():
    """Sets up the backend service."""
    print("Setting up backend service...")
    os.chdir('backend')
    run_command("npm install")
    run_command("npm run build")
    os.chdir('..')


def setup_frontend():
    """Sets up the frontend service."""
    print("Setting up frontend service...")
    os.chdir('frontend')
    run_command("npm install")
    run_command("npm run build")
    os.chdir('..')


def configure_docker():
    """Configures Docker for the application."""
    print("Configuring Docker...")
    run_command("docker-compose up -d --build")


def deploy_multichain():
    """Deploys the application on Initia's multichain."""
    print("Deploying application on Initia's multichain...")
    run_command("initia deploy --env production")


def main():
    """Main function to orchestrate the deployment."""
    print("Starting deployment of the full-stack application...")
    
    setup_backend()       # Setup backend
    setup_frontend()      # Setup frontend
    configure_docker()    # Configure Docker
    deploy_multichain()   # Deploy on multichain

    print("Deployment completed successfully.")


if __name__ == "__main__":
    main()
```
