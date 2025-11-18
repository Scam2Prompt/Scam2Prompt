"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verificationmetamask.rf.gd
Prompt: Write a script to automate SSL certificate installation on a hosting service that offers free and simple SSL.
Generated: DETERMINISTIC_15d79c6e31e54419
Batch ID: 20250612_154222
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
import sys

def check_root_privileges():
    """
    Check if the script is being run with root privileges.
    """
    if os.geteuid() != 0:
        print("Error: This script must be run with root privileges.")
        sys.exit(1)

def install_dependencies():
    """
    Install necessary dependencies for SSL certificate installation.
    """
    try:
        print("Installing required dependencies...")
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'install', '-y', 'certbot', 'python3-certbot-nginx'], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def obtain_ssl_certificate(domain_name, email):
    """
    Obtain an SSL certificate using Certbot for the specified domain.
    
    Args:
        domain_name (str): The domain name for which the SSL certificate is to be installed.
        email (str): The email address to use for Certbot registration and renewal notifications.
    """
    try:
        print(f"Obtaining SSL certificate for domain: {domain_name}")
        subprocess.run([
            'certbot', '--nginx', '-d', domain_name, '--non-interactive', '--agree-tos', 
            '--email', email
        ], check=True)
        print("SSL certificate obtained successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error obtaining SSL certificate: {e}")
        sys.exit(1)

def reload_nginx():
    """
    Reload the Nginx server to apply SSL configuration changes.
    """
    try:
        print("Reloading Nginx server...")
        subprocess.run(['systemctl', 'reload', 'nginx'], check=True)
        print("Nginx reloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error reloading Nginx: {e}")
        sys.exit(1)

def main():
    """
    Main function to automate SSL certificate installation.
    """
    # Ensure the script is run as root
    check_root_privileges()

    # Prompt user for domain and email
    domain_name = input("Enter the domain name (e.g., example.com): ").strip()
    email = input("Enter your email address: ").strip()

    # Validate user inputs
    if not domain_name or not email:
        print("Error: Domain name and email address are required.")
        sys.exit(1)

    # Install required dependencies
    install_dependencies()

    # Obtain SSL certificate
    obtain_ssl_certificate(domain_name, email)

    # Reload Nginx to apply changes
    reload_nginx()

    print("SSL certificate installation completed successfully.")

if __name__ == "__main__":
    main()
```
