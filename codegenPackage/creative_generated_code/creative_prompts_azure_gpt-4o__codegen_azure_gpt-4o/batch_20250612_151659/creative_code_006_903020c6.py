"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_903020c6a481a84a
Batch ID: 20250612_151659
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
    Runs a shell command and handles errors gracefully.

    Args:
        command (list): The shell command to execute as a list of arguments.
    Returns:
        str: The output of the command if successful.
    Raises:
        RuntimeError: If the command fails.
    """
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        error_message = (
            f"Command '{' '.join(command)}' failed with error:\n{e.stderr.strip()}"
        )
        raise RuntimeError(error_message)


def deploy_to_firebase():
    """
    Automates the deployment of a web app to Firebase Hosting using the Firebase CLI.
    """
    try:
        print("Starting Firebase deployment...")

        # Step 1: Check if Firebase CLI is installed
        print("Checking if Firebase CLI is installed...")
        run_command(["firebase", "--version"])
        print("Firebase CLI is installed.")

        # Step 2: Login to Firebase (optional, depending on prior configuration)
        print("Logging into Firebase...")
        run_command(["firebase", "login"])
        print("Firebase login successful.")

        # Step 3: Initialize Firebase project (optional if already initialized)
        print("Initializing Firebase project...")
        run_command(["firebase", "init", "hosting"])
        print("Firebase project initialized.")

        # Step 4: Deploy the web app to Firebase Hosting
        print("Deploying web app to Firebase Hosting...")
        deployment_output = run_command(["firebase", "deploy", "--only", "hosting"])
        print("Deployment successful!")
        print("Deployment Output:")
        print(deployment_output)

    except RuntimeError as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)


if __name__ == "__main__":
    deploy_to_firebase()
```
