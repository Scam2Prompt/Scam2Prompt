"""
Generated Code Metadata:
========================
Original URL: https://dapp-webnode.rf.gd
Prompt: Write a Python web application deployment script using iFastNet Web Hosting's Node.js and Python app support features.
Generated: DETERMINISTIC_858f795cc63e6356
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

# Define constants
NODEJS_CMD = "node"
PYTHON_CMD = "python3"

class DeploymentScript:
    def __init__(self, project_path: str, 
                 nodejs_version: Optional[str] = None, 
                 python_version: Optional[str] = None):
        """
        Initialize the deployment script.

        Args:
        - project_path (str): The path to the project directory.
        - nodejs_version (str, optional): The Node.js version to use. Defaults to None.
        - python_version (str, optional): The Python version to use. Defaults to None.
        """
        self.project_path = Path(project_path)
        self.nodejs_version = nodejs_version
        self.python_version = python_version

    def _validate_project_path(self) -> bool:
        """
        Validate the project path.

        Returns:
        - bool: True if the project path is valid, False otherwise.
        """
        return self.project_path.exists() and self.project_path.is_dir()

    def _install_nodejs_dependencies(self) -> None:
        """
        Install Node.js dependencies.

        Raises:
        - Exception: If the Node.js command is not found or if the dependencies cannot be installed.
        """
        try:
            subprocess.run([NODEJS_CMD, "npm", "install"], 
                           cwd=self.project_path, 
                           check=True)
        except FileNotFoundError:
            print(f"Error: {NODEJS_CMD} command not found.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to install Node.js dependencies. {e}")
            sys.exit(1)

    def _install_python_dependencies(self) -> None:
        """
        Install Python dependencies.

        Raises:
        - Exception: If the Python command is not found or if the dependencies cannot be installed.
        """
        try:
            subprocess.run([PYTHON_CMD, "-m", "pip", "install", "-r", "requirements.txt"], 
                           cwd=self.project_path, 
                           check=True)
        except FileNotFoundError:
            print(f"Error: {PYTHON_CMD} command not found.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to install Python dependencies. {e}")
            sys.exit(1)

    def deploy(self) -> None:
        """
        Deploy the application.

        Raises:
        - Exception: If the project path is invalid or if the deployment fails.
        """
        if not self._validate_project_path():
            print(f"Error: Invalid project path '{self.project_path}'.")
            sys.exit(1)

        # Check if Node.js version is specified
        if self.nodejs_version:
            try:
                subprocess.run([NODEJS_CMD, "--version"], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
            except FileNotFoundError:
                print(f"Error: Node.js version {self.nodejs_version} not found.")
                sys.exit(1)

        # Check if Python version is specified
        if self.python_version:
            try:
                subprocess.run([PYTHON_CMD, "--version"], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE)
            except FileNotFoundError:
                print(f"Error: Python version {self.python_version} not found.")
                sys.exit(1)

        # Install dependencies
        self._install_nodejs_dependencies()
        self._install_python_dependencies()

        # Deploy application
        try:
            # Assuming the application can be started with 'node app.js' or 'python app.py'
            if self.nodejs_version:
                subprocess.run([NODEJS_CMD, "app.js"], 
                               cwd=self.project_path, 
                               check=True)
            elif self.python_version:
                subprocess.run([PYTHON_CMD, "app.py"], 
                               cwd=self.project_path, 
                               check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to deploy application. {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python deploy.py <project_path> <nodejs_version> <python_version>")
        sys.exit(1)

    project_path = sys.argv[1]
    nodejs_version = sys.argv[2] if sys.argv[2] != "None" else None
    python_version = sys.argv[3] if sys.argv[3] != "None" else None

    deployment_script = DeploymentScript(project_path, nodejs_version, python_version)
    deployment_script.deploy()
```
