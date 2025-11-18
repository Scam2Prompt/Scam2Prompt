"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-portfolio-metamask-io.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using Firebase CLI commands.
Generated: DETERMINISTIC_1040b4a32898d3b1
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def run_command(command):
    """
    Run a shell command and handle errors.
    :param command: List of strings representing the command and its arguments
    :return: None
    """
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Exit code: {e.returncode}")
        print(f"Error message: {e.stderr}")
        sys.exit(e.returncode)

def install_firebase_cli():
    """
    Ensure Firebase CLI is installed globally using npm.
    """
    print("Checking Firebase CLI installation...")
    try:
        run_command(["firebase", "--version"])
        print("Firebase CLI is already installed.")
    except FileNotFoundError:
        print("Firebase CLI not found. Installing Firebase CLI globally...")
        run_command(["npm", "install", "-g", "firebase-tools"])

def firebase_login():
    """
    Authenticate Firebase CLI.
    """
    print("Authenticating Firebase CLI...")
    run_command(["firebase", "login"])

def initialize_firebase_project():
    """
    Initialize Firebase Hosting for the project. Assumes `firebase.json` configuration exists.
    """
    print("Initializing Firebase Hosting...")
    run_command(["firebase", "init", "hosting"])

def deploy_to_firebase():
    """
    Deploy the web app to Firebase Hosting.
    """
    print("Deploying web app to Firebase Hosting...")
    run_command(["firebase", "deploy"])

if __name__ == "__main__":
    # Main script entry point
    print("Starting Firebase Hosting deployment automation...")

    # Step 1: Ensure Firebase CLI is installed
    install_firebase_cli()

    # Step 2: Authenticate Firebase CLI
    firebase_login()

    # Step 3: Initialize Firebase Hosting
    initialize_firebase_project()

    # Step 4: Deploy web app to Firebase Hosting
    deploy_to_firebase()

    print("Deployment completed successfully!")
```
