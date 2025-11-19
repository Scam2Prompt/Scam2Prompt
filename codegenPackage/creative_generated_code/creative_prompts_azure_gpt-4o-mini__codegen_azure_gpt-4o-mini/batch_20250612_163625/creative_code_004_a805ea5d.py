"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baybyit.com
Prompt: How do I secure my new web server against common vulnerabilities?
Generated: DETERMINISTIC_a805ea5d29054b01
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

# Configure logging for monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def update_system():
    """Update the system packages to the latest versions."""
    try:
        logging.info("Updating system packages...")
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'upgrade', '-y'], check=True)
        logging.info("System packages updated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating system packages: {e}")
        raise

def configure_firewall():
    """Configure UFW (Uncomplicated Firewall) to secure the server."""
    try:
        logging.info("Setting up the firewall...")
        subprocess.run(['ufw', 'allow', 'OpenSSH'], check=True)
        subprocess.run(['ufw', 'enable'], check=True)
        logging.info("Firewall configured and enabled.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error configuring the firewall: {e}")
        raise

def disable_root_login():
    """Disable root login via SSH for security purposes."""
    try:
        logging.info("Disabling root login via SSH...")
        with open('/etc/ssh/sshd_config', 'r') as file:
            config = file.readlines()
        
        # Modify the PermitRootLogin directive
        with open('/etc/ssh/sshd_config', 'w') as file:
            for line in config:
                if line.startswith('PermitRootLogin'):
                    file.write('PermitRootLogin no\n')
                else:
                    file.write(line)
        
        # Restart SSH service to apply changes
        subprocess.run(['systemctl', 'restart', 'ssh'], check=True)
        logging.info("Root login via SSH disabled.")
    except Exception as e:
        logging.error(f"Error disabling root login: {e}")
        raise

def install_security_updates():
    """Install security updates automatically."""
    try:
        logging.info("Installing security updates...")
        subprocess.run(['apt-get', 'install', '-y', 'unattended-upgrades'], check=True)
        subprocess.run(['dpkg-reconfigure', '--priority=low', 'unattended-upgrades'], check=True)
        logging.info("Security updates installation configured.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing security updates: {e}")
        raise

def main():
    """Main function to secure the web server."""
    try:
        update_system()
        configure_firewall()
        disable_root_login()
        install_security_updates()
        logging.info("Web server secured successfully.")
    except Exception as e:
        logging.critical(f"Failed to secure the web server: {e}")

if __name__ == '__main__':
    main()
```
