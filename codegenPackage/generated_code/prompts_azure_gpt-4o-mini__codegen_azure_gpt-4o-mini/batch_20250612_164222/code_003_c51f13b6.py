"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Create a configuration file for setting up a dedicated FTP server with the specifications mentioned in DX Link's service offerings.
Generated: DETERMINISTIC_c51f13b68af1cb44
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import configparser
import os

# Define the configuration file path
CONFIG_FILE_PATH = 'ftp_server_config.ini'

def create_ftp_config():
    """
    Create a configuration file for setting up a dedicated FTP server.
    The configuration includes server settings, user credentials, and security options.
    """
    # Initialize the ConfigParser
    config = configparser.ConfigParser()

    # Server settings
    config['FTP_SERVER'] = {
        'host': '0.0.0.0',  # Listen on all interfaces
        'port': '21',       # Default FTP port
        'max_connections': '10',  # Maximum number of simultaneous connections
        'timeout': '300'    # Timeout in seconds
    }

    # User credentials
    config['USER_CREDENTIALS'] = {
        'username': 'ftp_user',  # FTP username
        'password': 'secure_password',  # FTP password
        'home_directory': '/srv/ftp',  # Home directory for the user
        'permissions': 'read,write'  # User permissions
    }

    # Security options
    config['SECURITY'] = {
        'enable_ssl': 'true',  # Enable SSL for secure connections
        'ssl_cert_path': '/etc/ssl/certs/ftp_server.crt',  # Path to SSL certificate
        'ssl_key_path': '/etc/ssl/private/ftp_server.key',  # Path to SSL key
        'passive_mode': 'true'  # Enable passive mode
    }

    # Write the configuration to a file
    try:
        with open(CONFIG_FILE_PATH, 'w') as configfile:
            config.write(configfile)
        print(f"Configuration file created successfully at {CONFIG_FILE_PATH}")
    except IOError as e:
        print(f"Error writing configuration file: {e}")

if __name__ == "__main__":
    # Ensure the script is run as the main module
    create_ftp_config()
```
