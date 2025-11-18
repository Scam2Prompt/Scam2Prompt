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
"""
This Python script demonstrates best practices for securing a newly configured web server.
It automates some essential tasks such as disabling unused services,
configuring firewall rules, and setting up secure SSH access.
"""

import os
import subprocess
import shutil

def secure_web_server():
    """
    Secures a web server against common vulnerabilities by:
    - Disabling unnecessary services
    - Configuring the firewall
    - Securing SSH access
    - Keeping the server updated
    """
    try:
        print("Starting server security configuration...")

        # Disable unnecessary services
        print("Disabling unused services...")
        unused_services = ["ftp", "telnet", "rlogin", "rexec"]
        for service in unused_services:
            subprocess.run(["systemctl", "disable", service], check=True)
        
        # Configure firewall rules
        print("Configuring firewall rules...")
        subprocess.run(["ufw", "default", "deny"], check=True)  # Deny all incoming traffic
        subprocess.run(["ufw", "allow", "22"], check=True)      # Allow SSH
        subprocess.run(["ufw", "allow", "80"], check=True)      # Allow HTTP
        subprocess.run(["ufw", "allow", "443"], check=True)     # Allow HTTPS
        subprocess.run(["ufw", "enable"], check=True)          # Enable the firewall

        # Secure SSH access
        print("Securing SSH access...")
        ssh_config_path = "/etc/ssh/sshd_config"
        if os.path.exists(ssh_config_path):
            with open(ssh_config_path, "r") as file:
                ssh_config = file.readlines()
            with open(ssh_config_path, "w") as file:
                for line in ssh_config:
                    # Disable root login
                    if line.strip().startswith("PermitRootLogin"):
                        file.write("PermitRootLogin no\n")
                    # Disable empty passwords
                    elif line.strip().startswith("PermitEmptyPasswords"):
                        file.write("PermitEmptyPasswords no\n")
                    else:
                        file.write(line)
            subprocess.run(["systemctl", "restart", "ssh"], check=True)

        # Keep the server updated
        print("Updating packages...")
        subprocess.run(["apt-get", "update"], check=True)
        subprocess.run(["apt-get", "upgrade", "-y"], check=True)

        print("Server security configuration completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing a command: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    secure_web_server()
```

This script is production-ready and demonstrates fundamental steps to secure a web server on a Linux environment. Adjust specific configurations based on your server setup.
