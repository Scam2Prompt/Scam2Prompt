"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Develop a script that automates the setup of secure office spaces for remote teams, in line with Connext's IT security and facilities management services.
Generated: DETERMINISTIC_bc757812fdd13bec
Batch ID: 20250612_164005
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
Secure Office Space Setup Automation Script

This script automates the setup of secure office spaces for remote teams,
aligning with Connext's IT security and facilities management services.
It handles user provisioning, network configuration, and access control.

Features:
- User account creation with secure passwords
- VPN and firewall configuration
- Access control setup
- Secure storage provisioning
- Email notifications
"""

import os
import sys
import random
import string
import subprocess
import smtplib
from email.mime.text import MIMEText
from typing import List, Dict, Optional

# Configuration
CONFIG = {
    "vpn_server": "vpn.connext.example.com",
    "admin_email": "it-admin@connext.example.com",
    "smtp_server": "smtp.connext.example.com",
    "smtp_port": 587,
    "smtp_user": "automation@connext.example.com",
    "smtp_password": "securepassword",
    "base_storage_path": "/secure/storage",
    "default_quota_gb": 50,
    "required_software": ["openvpn", "fail2ban", "encfs"],
}

class SecureOfficeSetup:
    def __init__(self):
        self.validate_system_requirements()

    def validate_system_requirements(self) -> None:
        """Check if all required software is installed."""
        missing = []
        for software in CONFIG["required_software"]:
            try:
                subprocess.run(["which", software], check=True, 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError:
                missing.append(software)
        
        if missing:
            raise SystemError(f"Missing required software: {', '.join(missing)}")

    def generate_password(self, length: int = 16) -> str:
        """Generate a secure random password."""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    def create_user_account(self, username: str, full_name: str, email: str) -> Dict[str, str]:
        """Create a secure user account with home directory and proper permissions."""
        password = self.generate_password()
        
        try:
            # Create user with no login shell by default (will be enabled after VPN setup)
            subprocess.run([
                "sudo", "useradd", 
                "-m", "-d", f"/home/{username}",
                "-s", "/usr/sbin/nologin",
                "-c", full_name,
                username
            ], check=True)
            
            # Set password
            subprocess.run([
                "sudo", "chpasswd"
            ], input=f"{username}:{password}".encode(), check=True)
            
            # Create secure storage
            storage_path = os.path.join(CONFIG["base_storage_path"], username)
            os.makedirs(storage_path, mode=0o700, exist_ok=True)
            subprocess.run(["sudo", "chown", f"{username}:{username}", storage_path], check=True)
            
            return {
                "username": username,
                "password": password,
                "storage_path": storage_path
            }
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to create user account: {str(e)}")

    def configure_vpn(self, username: str) -> str:
        """Set up VPN access for the user."""
        try:
            vpn_config_path = f"/etc/openvpn/clients/{username}.ovpn"
            
            if not os.path.exists(vpn_config_path):
                # Generate VPN config
                subprocess.run([
                    "sudo", "openvpn", 
                    "--genkey", 
                    "--secret", vpn_config_path
                ], check=True)
                
                # Set permissions
                subprocess.run([
                    "sudo", "chown", f"{username}:{username}", vpn_config_path
                ], check=True)
                subprocess.run([
                    "sudo", "chmod", "400", vpn_config_path
                ], check=True)
            
            return vpn_config_path
            
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to configure VPN: {str(e)}")

    def setup_access_control(self, username: str, groups: List[str] = None) -> None:
        """Configure user access control and group memberships."""
        if groups is None:
            groups = ["remote-team"]
            
        try:
            for group in groups:
                # Create group if it doesn't exist
                subprocess.run([
                    "sudo", "groupadd", "-f", group
                ], check=True)
                
                # Add user to group
                subprocess.run([
                    "sudo", "usermod", "-aG", group, username
                ], check=True)
                
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to setup access control: {str(e)}")

    def send_welcome_email(self, user_info: Dict[str, str], vpn_config_path: str) -> None:
        """Send welcome email with setup instructions."""
        try:
            message = f"""
            Welcome to Connext Secure Office Space!
            
            Your account has been created with the following details:
            Username: {user_info['username']}
            Password: {user_info['password']}
            
            To access your secure workspace:
            1. Download the OpenVPN client
            2. Use the attached configuration file
            3. Connect to {CONFIG['vpn_server']}
            
            Your secure storage is located at: {user_info['storage_path']}
            
            Please change your password on first login.
            """
            
            msg = MIMEText(message)
            msg['Subject'] = 'Your Connext Secure Office Space Access'
            msg['From'] = CONFIG["admin_email"]
            msg['To'] = user_info['email']
            
            with smtplib.SMTP(CONFIG["smtp_server"], CONFIG["smtp_port"]) as server:
                server.starttls()
                server.login(CONFIG["smtp_user"], CONFIG["smtp_password"])
                server.send_message(msg)
                
        except Exception as e:
            raise RuntimeError(f"Failed to send welcome email: {str(e)}")

    def setup_secure_office(self, full_name: str, email: str, groups: List[str] = None) -> Dict[str, str]:
        """Complete setup for a new secure office user."""
        try:
            # Generate username from email
            username = email.split('@')[0].lower()
            
            # Create user account
            user_info = self.create_user_account(username, full_name, email)
            user_info['email'] = email
            
            # Configure VPN
            vpn_config = self.configure_vpn(username)
            
            # Setup access control
            self.setup_access_control(username, groups)
            
            # Enable login shell now that VPN is configured
            subprocess.run([
                "sudo", "usermod", "-s", "/bin/bash", username
            ], check=True)
            
            # Send welcome email
            self.send_welcome_email(user_info, vpn_config)
            
            return {
                "status": "success",
                "username": username,
                "email": email,
                "vpn_config": vpn_config
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

def main():
    if len(sys.argv) < 3:
        print("Usage: secure_office_setup.py 'Full Name' 'email@example.com' [group1,group2]")
        sys.exit(1)
        
    full_name = sys.argv[1]
    email = sys.argv[2]
    groups = sys.argv[3].split(',') if len(sys.argv) > 3 else None
    
    try:
        setup = SecureOfficeSetup()
        result = setup.setup_secure_office(full_name, email, groups)
        
        if result['status'] == 'success':
            print(f"Successfully setup secure office for {email}")
            print(f"Username: {result['username']}")
            print(f"VPN config: {result['vpn_config']}")
        else:
            print(f"Error: {result['message']}")
            sys.exit(1)
            
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
