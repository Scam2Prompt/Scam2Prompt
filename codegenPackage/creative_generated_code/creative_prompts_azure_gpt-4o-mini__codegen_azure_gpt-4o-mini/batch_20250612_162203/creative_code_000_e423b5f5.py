"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseaaward-program.epizy.com
Prompt: Generate a Python script to deploy a web application on iFastNet hosting with Node.js support.
Generated: DETERMINISTIC_e423b5f5bf237b21
Batch ID: 20250612_162203
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

def check_node_installed():
    """Check if Node.js is installed on the system."""
    try:
        subprocess.run(["node", "--version"], check=True)
        print("Node.js is installed.")
    except subprocess.CalledProcessError:
        print("Node.js is not installed. Please install Node.js before proceeding.")
        sys.exit(1)

def create_app_structure(app_name):
    """Create the directory structure for the Node.js application."""
    try:
        os.makedirs(app_name)
        os.chdir(app_name)
        print(f"Application directory '{app_name}' created and navigated to.")
    except Exception as e:
        print(f"Error creating application directory: {e}")
        sys.exit(1)

def initialize_npm():
    """Initialize a new Node.js project using npm."""
    try:
        subprocess.run(["npm", "init", "-y"], check=True)
        print("npm project initialized.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to initialize npm project: {e}")
        sys.exit(1)

def create_server_file():
    """Create a basic Express server file."""
    server_code = """const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
"""
    try:
        with open('server.js', 'w') as f:
            f.write(server_code)
        print("Server file 'server.js' created.")
    except Exception as e:
        print(f"Error creating server file: {e}")
        sys.exit(1)

def install_dependencies():
    """Install required dependencies."""
    try:
        subprocess.run(["npm", "install", "express"], check=True)
        print("Express installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

def deploy_to_ifastnet(app_name):
    """Deploy the application to iFastNet hosting."""
    print("Deploying to iFastNet hosting...")
    # Note: Replace the following with actual deployment logic as per iFastNet API or FTP details.
    # This is a placeholder as deployment methods vary.
    try:
        # Placeholder for deployment commands
        print(f"Deployment of '{app_name}' is simulated.")
        # Example: subprocess.run(["your_deploy_command", app_name], check=True)
    except Exception as e:
        print(f"Error during deployment: {e}")
        sys.exit(1)

def main():
    """Main function to run the script."""
    check_node_installed()
    
    app_name = input("Enter the name of your web application: ").strip()
    create_app_structure(app_name)
    initialize_npm()
    create_server_file()
    install_dependencies()
    deploy_to_ifastnet(app_name)
    
    print("Web application deployment script completed successfully.")

if __name__ == "__main__":
    main()
```
