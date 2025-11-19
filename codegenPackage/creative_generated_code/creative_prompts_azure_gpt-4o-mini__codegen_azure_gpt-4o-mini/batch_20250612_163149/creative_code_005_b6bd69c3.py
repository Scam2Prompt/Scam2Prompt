"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apiym.com
Prompt: What is the process for managing Python virtual environments to avoid package conflicts as explained on apiym.com?
Generated: DETERMINISTIC_b6bd69c31f9b8bf2
Batch ID: 20250612_163149
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

def create_virtual_environment(env_name):
    """
    Create a virtual environment in a specified directory.

    Args:
        env_name (str): The name of the virtual environment to create.

    Raises:
        RuntimeError: If the virtual environment creation fails.
    """
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to create virtual environment: {e}")

def activate_virtual_environment(env_name):
    """
    Activate the virtual environment.

    Args:
        env_name (str): The name of the virtual environment to activate.
    """
    activate_script = os.path.join(env_name, 'Scripts', 'activate')
    if os.name != 'nt':  # If not Windows
        activate_script = os.path.join(env_name, 'bin', 'activate')
    
    print(f"To activate the virtual environment, run: source {activate_script}")

def install_package(env_name, package_name):
    """
    Install a package in the specified virtual environment.

    Args:
        env_name (str): The name of the virtual environment.
        package_name (str): The name of the package to install.

    Raises:
        RuntimeError: If the package installation fails.
    """
    pip_path = os.path.join(env_name, 'Scripts', 'pip')
    if os.name != 'nt':  # If not Windows
        pip_path = os.path.join(env_name, 'bin', 'pip')
    
    try:
        subprocess.check_call([pip_path, 'install', package_name])
        print(f"Package '{package_name}' installed successfully in '{env_name}'.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to install package '{package_name}': {e}")

def list_installed_packages(env_name):
    """
    List all packages installed in the specified virtual environment.

    Args:
        env_name (str): The name of the virtual environment.
    
    Returns:
        list: A list of installed packages.
    """
    pip_path = os.path.join(env_name, 'Scripts', 'pip')
    if os.name != 'nt':  # If not Windows
        pip_path = os.path.join(env_name, 'bin', 'pip')
    
    try:
        result = subprocess.check_output([pip_path, 'list'], text=True)
        print("Installed packages:\n", result)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to list installed packages: {e}")

def main():
    """
    Main function to demonstrate virtual environment management processes.
    """
    env_name = 'myenv'
    
    create_virtual_environment(env_name)
    activate_virtual_environment(env_name)
    
    # Example of installing a package
    install_package(env_name, 'requests')
    
    # List installed packages
    list_installed_packages(env_name)

if __name__ == "__main__":
    main()
```
