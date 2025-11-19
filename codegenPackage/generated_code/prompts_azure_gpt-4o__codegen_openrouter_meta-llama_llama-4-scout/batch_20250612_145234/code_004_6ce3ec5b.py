"""
Generated Code Metadata:
========================
Original URL: https://airdrop-stepngo.asia
Prompt: Write a step-by-step guide to configure a domain in FASTPANEL, ensuring proper SSL certificate installation and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_6ce3ec5bad1094bb
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that the request is not for code, but rather a step-by-step guide. However, I can provide a Python script that automates some of the steps involved in configuring a domain in FASTPANEL, installing an SSL certificate, and ensuring IPv4/IPv6 compatibility.

```python
import subprocess
import os

def configure_domain(domain, email):
    """
    Configure a domain in FASTPANEL.

    Args:
        domain (str): The domain to configure.
        email (str): The email address for SSL certificate registration.

    Returns:
        None
    """

    # Step 1: Add domain to FASTPANEL
    try:
        # Assuming FASTPANEL API endpoint and credentials are set as environment variables
        fastpanel_api_endpoint = os.environ['FASTPANEL_API_ENDPOINT']
        fastpanel_api_key = os.environ['FASTPANEL_API_KEY']

        # Using curl to interact with FASTPANEL API
        add_domain_command = f"curl -X POST '{fastpanel_api_endpoint}/domains' -H 'Authorization: Bearer {fastpanel_api_key}' -H 'Content-Type: application/json' -d '{\"domain\": \"{domain}\"}'"
        subprocess.run(add_domain_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error adding domain to FASTPANEL: {e}")

    # Step 2: Install SSL certificate using certbot
    try:
        install_ssl_command = f"certbot certonly --dns --dns-google --dns-google-credentials /etc/letsencrypt/dns-google-credentials --dns-google-propagation-seconds 120 --email {email} --agree-tos --non-interactive --expand --domain -d {domain}"
        subprocess.run(install_ssl_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error installing SSL certificate: {e}")

    # Step 3: Configure IPv4/IPv6 compatibility
    try:
        # Enable IPv6 on the server if not already enabled
        enable_ipv6_command = "sysctl -w net.ipv6.conf.all.disable_ipv6=0"
        subprocess.run(enable_ipv6_command, shell=True, check=True)

        # Restart web server to apply changes
        restart_web_server_command = "service nginx restart"
        subprocess.run(restart_web_server_command, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error configuring IPv4/IPv6 compatibility: {e}")


if __name__ == "__main__":
    domain = "example.com"
    email = "user@example.com"
    configure_domain(domain, email)
```

Please adjust the script according to your environment and replace the example domain and email with your own. 

Also, ensure that:

- `FASTPANEL_API_ENDPOINT` and `FASTPANEL_API_KEY` environment variables are set.
- `dns-google-credentials` file exists and has correct permissions.
- `certbot` and `nginx` are installed and configured properly. 

The code does not cover all steps that might be required for your specific use case, such as setting up FASTPANEL initially or detailed error handling for all potential issues. Always refer to the official documentation of the tools and services being used for the most accurate and detailed instructions.
