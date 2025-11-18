"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodl-tracking.web.app
Prompt: Write a script to automate the deployment process for Firebase Hosting, including authentication and resource allocation steps.
Generated: DETERMINISTIC_f3a74dd467bdbed8
Batch ID: 20250612_151159
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
import os

def run_command(command, description):
    """
    Executes a shell command and logs its status.
    
    Args:
        command (str): The shell command to execute.
        description (str): A brief description of what the command does.

    Raises:
        RuntimeError: If the command execution fails.
    """
    print(f"Starting: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Success: {description}\nOutput:\n{result.stdout}")
    except subprocess.CalledProcessError as error:
        print(f"Error during: {description}\n{error.stderr}")
        raise RuntimeError(f"Failed to execute: {description}") from error


def authenticate_firebase():
    """
    Authenticates the user with Firebase CLI.
    """
    run_command("firebase login", "Firebase authentication")


def initialize_project():
    """
    Initializes a Firebase Hosting project.
    """
    if not os.path.exists("firebase.json"):
        run_command("firebase init hosting", "Firebase Hosting initialization")
    else:
        print("firebase.json already exists. Skipping initialization.")


def deploy_project():
    """
    Deploys the project to Firebase Hosting.
    """
    run_command("firebase deploy --only hosting", "Firebase Hosting deployment")


def main():
    """
    Main function to orchestrate the Firebase Hosting deployment process.
    """
    print("Starting Firebase Hosting Deployment Automation Script...")
    
    try:
        # Step 1: Authenticate Firebase CLI
        authenticate_firebase()

        # Step 2: Initialize Firebase Hosting if not already initialized
        initialize_project()

        # Step 3: Deploy to Firebase Hosting
        deploy_project()

        print("Deployment completed successfully!")
    except RuntimeError as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
