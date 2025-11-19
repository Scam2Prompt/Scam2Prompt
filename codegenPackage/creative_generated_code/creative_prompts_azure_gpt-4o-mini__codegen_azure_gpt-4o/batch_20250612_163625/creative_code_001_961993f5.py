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

def setup_web_server():
    """
    Perform initial setup tasks for a new web server.
    Includes updates, firewall configuration, and basic security enhancements.
    """
    try:
        # Step 1: Update and upgrade the system packages
        print("Updating and upgrading system packages...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "upgrade", "-y"], check=True)
        print("System packages updated and upgraded successfully.")

        # Step 2: Configure firewall
        print("Configuring firewall...")
        subprocess.run(["sudo", "ufw", "allow", "OpenSSH"], check=True)  # Allow SSH
        subprocess.run(["sudo", "ufw", "allow", "80"], check=True)       # Allow HTTP traffic
        subprocess.run(["sudo", "ufw", "allow", "443"], check=True)      # Allow HTTPS traffic
        subprocess.run(["sudo", "ufw", "enable"], check=True)
        print("Firewall configured successfully.")

        # Step 3: Secure the server
        print("Setting up basic security measures...")
        
        # Disable root login via SSH
        ssh_config_path = "/etc/ssh/sshd_config"
        if os.path.exists(ssh_config_path):
            with open(ssh_config_path, "r") as file:
                lines = file.readlines()
            with open(ssh_config_path, "w") as file:
                for line in lines:
                    if line.strip().startswith("PermitRootLogin"):
                        file.write("PermitRootLogin no\n")
                    else:
                        file.write(line)
            subprocess.run(["sudo", "service", "ssh", "restart"], check=True)
            print("Root login via SSH disabled successfully.")
        else:
            print(f"SSH configuration file not found at {ssh_config_path}. Skipping SSH security setup.")

        # Install fail2ban for protection against brute force attacks
        print("Installing fail2ban...")
        subprocess.run(["sudo", "apt-get", "install", "fail2ban", "-y"], check=True)
        print("Fail2ban installed successfully.")

        # Step 4: Install essential software packages
        print("Installing essential software packages...")
        essential_packages = ["curl", "wget", "git"]
        subprocess.run(["sudo", "apt-get", "install"] + essential_packages + ["-y"], check=True)
        print(f"Installed essential packages: {', '.join(essential_packages)}")

        # Step 5: Create a non-root user for administration
        print("Creating a non-root user...")
        new_user = "admin"
        subprocess.run(["sudo", "adduser", new_user], check=True)
        subprocess.run(["sudo", "usermod", "-aG", "sudo", new_user], check=True)
        print(f"Non-root user '{new_user}' created successfully.")

        print("Web server setup completed successfully.")

    except subprocess.CalledProcessError as error:
        print(f"Error during setup: {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the setup function
if __name__ == "__main__":
    setup_web_server()
```
