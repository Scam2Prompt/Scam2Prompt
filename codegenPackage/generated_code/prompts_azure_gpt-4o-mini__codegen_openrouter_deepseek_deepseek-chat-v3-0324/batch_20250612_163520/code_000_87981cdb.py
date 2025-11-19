"""
Generated Code Metadata:
========================
Original URL: https://claimtether-rewards.rf.gd
Prompt: Generate a Python script that utilizes the Node.js support feature of iFastNet Web Hosting to deploy a simple web application.
Generated: DETERMINISTIC_87981cdb4d95c90f
Batch ID: 20250612_163520
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
import shutil
import json
from pathlib import Path

def create_nodejs_app(app_name="my_node_app"):
    """
    Creates a simple Node.js web application structure.
    Args:
        app_name (str): Name of the application directory
    Returns:
        Path: Path to the created application directory
    """
    app_dir = Path(app_name)
    
    try:
        # Create directory structure
        app_dir.mkdir(exist_ok=True)
        (app_dir / "public").mkdir(exist_ok=True)
        
        # Create package.json
        package_json = {
            "name": app_name,
            "version": "1.0.0",
            "description": "Simple Node.js app for iFastNet",
            "main": "server.js",
            "scripts": {
                "start": "node server.js"
            },
            "dependencies": {
                "express": "^4.18.2"
            }
        }
        
        with open(app_dir / "package.json", "w") as f:
            json.dump(package_json, f, indent=2)
        
        # Create server.js
        server_js = """
const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Basic route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
"""
        with open(app_dir / "server.js", "w") as f:
            f.write(server_js.strip())
        
        # Create simple index.html
        index_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Node.js App on iFastNet</title>
</head>
<body>
    <h1>Hello from Node.js on iFastNet!</h1>
    <p>Your application is running successfully.</p>
</body>
</html>
"""
        with open(app_dir / "public" / "index.html", "w") as f:
            f.write(index_html.strip())
            
        return app_dir.resolve()
    
    except Exception as e:
        print(f"Error creating Node.js app: {e}")
        if app_dir.exists():
            shutil.rmtree(app_dir)
        raise

def install_dependencies(app_dir):
    """
    Installs Node.js dependencies using npm.
    Args:
        app_dir (Path): Path to the application directory
    """
    try:
        subprocess.run(["npm", "install"], cwd=app_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        raise
    except FileNotFoundError:
        print("npm not found. Please ensure Node.js is installed.")
        raise

def create_zip_archive(app_dir):
    """
    Creates a zip archive of the Node.js application.
    Args:
        app_dir (Path): Path to the application directory
    Returns:
        Path: Path to the created zip file
    """
    try:
        zip_path = app_dir.parent / f"{app_dir.name}.zip"
        shutil.make_archive(str(zip_path.with_suffix('')), 'zip', app_dir)
        return zip_path
    except Exception as e:
        print(f"Error creating zip archive: {e}")
        raise

def deploy_to_ifastnet(app_name="my_node_app"):
    """
    Main function to create and package a Node.js app for iFastNet deployment.
    Args:
        app_name (str): Name of the application
    Returns:
        Path: Path to the zip file ready for deployment
    """
    try:
        print(f"Creating Node.js application '{app_name}'...")
        app_dir = create_nodejs_app(app_name)
        
        print("Installing dependencies...")
        install_dependencies(app_dir)
        
        print("Creating deployment package...")
        zip_path = create_zip_archive(app_dir)
        
        print(f"\nSuccess! Deployment package created at: {zip_path}")
        print("Upload this zip file to your iFastNet hosting control panel.")
        
        return zip_path
    
    except Exception as e:
        print(f"Deployment failed: {e}")
        return None

if __name__ == "__main__":
    deploy_to_ifastnet()
```
