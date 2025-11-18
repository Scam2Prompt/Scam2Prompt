"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-game7.xyz
Prompt: Suggest best practices for securing a newly configured web server against common vulnerabilities.
Generated: DETERMINISTIC_ae6d64774946ae4b
Batch ID: 20250612_151343
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def configure_firewall():
    """
    Configure the firewall to restrict access to necessary ports only.
    Allows HTTP (80), HTTPS (443), and SSH (22) by default.
    """
    logging.info("Configuring the firewall...")

    # List of allowed ports
    allowed_ports = [80, 443, 22]

    try:
        # Enable UFW (Uncomplicated Firewall)
        subprocess.run(['ufw', 'enable'], check=True)

        # Allow specified ports
        for port in allowed_ports:
            subprocess.run(['ufw', 'allow', str(port)], check=True)
            logging.info(f"Allowed port: {port}")

        logging.info("Firewall configured successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error configuring firewall: {e}")

def disable_root_login():
    """
    Disable root login via SSH to enhance security.
    """
    logging.info("Disabling root login via SSH...")

    try:
        # Update sshd_config to disable root login
        with open('/etc/ssh/sshd_config', 'r') as file:
            lines = file.readlines()

        with open('/etc/ssh/sshd_config', 'w') as file:
            for line in lines:
                if line.startswith("PermitRootLogin"):
                    file.write("PermitRootLogin no\n")
                else:
                    file.write(line)

        # Restart SSH service
        subprocess.run(['systemctl', 'restart', 'ssh'], check=True)
        logging.info("Root login disabled successfully.")
    except Exception as e:
        logging.error(f"Error disabling root login: {e}")

def keep_system_updated():
    """
    Update the system packages to ensure all components are up to date.
    """
    logging.info("Updating system packages...")

    try:
        # Update and upgrade system packages
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'upgrade', '-y'], check=True)

        logging.info("System packages updated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating system packages: {e}")

def main():
    """
    Main function to execute server hardening measures.
    """
    try:
        configure_firewall()
        disable_root_login()
        keep_system_updated()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
