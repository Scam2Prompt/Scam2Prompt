"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binairop.com
Prompt: What are the best practices for managing shared IP addresses across multiple domains in a web server setup?
Generated: DETERMINISTIC_5a66d5946e5d9ab4
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script demonstrates how to manage shared IP addresses across 
multiple domains in a web server setup by using configuration templates 
and logging for diagnostics. This example assumes the use of Nginx.
"""

import os
import logging

# Logging configuration
LOG_FILE = "shared_ip_management.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Constants
NGINX_CONFIG_DIR = "/etc/nginx/sites-available"
NGINX_ENABLED_DIR = "/etc/nginx/sites-enabled"
SHARED_IP = "192.168.1.100"  # Replace with your shared IP address


def create_nginx_config(domain_name, shared_ip):
    """
    Creates an Nginx configuration file for a given domain with a shared IP address.

    Args:
        domain_name (str): The domain name for the virtual host.
        shared_ip (str): The shared IP address.

    Returns:
        str: Path to the created configuration file.
    """
    config_content = f"""
server {{
    listen {shared_ip}:80;
    server_name {domain_name};

    root /var/www/{domain_name}/html;
    index index.html index.htm;

    location / {{
        try_files $uri $uri/ =404;
    }}

    error_page 404 /404.html;

    location = /404.html {{
        root /var/www/{domain_name}/html;
    }}

    log_format custom '$remote_addr - $remote_user [$time_local] '
                       '"$request" $status $body_bytes_sent '
                       '"$http_referer" "$http_user_agent"';

    access_log /var/log/nginx/{domain_name}_access.log custom;
    error_log /var/log/nginx/{domain_name}_error.log;
}}
"""
    config_path = os.path.join(NGINX_CONFIG_DIR, domain_name)
    try:
        with open(config_path, "w") as config_file:
            config_file.write(config_content)
        logging.info(f"Nginx config created for domain: {domain_name}")
    except Exception as e:
        logging.error(f"Failed to create Nginx config for domain {domain_name}: {e}")
        raise
    return config_path


def enable_nginx_config(domain_name):
    """
    Enables an Nginx configuration by creating a symbolic link in the sites-enabled directory.

    Args:
        domain_name (str): The domain name for the virtual host.

    Returns:
        None
    """
    enabled_path = os.path.join(NGINX_ENABLED_DIR, domain_name)
    available_path = os.path.join(NGINX_CONFIG_DIR, domain_name)
    try:
        if not os.path.exists(enabled_path):
            os.symlink(available_path, enabled_path)
            logging.info(f"Nginx config enabled for domain: {domain_name}")
        else:
            logging.warning(f"Nginx config for domain {domain_name} is already enabled.")
    except Exception as e:
        logging.error(f"Failed to enable Nginx config for domain {domain_name}: {e}")
        raise


# Example Usage
def setup_shared_ip_domains(domains, shared_ip):
    """
    Sets up multiple domains with a shared IP address.

    Args:
        domains (list): List of domain names.
        shared_ip (str): The shared IP address.

    Returns:
        None
    """
    for domain in domains:
        try:
            # Step 1: Create the Nginx configuration file
            create_nginx_config(domain, shared_ip)

            # Step 2: Enable the configuration
            enable_nginx_config(domain)

            # Step 3: Create necessary directories for the domain
            domain_root = f"/var/www/{domain}/html"
            os.makedirs(domain_root, exist_ok=True)
            logging.info(f"Directory structure created for domain: {domain}")
        except Exception as e:
            logging.error(f"Failed to set up domain {domain}: {e}")


if __name__ == "__main__":
    # Example domains
    domains_to_setup = ["example.com", "test.com", "demo.org"]

    try:
        # Set up shared IP for the provided domains
        setup_shared_ip_domains(domains_to_setup, SHARED_IP)

        logging.info("All domains were successfully set up.")
    except Exception as e:
        logging.critical(f"Critical error occurred during setup: {e}")
```
