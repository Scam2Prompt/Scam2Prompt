"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiwebio.rf.gd
Prompt: Generate a Python script that utilizes the Node.js support feature of iFastNet Web Hosting for deploying a simple web application.
Generated: DETERMINISTIC_143846d67036fa52
Batch ID: 20250612_161134
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

# Define the directory where the Node.js application will be stored
APP_DIR = 'my_node_app'

def create_app_directory():
    """Create a directory for the Node.js application."""
    try:
        if not os.path.exists(APP_DIR):
            os.makedirs(APP_DIR)
            print(f"Created directory: {APP_DIR}")
        else:
            print(f"Directory already exists: {APP_DIR}")
    except OSError as e:
        print(f"Error creating directory {APP_DIR}: {e}")
        sys.exit(1)

def create_package_json():
    """Create a package.json file for the Node.js application."""
    package_json_content = '''{
  "name": "my_node_app",
  "version": "1.0.0",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
'''
    try:
        with open(os.path.join(APP_DIR, 'package.json'), 'w') as f:
            f.write(package_json_content)
        print("Created package.json")
    except IOError as e:
        print(f"Error writing package.json: {e}")
        sys.exit(1)

def create_app_js():
    """Create a simple Express application in app.js."""
    app_js_content = '''const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Define a simple route for the home page
app.get('/', (req, res) => {
    res.send('Hello, World! This is my Node.js app deployed on iFastNet!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
'''
    try:
        with open(os.path.join(APP_DIR, 'app.js'), 'w') as f:
            f.write(app_js_content)
        print("Created app.js")
    except IOError as e:
        print(f"Error writing app.js: {e}")
        sys.exit(1)

def install_dependencies():
    """Install the necessary dependencies using npm."""
    try:
        subprocess.check_call(['npm', 'install'], cwd=APP_DIR)
        print("Installed dependencies")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def start_application():
    """Start the Node.js application."""
    try:
        subprocess.Popen(['npm', 'start'], cwd=APP_DIR)
        print("Node.js application started.")
    except Exception as e:
        print(f"Error starting the application: {e}")
        sys.exit(1)

def main():
    """Main function to orchestrate the creation and deployment of the Node.js application."""
    create_app_directory()
    create_package_json()
    create_app_js()
    install_dependencies()
    start_application()

if __name__ == '__main__':
    main()
```
