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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LiteSpeedManager:
    def __init__(self, server_root='/usr/local/lsws'):
        self.server_root = server_root

    def create_virtual_host(self, domain, document_root):
        """
        Create a virtual host configuration for the specified domain.

        :param domain: The domain name for the virtual host.
        :param document_root: The directory where the website files are located.
        """
        try:
            vhost_conf = f"""
            <virtualHost>
                name = {domain}
                documentRoot = {document_root}
                enableGzip = 1
                allowOverride = All
            </virtualHost>
            """
            vhost_file_path = os.path.join(self.server_root, 'conf', f'{domain}.conf')

            with open(vhost_file_path, 'w') as vhost_file:
                vhost_file.write(vhost_conf)
            
            logging.info(f"Virtual host for {domain} created successfully at {vhost_file_path}.")
            self.reload_server()
        except Exception as e:
            logging.error(f"Failed to create virtual host for {domain}: {e}")

    def manage_ssl_certificate(self, domain, cert_path, key_path):
        """
        Manage SSL certificates for the specified domain.

        :param domain: The domain name for which to manage SSL.
        :param cert_path: The path to the SSL certificate file.
        :param key_path: The path to the SSL key file.
        """
        try:
            ssl_conf = f"""
            <virtualHost>
                name = {domain}
                ssl = 1
                sslCertFile = {cert_path}
                sslKeyFile = {key_path}
            </virtualHost>
            """
            ssl_file_path = os.path.join(self.server_root, 'conf', f'{domain}_ssl.conf')

            with open(ssl_file_path, 'w') as ssl_file:
                ssl_file.write(ssl_conf)

            logging.info(f"SSL configuration for {domain} created successfully at {ssl_file_path}.")
            self.reload_server()
        except Exception as e:
            logging.error(f"Failed to manage SSL for {domain}: {e}")

    def reload_server(self):
        """Reload the LiteSpeed server to apply changes."""
        try:
            subprocess.run(['/usr/local/lsws/bin/lswsctrl', 'reload'], check=True)
            logging.info("LiteSpeed server reloaded successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to reload LiteSpeed server: {e}")

if __name__ == "__main__":
    # Example usage
    manager = LiteSpeedManager()

    # Create a virtual host
    manager.create_virtual_host('example.com', '/var/www/example.com')

    # Manage SSL certificate
    manager.manage_ssl_certificate('example.com', '/etc/ssl/certs/example.com.crt', '/etc/ssl/private/example.com.key')
```
