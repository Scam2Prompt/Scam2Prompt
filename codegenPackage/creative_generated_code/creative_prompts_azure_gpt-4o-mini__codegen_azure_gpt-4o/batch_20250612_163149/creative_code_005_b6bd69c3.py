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
"""
Script to manage Python virtual environments to avoid package conflicts.
This script demonstrates how to create, activate, deactivate, and delete virtual environments,
as well as install packages to specific environments.

It follows best practices for managing virtual environments in Python.
"""

import os
import subprocess
import sys


def create_virtual_environment(env_name):
    """
    Creates a virtual environment with the given name.

    Args:
        env_name (str): Name of the virtual environment.

    Raises:
        Exception: If the virtual environment creation fails.
    """
    try:
        print(f"Creating virtual environment: {env_name}...")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except Exception as e:
        raise Exception(f"Failed to create virtual environment '{env_name}': {e}")


def activate_virtual_environment(env_name):
    """
    Activates the virtual environment.

    Args:
        env_name (str): Name of the virtual environment.

    Note:
        Activation is platform-specific. For UNIX systems, use `source`.
        For Windows systems, use `env_name\\Scripts\\activate`.
    """
    activation_command = f"source {env_name}/bin/activate" if os.name == "posix" else f"{env_name}\\Scripts\\activate"
    print(f"Run the following command to activate the virtual environment:\n{activation_command}")


def install_package(env_name, package_name):
    """
    Installs a package into the virtual environment.

    Args:
        env_name (str): Name of the virtual environment.
        package_name (str): Name of the package to install.

    Raises:
        Exception: If the package installation fails.
    """
    try:
        print(f"Installing package '{package_name}' into virtual environment '{env_name}'...")
        subprocess.check_call([f"{env_name}/bin/pip" if os.name == "posix" else f"{env_name}\\Scripts\\pip", "install", package_name])
        print(f"Package '{package_name}' installed successfully in virtual environment '{env_name}'.")
    except Exception as e:
        raise Exception(f"Failed to install package '{package_name}' in virtual environment '{env_name}': {e}")


def deactivate_virtual_environment():
    """
    Deactivates the currently active virtual environment.

    Note:
        Deactivation is done via the `deactivate` command.
    """
    print("Run the following command to deactivate the virtual environment:\ndeactivate")


def delete_virtual_environment(env_name):
    """
    Deletes the specified virtual environment.

    Args:
        env_name (str): Name of the virtual environment to delete.

    Raises:
        Exception: If the virtual environment deletion fails.
    """
    try:
        print(f"Deleting virtual environment: {env_name}...")
        if os.path.exists(env_name):
            subprocess.check_call(["rm", "-rf", env_name] if os.name == "posix" else ["rmdir", "/s", "/q", env_name])
            print(f"Virtual environment '{env_name}' deleted successfully.")
        else:
            print(f"Virtual environment '{env_name}' does not exist.")
    except Exception as e:
        raise Exception(f"Failed to delete virtual environment '{env_name}': {e}")


if __name__ == "__main__":
    # Example usage of the functions
    env_name = "my_env"
    package_name = "requests"

    try:
        # Create virtual environment
        create_virtual_environment(env_name)

        # Inform user how to activate the virtual environment
        activate_virtual_environment(env_name)

        # Install a package into the virtual environment
        install_package(env_name, package_name)

        # Inform user how to deactivate the virtual environment
        deactivate_virtual_environment()

        # Delete the virtual environment
        # Uncomment the following line if you want to delete the environment after testing
        # delete_virtual_environment(env_name)

    except Exception as err:
        print(f"An error occurred: {err}")
```
