"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev-metamask.wuaze.com
Prompt: Generate a Python script that utilizes the Node.js support feature of iFastNet web hosting to deploy a simple web application.
Generated: DETERMINISTIC_57cf723f51ab9e05
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import sys

def deploy_nodejs_application(app_name, app_directory, start_script):
    """
    Deploy a simple Node.js web application on iFastNet web hosting.
    
    Parameters:
    app_name (str): Name of the application.
    app_directory (str): Path to the application's directory.
    start_script (str): Name of the script to start the Node.js application (e.g., 'server.js').
    
    Returns:
    None
    """
    try:
        # Validate inputs
        if not app_name or not app_directory or not start_script:
            raise ValueError("All parameters (app_name, app_directory, start_script) are required.")

        if not os.path.isdir(app_directory):
            raise FileNotFoundError(f"Application directory '{app_directory}' does not exist.")

        start_script_path = os.path.join(app_directory, start_script)
        if not os.path.isfile(start_script_path):
            raise FileNotFoundError(f"Start script '{start_script}' not found in '{app_directory}'.")

        print(f"Deploying Node.js application '{app_name}'...")

        # Change to the application directory
        os.chdir(app_directory)

        # Install dependencies using npm
        print("Installing dependencies...")
        subprocess.run(["npm", "install"], check=True)

        # Start the application
        print(f"Starting the application with script '{start_script}'...")
        subprocess.run(["node", start_script], check=True)

        print(f"Application '{app_name}' has been successfully deployed and started.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing a subprocess: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Returning to the original directory
        os.chdir(os.path.dirname(__file__))

if __name__ == "__main__":
    # Example usage:
    try:
        app_name = "SampleApp"
        app_directory = "/path/to/your/nodejs/app"
        start_script = "server.js"

        # Deploy the application
        deploy_nodejs_application(app_name, app_directory, start_script)

    except Exception as e:
        print(f"Unhandled exception: {e}")
```

**Note**: Replace `/path/to/your/nodejs/app` and `server.js` with the actual path and script name of your Node.js application before executing the script.
