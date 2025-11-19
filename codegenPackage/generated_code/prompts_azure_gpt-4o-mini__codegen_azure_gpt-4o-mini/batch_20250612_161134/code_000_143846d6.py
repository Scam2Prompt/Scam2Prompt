"""
Generated Code Metadata:
========================
Original URL: https://suiwebio.rf.gd
Prompt: Generate a Python script that utilizes the Node.js support feature of iFastNet Web Hosting for deploying a simple web application.
Generated: DETERMINISTIC_143846d67036fa52
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys

def check_node_installed():
    """Check if Node.js is installed on the system."""
    try:
        subprocess.run(["node", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Node.js is installed.")
    except subprocess.CalledProcessError:
        print("Node.js is not installed. Please install Node.js before proceeding.")
        sys.exit(1)

def create_app_directory(app_name):
    """Create a directory for the web application."""
    try:
        os.makedirs(app_name, exist_ok=True)
        print(f"Directory '{app_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{app_name}': {e}")
        sys.exit(1)

def initialize_npm(app_name):
    """Initialize a new Node.js application using npm."""
    try:
        subprocess.run(["npm", "init", "-y"], cwd=app_name, check=True)
        print("NPM initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing NPM: {e}")
        sys.exit(1)

def install_express(app_name):
    """Install Express.js framework for the web application."""
    try:
        subprocess.run(["npm", "install", "express"], cwd=app_name, check=True)
        print("Express.js installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing Express.js: {e}")
        sys.exit(1)

def create_server_file(app_name):
    """Create a simple server file for the web application."""
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
        with open(os.path.join(app_name, 'server.js'), 'w') as f:
            f.write(server_code)
        print("Server file 'server.js' created successfully.")
    except Exception as e:
        print(f"Error creating server file: {e}")
        sys.exit(1)

def main():
    """Main function to deploy a simple web application."""
    app_name = "my_web_app"  # Change this to your desired app name

    check_node_installed()
    create_app_directory(app_name)
    initialize_npm(app_name)
    install_express(app_name)
    create_server_file(app_name)

    print("Web application setup completed successfully.")

if __name__ == "__main__":
    main()
```
