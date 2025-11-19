"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baybyit.com
Prompt: What are the first steps to take after setting up a new web server?
Generated: DETERMINISTIC_961993f5a44062b8
Batch ID: 20250612_163625
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
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def install_updates():
    """Update the package list and upgrade installed packages."""
    try:
        logging.info("Updating package index and upgrading installed packages...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], check=True)
        logging.info("System packages updated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to update packages: {e}")
        raise

def configure_firewall():
    """Set up the firewall to allow only necessary ports."""
    try:
        logging.info("Configuring firewall to allow only SSH and HTTP(S)...")
        subprocess.run(['sudo', 'ufw', 'allow', 'OpenSSH'], check=True)
        subprocess.run(['sudo', 'ufw', 'allow', '80/tcp'], check=True)  # HTTP
        subprocess.run(['sudo', 'ufw', 'allow', '443/tcp'], check=True)  # HTTPS
        subprocess.run(['sudo', 'ufw', 'enable'], check=True)
        logging.info("Firewall configured successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to configure firewall: {e}")
        raise

def create_non_root_user(username):
    """Create a new non-root user and add it to the sudo group."""
    try:
        logging.info(f"Creating non-root user '{username}'...")
        subprocess.run(['sudo', 'adduser', username], check=True)
        subprocess.run(['sudo', 'usermod', '-aG', 'sudo', username], check=True)
        logging.info(f"User '{username}' created and added to sudo group.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create user '{username}': {e}")
        raise

def main():
    """Main function to execute server setup tasks."""
    try:
        install_updates()
        configure_firewall()
        create_non_root_user('newuser')  # Replace 'newuser' with the desired username
    except Exception as e:
        logging.critical(f"Server setup failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
