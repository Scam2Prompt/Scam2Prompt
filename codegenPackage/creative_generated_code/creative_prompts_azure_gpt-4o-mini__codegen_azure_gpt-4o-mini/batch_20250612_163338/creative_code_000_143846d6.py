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

// Middleware to parse JSON requests
app.use(express.json());

// A simple route
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
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
    """Install dependencies for the Node.js application using npm."""
    try:
        print("Installing dependencies...")
        subprocess.run(['npm', 'install'], cwd=APP_DIR, check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def main():
    """Main function to initialize and deploy the Node.js application."""
    create_app_directory()
    create_package_json()
    create_app_js()
    install_dependencies()
    print("Node.js application setup complete.")

if __name__ == '__main__':
    main()
```
