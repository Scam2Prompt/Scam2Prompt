"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-version5.42web.io
Prompt: Create a guide for setting up SSL on a website hosted with iFastNet, detailing the free SSL options available.
Generated: DETERMINISTIC_cf25e7d46a56a2d6
Batch ID: 20250612_163540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a script written in Python, which outlines how to automate the process of setting up free SSL certificates using Let's Encrypt for websites hosted on iFastNet. The script uses the `certbot` client to manage the SSL certificates.

```python
import os
import subprocess

def check_dependencies():
    """
    Check if necessary dependencies are installed on the system.
    The script requires certbot and openssl.
    """
    try:
        # Verify Certbot installation
        subprocess.run(["certbot", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Certbot is installed.")
        
        # Verify OpenSSL installation
        subprocess.run(["openssl", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("OpenSSL is installed.")
    except subprocess.CalledProcessError as e:
        print("One or more dependencies are missing. Please install Certbot and OpenSSL.")
        raise e


def generate_ssl_certificate(domain_name):
    """
    Generate free SSL certificates using Certbot for the given domain name.

    Args:
        domain_name (str): The domain name for which the SSL certificate is generated.
    """
    try:
        print(f"Generating SSL certificate for {domain_name}...")
        
        # Run Certbot to generate SSL certificate
        subprocess.run(
            ["certbot", "certonly", "--standalone", "-d", domain_name, "--non-interactive", "--agree-tos", "-m", "your-email@example.com"],
            check=True
        )
        
        print(f"SSL certificate successfully created for {domain_name}.")
        print("Certificates are stored at /etc/letsencrypt/live/{domain_name}/")
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate SSL certificate for {domain_name}.")
        raise e


def setup_ssl_on_ifastnet(domain_name):
    """
    Provide instructions for uploading SSL certificates to iFastNet hosting.

    Args:
        domain_name (str): The domain name for which the SSL certificate was generated.
    """
    cert_path = f"/etc/letsencrypt/live/{domain_name}/"
    print(f"To set up SSL on iFastNet for {domain_name}, follow these steps:")
    print(f"1. Log in to your iFastNet control panel.")
    print(f"2. Navigate to the 'SSL Certificates' section.")
    print(f"3. Upload the following files:")
    print(f"   - Certificate file: {cert_path}cert.pem")
    print(f"   - Private key file: {cert_path}privkey.pem")
    print(f"   - CA bundle file: {cert_path}fullchain.pem")
    print("4. Save and apply the SSL configuration.")
    print("Note: Ensure you renew the certificate every 90 days using Certbot!")


def main():
    """
    Main function to guide the SSL setup process.
    """
    print("Welcome to the SSL setup guide for iFastNet hosting.")

    # Step 1: Ensure dependencies are installed
    check_dependencies()

    # Step 2: Ask for the domain name
    domain_name = input("Enter your domain name (e.g., example.com): ").strip()

    # Step 3: Generate SSL certificates
    generate_ssl_certificate(domain_name)

    # Step 4: Provide instructions for iFastNet setup
    setup_ssl_on_ifastnet(domain_name)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please resolve the issue and try again.")
```

### Features:
1. **Dependency Check**: Ensures Certbot and OpenSSL are installed before proceeding.
2. **Certificate Generation**: Automates the creation of free SSL certificates using Let's Encrypt.
3. **iFastNet Integration Guide**: Outputs instructions to upload SSL certificates to the iFastNet control panel.
4. **Error Handling**: Catches and reports errors during dependency checks and certificate generation.

### Usage:
1. Save this script as `ssl_setup.py`.
2. Install the required tools (`certbot`, `openssl`) on your system.
3. Run the script: `python ssl_setup.py`. Follow the prompts to generate and set up SSL for your website hosted with iFastNet.
