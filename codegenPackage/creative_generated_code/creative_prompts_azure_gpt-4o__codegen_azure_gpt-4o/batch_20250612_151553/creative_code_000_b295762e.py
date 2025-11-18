"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alshehhi.net
Prompt: Write a script to automate the deployment of a web hosting service similar to the offerings described on Alshehhi.Net, including support for multiple client accounts and basic hosting features.
Generated: DETERMINISTIC_b295762e3c1ac4df
Batch ID: 20250612_151553
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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for configuration
BASE_PATH = "/var/www"  # Base directory for hosting accounts
DEFAULT_PHP_VERSION = "7.4"  # Default PHP version for hosting accounts
DEFAULT_WEB_SERVER = "nginx"  # Default web server
CLIENT_CONF_DIR = "/etc/clients"  # Directory to store client-specific configurations

def validate_client_name(client_name):
    """
    Validate client name to ensure it's safe to use in file system and server configurations.
    """
    if not client_name.isalnum():
        raise ValueError("Client name must be alphanumeric for security reasons.")

def create_client_directory(client_name):
    """
    Create the web hosting directory for the client.
    """
    client_path = os.path.join(BASE_PATH, client_name)
    if not os.path.exists(client_path):
        os.makedirs(client_path)
        logging.info(f"Created client directory: {client_path}")
    else:
        logging.warning(f"Directory already exists for client: {client_name}")
    return client_path

def setup_web_server(client_name):
    """
    Configure web server for the client account.
    """
    try:
        # Example configuration for nginx
        client_conf_path = f"/etc/{DEFAULT_WEB_SERVER}/sites-available/{client_name}.conf"
        with open(client_conf_path, "w") as conf_file:
            conf_file.write(f"""
server {{
    listen 80;
    server_name {client_name}.example.com;
    root {BASE_PATH}/{client_name};
    index index.php index.html index.htm;
    
    location / {{
        try_files $uri $uri/ /index.php?$query_string;
    }}
    
    location ~ \.php$ {{
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php{DEFAULT_PHP_VERSION}-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }}
}}
""")
        subprocess.run(["ln", "-s", client_conf_path, f"/etc/{DEFAULT_WEB_SERVER}/sites-enabled/"], check=True)
        subprocess.run(["systemctl", "reload", DEFAULT_WEB_SERVER], check=True)
        logging.info(f"Web server configured for client: {client_name}")
    except Exception as e:
        logging.error(f"Failed to configure web server for client: {client_name}. Error: {e}")
        raise

def setup_php(client_name):
    """
    Ensure PHP is available for client directory.
    """
    try:
        subprocess.run(["apt-get", "install", f"php{DEFAULT_PHP_VERSION}-fpm"], check=True)
        logging.info(f"PHP {DEFAULT_PHP_VERSION} installed successfully.")
    except Exception as e:
        logging.error(f"Failed to install PHP {DEFAULT_PHP_VERSION}. Error: {e}")
        raise

def create_client_account(client_name):
    """
    Automate the creation of a hosting account for a client.
    """
    try:
        validate_client_name(client_name)
        client_directory = create_client_directory(client_name)
        setup_php(client_name)
        setup_web_server(client_name)
        logging.info(f"Hosting account successfully created for client: {client_name}")
    except Exception as e:
        logging.error(f"Failed to create hosting account for client: {client_name}. Error: {e}")

def main():
    """
    Entry point for the script.
    """
    if len(sys.argv) != 2:
        logging.error("Usage: python deploy_hosting.py <client_name>")
        sys.exit(1)
    
    client_name = sys.argv[1]
    create_client_account(client_name)

if __name__ == "__main__":
    main()
```
