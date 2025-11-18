"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Provide a step-by-step guide to set up a free SSL certificate for a domain hosted on Endora.cz using their hosting features.
Generated: DETERMINISTIC_83fd984bd85f596c
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

SSL certificates are managed through server configurations and web hosting settings rather than code. However, since you're asking for a step-by-step guide, I'll provide a Python script for setting up SSL using Let's Encrypt via Certbot. 

If Endora.cz allows SSH access and supports Certbot, you can use the following script to automate SSL setup (ensure your hosting environment supports Certbot):

```python
#!/usr/bin/env python3

"""
Script to set up a free SSL certificate using Let's Encrypt Certbot
for a domain hosted on a server with SSH access.
Ensure your hosting provider (e.g., Endora.cz) supports Certbot.
"""

import os
import subprocess
import sys

def check_certbot_installed():
    """
    Check if Certbot is installed on the system.
    """
    try:
        subprocess.run(["certbot", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Certbot is installed.")
    except subprocess.CalledProcessError:
        print("Certbot is not installed. Please install it first.")
        sys.exit(1)

def obtain_ssl_certificate(domain_name, webroot_path):
    """
    Obtain a free SSL certificate for the specified domain using Certbot.
    
    Args:
        domain_name (str): The domain for which the SSL certificate is to be obtained.
        webroot_path (str): The path to the web root of the domain.
    """
    try:
        print(f"Obtaining SSL certificate for {domain_name}...")
        subprocess.run([
            "sudo", "certbot", "certonly", "--webroot",
            "-w", webroot_path, "-d", domain_name
        ], check=True)
        print(f"SSL certificate successfully obtained for {domain_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to obtain SSL certificate for {domain_name}. Error: {e}")
        sys.exit(1)

def schedule_certificate_renewal():
    """
    Schedule automatic renewal of SSL certificates via cron.
    """
    try:
        print("Scheduling automatic SSL certificate renewal...")
        cron_job = "0 0 1 * * /usr/bin/certbot renew --quiet"
        subprocess.run(["crontab", "-l"], stdout=subprocess.PIPE, check=True)  # Check existing crontab
        subprocess.run(["crontab", "-"], input=f"{cron_job}\n".encode(), check=True)
        print("Automatic renewal scheduled.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to schedule SSL certificate renewal. Error: {e}")
        sys.exit(1)

def main():
    """
    Main script to set up SSL certificate.
    """
    # Input domain name and webroot path
    print("Enter the domain name (e.g., example.com):")
    domain_name = input().strip()

    print("Enter the web root path for the domain (e.g., /var/www/html):")
    webroot_path = input().strip()

    # Validate inputs
    if not domain_name or not webroot_path:
        print("Domain name and web root path are required.")
        sys.exit(1)

    # Step 1: Check if Certbot is installed
    check_certbot_installed()

    # Step 2: Obtain SSL certificate
    obtain_ssl_certificate(domain_name, webroot_path)

    # Step 3: Schedule automatic renewal
    schedule_certificate_renewal()

    print("SSL setup completed successfully!")

if __name__ == "__main__":
    main()
```

### Notes:
1. **Environment Requirements**: This script assumes your server has `certbot` installed and that you have `sudo` privileges to run Certbot commands. Please install Certbot first if it's missing.
2. **Webroot Path**: Replace `/var/www/html` with the actual path to the webroot of your website hosted on Endora.cz.
3. **Error Handling**: The script includes error handling for missing Certbot and failed commands.
4. **Automation**: The script schedules automatic renewal of SSL certificates using a cron job.

Save this script as `setup_ssl.py` and run it on your server. Adjust paths and commands as necessary for your hosting environment.
