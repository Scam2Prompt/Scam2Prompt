"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Create a configuration file for setting up a dedicated FTP server with the specifications mentioned in DX Link's service offerings.
Generated: DETERMINISTIC_c51f13b68af1cb44
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script to create a configuration file for setting up a dedicated FTP server based on DX Link's service offerings. The configuration file is generated in the format typically used by FTP servers like vsftpd.

```python
import os

# Constants for the FTP server configuration
CONFIG_FILE_PATH = '/etc/vsftpd.conf'
FTP_SERVER_SETTINGS = {
    "listen": "YES",  # Enable standalone mode
    "listen_ipv6": "NO",  # Disable IPv6 support
    "anonymous_enable": "NO",  # Disable anonymous users
    "local_enable": "YES",  # Enable local user access
    "write_enable": "YES",  # Allow file uploads and modifications
    "local_umask": "022",  # File permission mask for local users
    "dirmessage_enable": "YES",  # Enable directory-specific messages
    "xferlog_enable": "YES",  # Enable transfer log
    "connect_from_port_20": "YES",  # Use port 20 for data connections
    "xferlog_file": "/var/log/vsftpd.log",  # Path to transfer log file
    "ftpd_banner": "Welcome to DX Link FTP Service!",  # Custom welcome message
    "chroot_local_user": "YES",  # Jail local users to their home directories
    "allow_writeable_chroot": "YES",  # Allow writable chroot (required for jailed users)
    "pasv_enable": "YES",  # Enable passive mode
    "pasv_min_port": "10000",  # Minimum port for passive mode
    "pasv_max_port": "10100",  # Maximum port for passive mode
    "ssl_enable": "YES",  # Enable SSL for secure connections
    "rsa_cert_file": "/etc/ssl/certs/vsftpd.pem",  # Path to SSL certificate
    "rsa_private_key_file": "/etc/ssl/private/vsftpd.key"  # Path to SSL private key
}

def generate_ftp_config_file(settings, file_path):
    """
    Generates an FTP server configuration file based on provided settings.

    :param settings: Dictionary containing FTP server settings.
    :param file_path: Path to save the configuration file.
    """
    try:
        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Write the settings to the configuration file
        with open(file_path, 'w') as config_file:
            for key, value in settings.items():
                config_file.write(f"{key}={value}\n")

        print(f"Configuration file generated successfully at {file_path}")

    except PermissionError:
        print(f"Permission denied: Unable to write to {file_path}. Try running as root.")
    except Exception as e:
        print(f"An error occurred while generating the configuration file: {e}")

if __name__ == "__main__":
    generate_ftp_config_file(FTP_SERVER_SETTINGS, CONFIG_FILE_PATH)
```

This script generates a production-ready FTP configuration file for vsftpd based on the given specifications, ensuring the code is clean, efficient, and well-documented.
