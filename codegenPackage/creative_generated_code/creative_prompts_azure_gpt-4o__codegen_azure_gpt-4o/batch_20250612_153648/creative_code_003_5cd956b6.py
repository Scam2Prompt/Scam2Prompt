"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorealm.vercel.app
Prompt: Create a script that automates the process of launching a business app using Gorealm's CLI tool.
Generated: DETERMINISTIC_5cd956b6583974cd
Batch ID: 20250612_153648
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

def run_command(command):
    """
    Run a shell command and return its output. Raises an exception on failure.

    Args:
        command (str): The shell command to execute.

    Returns:
        str: The output of the command.

    Raises:
        RuntimeError: If the command fails.
    """
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(f"Command failed: {command}\nError: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        raise RuntimeError(f"Error executing command: {command}\n{str(e)}")

def check_gorealm_installed():
    """
    Check if 'gorealm' CLI tool is installed by verifying its presence.

    Raises:
        RuntimeError: If 'gorealm' is not installed.
    """
    try:
        run_command("gorealm --version")
    except RuntimeError:
        raise RuntimeError("Gorealm is not installed or not found in the system PATH.")

def launch_business_app(app_name, environment="production"):
    """
    Automates the process of launching a business app using Gorealm's CLI tool.

    Args:
        app_name (str): The name of the business app to launch.
        environment (str): The environment in which to launch the app ('production' by default).

    Raises:
        RuntimeError: If the app launch fails.
    """
    if not app_name:
        raise ValueError("App name cannot be empty.")
    
    print(f"[INFO] Launching app '{app_name}' in '{environment}' environment...")

    command = f"gorealm app launch --name {app_name} --env {environment}"
    output = run_command(command)

    print("[SUCCESS] App launched successfully!")
    print(f"Output:\n{output}")

def main():
    """
    Entry point of the script.
    """
    try:
        print("[INFO] Checking if 'gorealm' CLI tool is installed...")
        check_gorealm_installed()
        print("[INFO] 'gorealm' CLI tool is installed.")

        # Replace with the actual app name and environment as needed
        app_name = "example-business-app"
        environment = "production"
        
        launch_business_app(app_name, environment)
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
