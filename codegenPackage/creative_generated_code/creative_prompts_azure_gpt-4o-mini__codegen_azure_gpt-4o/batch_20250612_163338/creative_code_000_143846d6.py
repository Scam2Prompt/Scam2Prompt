"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staratlasawards-finance.rf.gd
Prompt: Generate a Python script that utilizes the Node.js support feature of iFastNet Web Hosting for deploying a simple web application.
Generated: DETERMINISTIC_143846d67036fa52
Batch ID: 20250612_163338
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

def deploy_nodejs_app(app_name, app_path, port):
    """
    Deploy a simple Node.js web application on iFastNet Web Hosting.

    Parameters:
        app_name (str): Name of the application.
        app_path (str): Path to the Node.js application directory.
        port (int): Port on which the application should run.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    try:
        # Ensure the application directory exists
        if not os.path.exists(app_path):
            raise FileNotFoundError(f"The specified path '{app_path}' does not exist.")
        
        # Change to the application directory
        os.chdir(app_path)

        # Install dependencies using npm
        print(f"Installing dependencies for {app_name}...")
        subprocess.run(["npm", "install"], check=True)

        # Start the application using npm start
        print(f"Starting the Node.js application '{app_name}' on port {port}...")
        subprocess.run(["npm", "start"], check=True)

        print(f"Application '{app_name}' deployed successfully on port {port}.")
        return True

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        return False

    except subprocess.CalledProcessError as sp_error:
        print(f"Error during subprocess execution: {sp_error}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    # Configuration for the deployment
    app_name = "MyNodeJSApp"
    app_path = "/path/to/your/nodejs/app"
    port = 3000

    # Deploy the application
    success = deploy_nodejs_app(app_name, app_path, port)

    if success:
        print("Deployment completed successfully.")
    else:
        print("Deployment failed. Please check the error messages above.")
```

Note: Replace `"/path/to/your/nodejs/app"` with the actual path to your Node.js application directory. Ensure that the `npm start` script is properly configured in your `package.json` file for the application.
