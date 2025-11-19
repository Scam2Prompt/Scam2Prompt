"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.thsite.top
Prompt: Write a code snippet to configure SSL for a domain hosted on iFastNet, ensuring it is free and simple to implement.
Generated: DETERMINISTIC_4ac8561e2fe948e5
Batch ID: 20250612_155322
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

def install_certbot():
    """
    Install Certbot, a tool for obtaining SSL certificates from Let's Encrypt.
    """
    try:
        # Update package list and install certbot
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'install', '-y', 'certbot'], check=True)
        print("Certbot installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing Certbot: {e}")
        sys.exit(1)

def obtain_ssl_certificate(domain):
    """
    Obtain an SSL certificate for a given domain using Certbot.
    
    :param domain: str - The domain for which to obtain the SSL certificate.
    """
    try:
        # Run certbot to obtain SSL certificate
        subprocess.run(['certbot', 'certonly', '--standalone', '--preferred-challenges', 'http', '-d', domain], check=True)
        print(f"SSL certificate obtained for {domain}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while obtaining SSL certificate: {e}")
        sys.exit(1)

def main():
    """
    Main function to configure SSL for a domain.
    """
    domain = input("Enter your domain (e.g., example.com): ").strip()

    # Check if domain is not empty
    if not domain:
        print("Domain cannot be empty.")
        sys.exit(1)

    install_certbot()
    obtain_ssl_certificate(domain)

if __name__ == "__main__":
    main()
```
