"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Write a Python script to automate the installation process for a fire protection system in a commercial building, referencing best practices from ERA Engineering's services.
Generated: DETERMINISTIC_bf7cccb93c51e8e7
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import logging
from pathlib import Path

# Configure logging for the script
logging.basicConfig(
    filename='fire_protection_installation.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def check_service_status(service_name):
    """Check if a given service is running."""
    try:
        status = subprocess.run(['systemctl', 'is-active', service_name],
                                capture_output=True, text=True, check=True)
        return status.stdout.strip() == 'active'
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking status of {service_name}: {e}")
        return False

def install_package(package_name):
    """Install the specified package using apt."""
    try:
        logging.info(f"Installing package: {package_name}")
        subprocess.run(['sudo', 'apt', 'install', '-y', package_name],
                       check=True)
        logging.info(f"Successfully installed: {package_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install {package_name}: {e}")
        raise

def enable_service(service_name):
    """Enable and start the specified service."""
    try:
        logging.info(f"Enabling service: {service_name}")
        subprocess.run(['sudo', 'systemctl', 'enable', service_name], check=True)
        subprocess.run(['sudo', 'systemctl', 'start', service_name], check=True)
        logging.info(f"Successfully enabled and started: {service_name}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to enable/start {service_name}: {e}")
        raise

def main():
    """Main function to automate fire protection system installation."""
    logging.info("Starting installation process for fire protection system.")
    
    # List of required packages and services
    packages = ['firewalld', 'fire-protection-system']
    services = ['firewall.service', 'fire-protection.service']

    # Check and install necessary packages
    for package in packages:
        if not check_service_status(package):
            install_package(package)

    # Enable and start necessary services
    for service in services:
        if not check_service_status(service):
            enable_service(service)

    logging.info("Installation process completed successfully.")

if __name__ == "__main__":
    # Ensure the script runs only as the main module
    try:
        main()
    except Exception as e:
        logging.critical(f"Installation process failed: {e}")
        exit(1)
```
