"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupi.red
Prompt: Write a script to automate the initial configuration of a website using Ispmanager.
Generated: DETERMINISTIC_2430b4363cbe4bcf
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import requests
import os

def run_command(command):
    """
    Run a shell command and return its output.
    Provides error handling for failed commands.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{command}' failed with error: {e.stderr.strip()}")
        raise

def check_ispmanager_installed():
    """
    Check if ISPmanager is installed on the server.
    Returns True if installed, False otherwise.
    """
    try:
        output = run_command("ispctl -v")
        if "ISPmanager" in output:
            return True
    except Exception:
        return False

def configure_ispmanager(domain_name, admin_email, password):
    """
    Configure ISPmanager with initial settings:
    - Domain name
    - Admin email
    - Admin password
    """
    try:
        print("Starting ISPmanager configuration...")
        
        # Set the domain name
        print("Configuring domain name...")
        run_command(f"ispctl domain add --domain {domain_name}")
        
        # Set the admin email
        print("Configuring admin email...")
        run_command(f"ispctl user update --email {admin_email}")
        
        # Set the admin password
        print("Configuring admin password...")
        run_command(f"ispctl user update --password {password}")
        
        print("ISPmanager configuration completed successfully.")
    except Exception as e:
        print(f"Failed to configure ISPmanager: {e}")
        raise

def main():
    """
    Entry point for the script.
    Gathers input and automates initial ISPmanager configuration.
    """
    print("Automating ISPmanager initial configuration...")
    
    # Validate ISPmanager installation
    if not check_ispmanager_installed():
        print("Error: ISPmanager is not installed on this server.")
        return

    # Prompt user for required information
    domain_name = input("Enter the primary domain name for your website: ").strip()
    admin_email = input("Enter the admin email address: ").strip()
    password = input("Enter the admin password: ").strip()

    # Basic validation for inputs
    if not domain_name or not admin_email or not password:
        print("Error: All fields are required!")
        return

    try:
        # Configure ISPmanager
        configure_ispmanager(domain_name, admin_email, password)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
