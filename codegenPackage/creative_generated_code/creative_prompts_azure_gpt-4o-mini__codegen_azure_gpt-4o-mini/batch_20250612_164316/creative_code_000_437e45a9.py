"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Generate a Python script that utilizes iFastNet Web Hosting's Node.js support to deploy a simple web application.
Generated: DETERMINISTIC_437e45a999b1885f
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import subprocess
import sys

# Define the path for the Node.js application
APP_NAME = "my-node-app"
APP_DIR = os.path.join(os.getcwd(), APP_NAME)

# Function to create a simple Node.js application
def create_node_app():
    """Creates a basic Node.js application structure."""
    try:
        # Create the application directory
        os.makedirs(APP_DIR, exist_ok=True)

        # Create package.json file
        package_json_content = {
            "name": APP_NAME,
            "version": "1.0.0",
            "main": "server.js",
            "scripts": {
                "start": "node server.js"
            },
            "dependencies": {
                "express": "^4.17.1"
            }
        }

        with open(os.path.join(APP_DIR, "package.json"), 'w') as f:
            import json
            json.dump(package_json_content, f, indent=4)

        # Create server.js file
        server_js_content = """const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Simple route
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
"""

        with open(os.path.join(APP_DIR, "server.js"), 'w') as f:
            f.write(server_js_content)

        print(f"Node.js application '{APP_NAME}' created successfully.")

    except Exception as e:
        print(f"Error creating Node.js app: {e}")
        sys.exit(1)

# Function to install dependencies using npm
def install_dependencies():
    """Installs the necessary Node.js dependencies."""
    try:
        # Navigate to the app directory
        os.chdir(APP_DIR)

        # Run npm install
        subprocess.check_call(['npm', 'install'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Dependencies installed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Function to start the Node.js application
def start_application():
    """Starts the Node.js application."""
    try:
        # Change to the application directory
        os.chdir(APP_DIR)

        # Start the application
        subprocess.Popen(['npm', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Node.js application '{APP_NAME}' is now running.")

    except Exception as e:
        print(f"Error starting the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_node_app()  # Step 1: Create the Node.js application
    install_dependencies()  # Step 2: Install dependencies
    start_application()  # Step 3: Start the application
```
