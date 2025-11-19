"""
Generated Code Metadata:
========================
Original URL: https://apps-game7.xyz
Prompt: Suggest best practices for securing a newly configured web server against common vulnerabilities.
Generated: DETERMINISTIC_ae6d64774946ae4b
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Web Server Hardening Script
This script provides best practices for securing a newly configured web server.
"""

import os
import subprocess
import sys
from typing import List, Optional

def check_root() -> None:
    """Ensure the script is run as root."""
    if os.geteuid() != 0:
        print("Error: This script must be run as root.")
        sys.exit(1)

def run_command(cmd: List[str]) -> Optional[str]:
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {' '.join(cmd)}")
        print(f"Error: {e.stderr}")
        return None

def update_system() -> None:
    """Update the system packages."""
    print("Updating system packages...")
    run_command(["apt", "update"])
    run_command(["apt", "upgrade", "-y"])
    run_command(["apt", "autoremove", "-y"])

def configure_firewall() -> None:
    """Configure UFW firewall with basic rules."""
    print("Configuring firewall...")
    run_command(["ufw", "default", "deny", "incoming"])
    run_command(["ufw", "default", "allow", "outgoing"])
    run_command(["ufw", "allow", "ssh"])
    run_command(["ufw", "allow", "http"])
    run_command(["ufw", "allow", "https"])
    run_command(["ufw", "enable"])

def secure_ssh() -> None:
    """Harden SSH configuration."""
    print("Securing SSH...")
    ssh_config = "/etc/ssh/sshd_config"
    
    # Backup original config
    run_command(["cp", ssh_config, f"{ssh_config}.bak"])
    
    # Apply security settings
    replacements = [
        ("#PermitRootLogin yes", "PermitRootLogin no"),
        ("#PasswordAuthentication yes", "PasswordAuthentication no"),
        ("#PubkeyAuthentication yes", "PubkeyAuthentication yes"),
        ("#Port 22", "Port 2222"),  # Change to your preferred port
    ]
    
    with open(ssh_config, "r") as f:
        lines = f.readlines()
    
    with open(ssh_config, "w") as f:
        for line in lines:
            for old, new in replacements:
                if line.strip() == old:
                    line = new + "\n"
            f.write(line)
    
    run_command(["systemctl", "restart", "ssh"])

def install_security_tools() -> None:
    """Install essential security tools."""
    print("Installing security tools...")
    tools = [
        "fail2ban",
        "unattended-upgrades",
        "clamav",
        "rkhunter",
        "lynis"
    ]
    run_command(["apt", "install", "-y"] + tools)

def configure_automatic_updates() -> None:
    """Enable automatic security updates."""
    print("Configuring automatic updates...")
    auto_updates = "/etc/apt/apt.conf.d/20auto-upgrades"
    with open(auto_updates, "w") as f:
        f.write('APT::Periodic::Update-Package-Lists "1";\n')
        f.write('APT::Periodic::Unattended-Upgrade "1";\n')
    run_command(["systemctl", "enable", "--now", "unattended-upgrades"])

def disable_unused_services() -> None:
    """Disable unnecessary services."""
    print("Disabling unused services...")
    services = [
        "telnet",
        "ftp",
        "rpcbind",
        "nfs-kernel-server"
    ]
    for service in services:
        run_command(["systemctl", "stop", service])
        run_command(["systemctl", "disable", service])

def set_file_permissions() -> None:
    """Set secure file permissions."""
    print("Setting secure file permissions...")
    directories = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/group",
        "/etc/sudoers",
        "/var/www"
    ]
    for directory in directories:
        run_command(["chmod", "-R", "750", directory])
        run_command(["chown", "-R", "root:root", directory])

def main() -> None:
    """Main function to execute all hardening steps."""
    try:
        check_root()
        update_system()
        configure_firewall()
        secure_ssh()
        install_security_tools()
        configure_automatic_updates()
        disable_unused_services()
        set_file_permissions()
        print("Server hardening completed successfully!")
    except Exception as e:
        print(f"Error during hardening: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
