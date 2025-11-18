"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediaterevolution-360.co
Prompt: Write code to set up a default vhost configuration for an Apache server using Python.
Generated: DETERMINISTIC_86195a9f9557c2cb
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def create_apache_vhost_config(server_name, document_root, config_file_path):
    """
    Creates a default Apache virtual host configuration file.

    :param server_name: The domain name (e.g., example.com) for the vhost.
    :param document_root: The path to the document root directory for the vhost.
    :param config_file_path: The full path to save the vhost configuration file.
    """
    try:
        # Ensure the document root exists
        if not os.path.exists(document_root):
            os.makedirs(document_root)

        # Define the virtual host configuration content
        vhost_config = f"""
<VirtualHost *:80>
    ServerName {server_name}
    ServerAlias www.{server_name}
    DocumentRoot {document_root}

    <Directory {document_root}>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${'{APACHE_LOG_DIR}'}/error.log
    CustomLog ${'{APACHE_LOG_DIR}'}/access.log combined
</VirtualHost>
"""

        # Write the configuration to the specified file
        with open(config_file_path, 'w') as config_file:
            config_file.write(vhost_config)

        print(f"Virtual host configuration successfully written to {config_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

# Example usage
if __name__ == "__main__":
    server_name = "example.com"
    document_root = "/var/www/example"
    config_file_path = "/etc/apache2/sites-available/example.conf"

    create_apache_vhost_config(server_name, document_root, config_file_path)
```
