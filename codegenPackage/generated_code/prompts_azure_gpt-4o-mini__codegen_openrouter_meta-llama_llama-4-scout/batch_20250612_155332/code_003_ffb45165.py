"""
Generated Code Metadata:
========================
Original URL: https://the-ebh.net
Prompt: Develop a code snippet that demonstrates how to use CentOS Special Interest Groups (SIGs) to enhance the functionality of a CentOS installation.
Generated: DETERMINISTIC_ffb4516593d5eac1
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import subprocess
import sys

def enable_sig(sig_name):
    """
    Enable a CentOS SIG repository.

    Args:
        sig_name (str): The name of the SIG repository to enable.

    Returns:
        bool: True if the SIG repository was enabled successfully, False otherwise.
    """
    try:
        # Enable the SIG repository
        command = f"dnf config-manager --set-enabled {sig_name}"
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error enabling {sig_name} SIG: {e}", file=sys.stderr)
        return False

def install_packages(sig_name, packages):
    """
    Install packages from a CentOS SIG repository.

    Args:
        sig_name (str): The name of the SIG repository.
        packages (list): A list of packages to install.

    Returns:
        bool: True if the packages were installed successfully, False otherwise.
    """
    try:
        # Install the packages
        command = f"dnf install -y {' '.join(packages)}"
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages from {sig_name} SIG: {e}", file=sys.stderr)
        return False

def main():
    # Define the SIG repository and packages to install
    sig_name = "powertools"
    packages = ["epel-release", "dnf-utils"]

    # Enable the SIG repository
    if not enable_sig(sig_name):
        sys.exit(1)

    # Install packages from the SIG repository
    if not install_packages(sig_name, packages):
        sys.exit(1)

    print(f"Successfully enabled {sig_name} SIG and installed packages.")

if __name__ == "__main__":
    main()
```
