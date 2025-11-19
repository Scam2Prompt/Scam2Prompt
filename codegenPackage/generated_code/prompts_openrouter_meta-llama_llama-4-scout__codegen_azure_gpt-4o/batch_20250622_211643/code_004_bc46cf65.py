"""
Generated Code Metadata:
========================
Original URL: https://mindsol.app
Prompt: Write a script to automate tasks on a LiteSpeed Web Server, such as setting up virtual hosts or managing SSL certificates, using a programming language of choice.
Generated: DETERMINISTIC_bc46cf65dc0dd638
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import json

# Constants
LITESPEED_CONFIG_PATH = "/usr/local/lsws/conf/httpd_config.conf"
VHOSTS_DIR = "/usr/local/lsws/conf/vhosts"
SSL_CERTS_DIR = "/usr/local/lsws/ssl"

# Helper function to execute shell commands
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr.decode('utf-8')}")
        return None

# Function to create a virtual host
def create_virtual_host(vhost_name, document_root, domain_name):
    vhost_config_path = os.path.join(VHOSTS_DIR, f"{vhost_name}.conf")
    try:
        # Create virtual host configuration file
        with open(vhost_config_path, 'w') as vhost_file:
            vhost_file.write(f"""
<VirtualHost {domain_name}>
    DocumentRoot {document_root}
    ServerName {domain_name}
    ErrorLog logs/{vhost_name}_error.log
    CustomLog logs/{vhost_name}_access.log combined
</VirtualHost>
""")
        print(f"Virtual host '{vhost_name}' created successfully.")
    except Exception as e:
        print(f"Error creating virtual host: {e}")

# Function to enable SSL for a virtual host
def enable_ssl(vhost_name, domain_name, cert_path, key_path):
    vhost_config_path = os.path.join(VHOSTS_DIR, f"{vhost_name}.conf")
    try:
        # Append SSL configuration to the virtual host file
        with open(vhost_config_path, 'a') as vhost_file:
            vhost_file.write(f"""
<VirtualHost {domain_name}:443>
    DocumentRoot {document_root}
    ServerName {domain_name}
    SSLEngine on
    SSLCertificateFile {cert_path}
    SSLCertificateKeyFile {key_path}
    ErrorLog logs/{vhost_name}_ssl_error.log
    CustomLog logs/{vhost_name}_ssl_access.log combined
</VirtualHost>
""")
        print(f"SSL enabled for virtual host '{vhost_name}'.")
    except Exception as e:
        print(f"Error enabling SSL: {e}")

# Function to reload LiteSpeed Web Server
def reload_litespeed():
    command = "/usr/local/lsws/bin/lswsctrl restart"
    result = run_command(command)
    if result:
        print("LiteSpeed Web Server reloaded successfully.")
    else:
        print("Failed to reload LiteSpeed Web Server.")

# Main function
def main():
    print("LiteSpeed Web Server Automation Script")
    print("1. Create Virtual Host")
    print("2. Enable SSL for Virtual Host")
    print("3. Reload LiteSpeed Web Server")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        vhost_name = input("Enter virtual host name: ")
        document_root = input("Enter document root path: ")
        domain_name = input("Enter domain name: ")
        create_virtual_host(vhost_name, document_root, domain_name)
    elif choice == "2":
        vhost_name = input("Enter virtual host name: ")
        domain_name = input("Enter domain name: ")
        cert_path = input("Enter SSL certificate path: ")
        key_path = input("Enter SSL certificate key path: ")
        enable_ssl(vhost_name, domain_name, cert_path, key_path)
    elif choice == "3":
        reload_litespeed()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
```
