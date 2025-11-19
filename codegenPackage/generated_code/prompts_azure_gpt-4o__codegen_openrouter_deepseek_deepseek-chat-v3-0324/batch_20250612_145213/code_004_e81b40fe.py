"""
Generated Code Metadata:
========================
Original URL: https://webautomigrate.hstn.me
Prompt: Create a guide for setting up email accounts on a hosting platform with multiple email account support and modern cPanel, such as iFastNet.
Generated: DETERMINISTIC_e81b40fe2fb6b438
Batch ID: 20250612_145213
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
Email Account Setup Guide for Hosting Platforms with cPanel (e.g., iFastNet)

This script provides a step-by-step guide for setting up email accounts on a hosting platform
with cPanel interface. It includes functions to validate inputs and simulate the setup process.
"""

import re
import getpass
import smtplib
from typing import Tuple, Optional

class EmailAccountSetup:
    """
    A class to handle email account setup on cPanel hosting platforms.
    """
    
    def __init__(self, domain: str):
        """
        Initialize with the domain name for email accounts.
        
        Args:
            domain (str): The domain name (e.g., 'example.com')
        """
        if not self._validate_domain(domain):
            raise ValueError("Invalid domain format")
        self.domain = domain
        self.accounts = []
    
    @staticmethod
    def _validate_domain(domain: str) -> bool:
        """
        Validate domain name format.
        
        Args:
            domain (str): Domain name to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        pattern = r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
        return re.match(pattern, domain) is not None
    
    @staticmethod
    def _validate_email_local_part(local_part: str) -> bool:
        """
        Validate the local part of an email address.
        
        Args:
            local_part (str): The part before @ in email
            
        Returns:
            bool: True if valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+$'
        return re.match(pattern, local_part) is not None
    
    @staticmethod
    def _validate_password(password: str) -> bool:
        """
        Validate password meets complexity requirements.
        
        Args:
            password (str): Password to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        return True
    
    def create_email_account(self, username: str, password: str, quota_mb: int = 500) -> Tuple[bool, str]:
        """
        Simulate creating an email account in cPanel.
        
        Args:
            username (str): Email username (local part)
            password (str): Account password
            quota_mb (int): Mailbox quota in MB (default: 500)
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        if not self._validate_email_local_part(username):
            return False, "Invalid username format"
        
        if not self._validate_password(password):
            return False, "Password doesn't meet complexity requirements"
        
        if quota_mb <= 0:
            return False, "Quota must be positive"
        
        email = f"{username}@{self.domain}"
        if email in self.accounts:
            return False, "Email account already exists"
        
        # In a real implementation, this would call cPanel API
        self.accounts.append(email)
        return True, f"Successfully created {email} with {quota_mb}MB quota"
    
    def test_email_connection(self, email: str, password: str, smtp_server: str = "mail.yourdomain.com") -> bool:
        """
        Test SMTP connection for the email account.
        
        Args:
            email (str): Full email address
            password (str): Account password
            smtp_server (str): SMTP server address
            
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            with smtplib.SMTP(smtp_server, 587) as server:
                server.starttls()
                server.login(email, password)
            return True
        except smtplib.SMTPException as e:
            print(f"SMTP connection failed: {str(e)}")
            return False
        except Exception as e:
            print(f"Error testing connection: {str(e)}")
            return False

def interactive_setup():
    """
    Interactive command-line interface for email setup.
    """
    print("Email Account Setup Guide for cPanel Hosting\n")
    
    # Get domain
    while True:
        domain = input("Enter your domain name (e.g., example.com): ").strip()
        if EmailAccountSetup._validate_domain(domain):
            break
        print("Invalid domain format. Please try again.")
    
    setup = EmailAccountSetup(domain)
    
    # Main menu
    while True:
        print("\nOptions:")
        print("1. Create new email account")
        print("2. Test email connection")
        print("3. List existing accounts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            # Create account
            while True:
                username = input("Enter email username (before @): ").strip()
                if setup._validate_email_local_part(username):
                    break
                print("Invalid username. Only letters, numbers, and .-_+ allowed.")
            
            while True:
                password = getpass.getpass("Enter password (min 8 chars, mixed case, numbers): ")
                if setup._validate_password(password):
                    confirm = getpass.getpass("Confirm password: ")
                    if password == confirm:
                        break
                    print("Passwords don't match!")
                else:
                    print("Password doesn't meet complexity requirements.")
            
            quota = input("Enter mailbox quota in MB (default 500): ").strip()
            try:
                quota = int(quota) if quota else 500
            except ValueError:
                print("Invalid quota, using default 500MB")
                quota = 500
            
            success, message = setup.create_email_account(username, password, quota)
            print(message)
        
        elif choice == "2":
            # Test connection
            if not setup.accounts:
                print("No accounts created yet.")
                continue
            
            email = input("Enter full email address to test: ").strip()
            if email not in setup.accounts:
                print("Account not found.")
                continue
            
            password = getpass.getpass(f"Enter password for {email}: ")
            if setup.test_email_connection(email, password):
                print("SMTP connection successful!")
            else:
                print("SMTP connection failed.")
        
        elif choice == "3":
            # List accounts
            if setup.accounts:
                print("\nExisting email accounts:")
                for account in setup.accounts:
                    print(f"- {account}")
            else:
                print("No accounts created yet.")
        
        elif choice == "4":
            print("Exiting setup guide.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        interactive_setup()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
