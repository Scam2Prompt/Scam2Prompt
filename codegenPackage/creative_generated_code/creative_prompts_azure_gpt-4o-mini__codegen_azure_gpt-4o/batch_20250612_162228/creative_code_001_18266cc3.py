"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.net
Prompt: Write a script to automate the setup of a managed server on さくらのレンタルサーバ, ensuring it includes high security and stability features.
Generated: DETERMINISTIC_18266cc387c67408
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
Script to automate the setup of a managed server on さくらのレンタルサーバ.
This script ensures high security and stability features are implemented.
"""

import subprocess
import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def run_command(command):
    """
    Function to run shell commands and handle errors.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        logging.info(f"Command succeeded: {command}")
        logging.debug(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}")
        logging.error(f"Error: {e.stderr}")
        sys.exit(1)

def update_packages():
    """
    Update all installed packages to their latest version.
    """
    logging.info("Updating system packages...")
    run_command("sudo apt update && sudo apt upgrade -y")

def configure_firewall():
    """
    Configure the firewall to allow only necessary traffic.
    """
    logging.info("Configuring firewall...")
    run_command("sudo ufw default deny incoming")
    run_command("sudo ufw default allow outgoing")
    run_command("sudo ufw allow ssh")
    run_command("sudo ufw enable")

def install_fail2ban():
    """
    Install and configure fail2ban for protection against brute-force attacks.
    """
    logging.info("Installing fail2ban...")
    run_command("sudo apt install fail2ban -y")

    # Create a basic fail2ban configuration
    fail2ban_conf = """
[DEFAULT]
ignoreip = 127.0.0.1/8
bantime  = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true
port    = ssh
logpath = %(sshd_log)s
"""
    with open("/etc/fail2ban/jail.local", "w") as f:
        f.write(fail2ban_conf)
    logging.info("fail2ban configuration applied.")

    # Restart fail2ban to apply changes
    run_command("sudo systemctl restart fail2ban")

def secure_ssh():
    """
    Harden SSH security settings.
    """
    logging.info("Securing SSH...")
    ssh_config_path = "/etc/ssh/sshd_config"
    if not os.path.exists(ssh_config_path):
        logging.error("SSH configuration file not found.")
        sys.exit(1)

    # Backup the original SSH configuration
    run_command(f"sudo cp {ssh_config_path} {ssh_config_path}.backup")

    # Update the SSH configuration
    with open(ssh_config_path, "a") as ssh_config:
        ssh_config.write("\nPermitRootLogin no\n")
        ssh_config.write("PasswordAuthentication no\n")
        ssh_config.write("Protocol 2\n")
        ssh_config.write("MaxAuthTries 3\n")
        ssh_config.write("AllowUsers your_username\n")  # Replace with actual username

    logging.info("SSH configuration hardened.")
    run_command("sudo systemctl restart sshd")

def setup_logging():
    """
    Set up system logging for monitoring and troubleshooting.
    """
    logging.info("Setting up system logging...")
    run_command("sudo apt install rsyslog -y")
    run_command("sudo systemctl enable rsyslog")
    run_command("sudo systemctl start rsyslog")

def main():
    """
    Main function to orchestrate the setup.
    """
    logging.info("Starting server setup...")
    update_packages()
    configure_firewall()
    install_fail2ban()
    secure_ssh()
    setup_logging()
    logging.info("Server setup completed successfully.")

if __name__ == "__main__":
    main()
```
