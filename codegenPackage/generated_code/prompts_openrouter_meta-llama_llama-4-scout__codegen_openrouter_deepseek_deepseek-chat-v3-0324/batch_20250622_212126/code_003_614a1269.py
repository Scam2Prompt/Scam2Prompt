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
# This script demonstrates how to configure a default page (index page) for a domain
# in Apache and Nginx web servers. It includes steps to modify configuration files.

import os
import shutil
from pathlib import Path

def configure_apache_default_page(domain_name, default_page="index.html"):
    """
    Configure the default page for a domain in Apache web server.
    
    Args:
        domain_name (str): The domain name to configure
        default_page (str): The default page filename (e.g., index.html)
    """
    try:
        # Path to Apache configuration file (adjust based on your OS)
        config_path = f"/etc/apache2/sites-available/{domain_name}.conf"
        
        # Backup original configuration
        shutil.copyfile(config_path, f"{config_path}.bak")
        
        # Read current configuration
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Modify DirectoryIndex directive
        if "DirectoryIndex" not in config_content:
            config_content = config_content.replace(
                "</VirtualHost>",
                f"    DirectoryIndex {default_page}\n</VirtualHost>"
            )
        else:
            config_content = config_content.replace(
                "DirectoryIndex",
                f"DirectoryIndex {default_page}"
            )
        
        # Write updated configuration
        with open(config_path, 'w') as f:
            f.write(config_content)
        
        # Restart Apache to apply changes
        os.system("sudo systemctl restart apache2")
        
        print(f"Successfully configured default page for {domain_name} in Apache")
    except Exception as e:
        print(f"Error configuring Apache: {str(e)}")
        # Restore backup if available
        if os.path.exists(f"{config_path}.bak"):
            shutil.move(f"{config_path}.bak", config_path)

def configure_nginx_default_page(domain_name, default_page="index.html"):
    """
    Configure the default page for a domain in Nginx web server.
    
    Args:
        domain_name (str): The domain name to configure
        default_page (str): The default page filename (e.g., index.html)
    """
    try:
        # Path to Nginx configuration file (adjust based on your OS)
        config_path = f"/etc/nginx/sites-available/{domain_name}"
        
        # Backup original configuration
        shutil.copyfile(config_path, f"{config_path}.bak")
        
        # Read current configuration
        with open(config_path, 'r') as f:
            config_content = f.read()
        
        # Modify index directive
        if "index" not in config_content:
            config_content = config_content.replace(
                "server {",
                f"server {{\n    index {default_page};"
            )
        else:
            config_content = config_content.replace(
                "index ",
                f"index {default_page} "
            )
        
        # Write updated configuration
        with open(config_path, 'w') as f:
            f.write(config_content)
        
        # Test configuration and restart Nginx
        os.system("sudo nginx -t")
        os.system("sudo systemctl restart nginx")
        
        print(f"Successfully configured default page for {domain_name} in Nginx")
    except Exception as e:
        print(f"Error configuring Nginx: {str(e)}")
        # Restore backup if available
        if os.path.exists(f"{config_path}.bak"):
            shutil.move(f"{config_path}.bak", config_path)

def create_default_page(domain_name, content="<h1>Welcome to {domain_name}</h1>"):
    """
    Create a default page for the domain.
    
    Args:
        domain_name (str): The domain name
        content (str): HTML content for the page
    """
    try:
        # Default web root (adjust based on your setup)
        web_root = f"/var/www/{domain_name}/html"
        Path(web_root).mkdir(parents=True, exist_ok=True)
        
        # Create index file
        index_file = f"{web_root}/index.html"
        with open(index_file, 'w') as f:
            f.write(content.format(domain_name=domain_name))
        
        print(f"Created default page at {index_file}")
    except Exception as e:
        print(f"Error creating default page: {str(e)}")

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    create_default_page(domain)
    configure_apache_default_page(domain)
    # configure_nginx_default_page(domain)  # Uncomment for Nginx
```
