"""
Generated Code Metadata:
========================
Original URL: https://micropro.co.nz
Prompt: What are the typical steps to configure a domain's default page, and how does it relate to web server configuration?
Generated: DETERMINISTIC_614a1269b280aa97
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Domain Default Page Configuration

This script provides a basic guide on how to configure a domain's default page.
It also explains the relation to web server configuration.

Author: [Your Name]
Date: [Today's Date]
"""

import os

def configure_default_page(domain_name, web_server, document_root, default_page):
    """
    Configures a domain's default page.

    Args:
        domain_name (str): The domain name to configure.
        web_server (str): The web server software being used (e.g., Apache, Nginx).
        document_root (str): The document root directory of the web server.
        default_page (str): The default page to serve (e.g., index.html).

    Returns:
        None
    """

    try:
        # Check if the document root directory exists
        if not os.path.exists(document_root):
            raise FileNotFoundError(f"Document root directory '{document_root}' does not exist.")

        # Check if the default page exists in the document root
        default_page_path = os.path.join(document_root, default_page)
        if not os.path.exists(default_page_path):
            raise FileNotFoundError(f"Default page '{default_page_path}' does not exist.")

        # Configure the default page for Apache
        if web_server.lower() == "apache":
            # Create or modify the Apache configuration file
            apache_config_file = f"/etc/apache2/sites-available/{domain_name}.conf"
            with open(apache_config_file, "a") as f:
                f.write(f"<VirtualHost *:80>\n")
                f.write(f"    ServerName {domain_name}\n")
                f.write(f"    DocumentRoot {document_root}\n")
                f.write(f"    <Directory {document_root}>\n")
                f.write(f"        DirectoryIndex {default_page}\n")
                f.write(f"    </Directory>\n")
                f.write(f"</VirtualHost>\n")

            # Enable the Apache configuration
            os.system(f"a2ensite {domain_name}.conf")
            os.system("service apache2 restart")

        # Configure the default page for Nginx
        elif web_server.lower() == "nginx":
            # Create or modify the Nginx configuration file
            nginx_config_file = f"/etc/nginx/sites-available/{domain_name}"
            with open(nginx_config_file, "a") as f:
                f.write(f"server {{\n")
                f.write(f"    listen 80;\n")
                f.write(f"    server_name {domain_name};\n")
                f.write(f"    root {document_root};\n")
                f.write(f"    index {default_page};\n")
                f.write(f"}\n")

            # Create a symbolic link to the Nginx configuration file
            os.system(f"ln -s /etc/nginx/sites-available/{domain_name} /etc/nginx/sites-enabled/")
            os.system("service nginx restart")

        else:
            print(f"Unsupported web server: {web_server}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    domain_name = "example.com"
    web_server = "apache"
    document_root = "/var/www/html"
    default_page = "index.html"

    configure_default_page(domain_name, web_server, document_root, default_page)
```
