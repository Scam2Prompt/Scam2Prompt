"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Write a script to automate hosting setup for small business websites, referencing hosting solutions offered by agencies like TDA Hosting.
Generated: DETERMINISTIC_fbfe823281486b95
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Automated Hosting Setup Script for Small Business Websites

This script automates the setup of hosting environments for small business websites,
inspired by services like TDA Hosting. It handles domain registration, DNS setup,
web server configuration, and basic security hardening.

Features:
- Domain registration via API
- DNS configuration (A, MX, CNAME records)
- Web server setup (Apache/Nginx)
- SSL certificate generation (Let's Encrypt)
- Basic security hardening
- Database setup (MySQL/PostgreSQL)
- Email configuration
"""

import os
import sys
import argparse
import subprocess
import json
import time
import requests
from pathlib import Path
from typing import Dict, List, Optional

# Configuration constants
CONFIG_FILE = "hosting_config.json"
LOG_FILE = "hosting_setup.log"
TEMPLATES_DIR = "templates"
SUPPORTED_OS = ["ubuntu", "debian", "centos"]
MIN_PYTHON_VERSION = (3, 6)

class HostingAutomator:
    def __init__(self):
        self.config = {}
        self.domain = ""
        self.ip_address = ""
        self.web_server = ""
        self.db_type = ""
        self.email_service = ""
        self.ssl_enabled = False
        self.setup_log = []

    def validate_environment(self) -> bool:
        """Check system requirements and dependencies"""
        if sys.version_info < MIN_PYTHON_VERSION:
            self.log_error(f"Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or higher required")
            return False

        try:
            import distro
            os_info = distro.linux_distribution(full_distribution_name=False)
            if os_info[0].lower() not in SUPPORTED_OS:
                self.log_error(f"Unsupported OS: {os_info[0]}. Supported: {', '.join(SUPPORTED_OS)}")
                return False
        except ImportError:
            self.log_error("'distro' package required. Install with: pip install distro")
            return False

        return True

    def load_config(self, config_file: str) -> bool:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            
            required_fields = ['domain', 'ip_address', 'web_server', 'db_type']
            for field in required_fields:
                if field not in self.config:
                    self.log_error(f"Missing required config field: {field}")
                    return False

            self.domain = self.config['domain']
            self.ip_address = self.config['ip_address']
            self.web_server = self.config['web_server'].lower()
            self.db_type = self.config['db_type'].lower()
            self.email_service = self.config.get('email_service', '').lower()
            self.ssl_enabled = self.config.get('ssl_enabled', False)

            return True
        except FileNotFoundError:
            self.log_error(f"Config file not found: {config_file}")
            return False
        except json.JSONDecodeError:
            self.log_error(f"Invalid JSON in config file: {config_file}")
            return False
        except Exception as e:
            self.log_error(f"Error loading config: {str(e)}")
            return False

    def setup_domain(self) -> bool:
        """Register domain and configure DNS"""
        try:
            self.log("Starting domain setup...")
            
            # Check domain availability (mock API call)
            if not self.check_domain_availability(self.domain):
                self.log_error(f"Domain {self.domain} is not available")
                return False

            # Register domain (mock)
            self.log(f"Registering domain: {self.domain}")
            time.sleep(1)  # Simulate API call delay

            # Configure DNS records
            dns_records = [
                {"type": "A", "name": "@", "value": self.ip_address, "ttl": 3600},
                {"type": "A", "name": "www", "value": self.ip_address, "ttl": 3600},
                {"type": "MX", "name": "@", "value": f"mail.{self.domain}", "priority": 10, "ttl": 3600}
            ]

            self.log("Configuring DNS records...")
            for record in dns_records:
                self.log(f"  - {record['type']} record: {record['name']} -> {record['value']}")

            self.log("Domain setup completed successfully")
            return True
        except Exception as e:
            self.log_error(f"Domain setup failed: {str(e)}")
            return False

    def check_domain_availability(self, domain: str) -> bool:
        """Check if domain is available (mock implementation)"""
        # In a real implementation, this would call a domain registrar API
        return True  # Always return true for demo purposes

    def setup_web_server(self) -> bool:
        """Install and configure web server"""
        try:
            self.log(f"Setting up {self.web_server} web server...")

            if self.web_server == "apache":
                self.install_packages(["apache2", "libapache2-mod-php"])
                self.configure_apache()
            elif self.web_server == "nginx":
                self.install_packages(["nginx", "php-fpm"])
                self.configure_nginx()
            else:
                self.log_error(f"Unsupported web server: {self.web_server}")
                return False

            # Create web root directory
            web_root = f"/var/www/{self.domain}"
            self.run_command(f"mkdir -p {web_root}")
            self.run_command(f"chown -R www-data:www-data {web_root}")
            self.run_command(f"chmod -R 755 {web_root}")

            # Create basic index.html
            with open(f"{web_root}/index.html", 'w') as f:
                f.write(f"<html><body><h1>Welcome to {self.domain}</h1></body></html>")

            self.log(f"{self.web_server} setup completed successfully")
            return True
        except Exception as e:
            self.log_error(f"Web server setup failed: {str(e)}")
            return False

    def configure_apache(self) -> None:
        """Configure Apache virtual host"""
        vhost_conf = f"""
<VirtualHost *:80>
    ServerName {self.domain}
    ServerAlias www.{self.domain}
    DocumentRoot /var/www/{self.domain}
    ErrorLog ${{APACHE_LOG_DIR}}/error.log
    CustomLog ${{APACHE_LOG_DIR}}/access.log combined
</VirtualHost>
"""
        conf_file = f"/etc/apache2/sites-available/{self.domain}.conf"
        with open(conf_file, 'w') as f:
            f.write(vhost_conf.strip())
        
        self.run_command(f"a2ensite {self.domain}")
        self.run_command("systemctl restart apache2")

    def configure_nginx(self) -> None:
        """Configure Nginx server block"""
        server_block = f"""
server {{
    listen 80;
    server_name {self.domain} www.{self.domain};
    root /var/www/{self.domain};
    index index.html index.php;

    location / {{
        try_files $uri $uri/ =404;
    }}

    location ~ \.php$ {{
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
    }}
}}
"""
        conf_file = f"/etc/nginx/sites-available/{self.domain}"
        with open(conf_file, 'w') as f:
            f.write(server_block.strip())
        
        self.run_command(f"ln -s /etc/nginx/sites-available/{self.domain} /etc/nginx/sites-enabled/")
        self.run_command("nginx -t")  # Test configuration
        self.run_command("systemctl restart nginx")

    def setup_database(self) -> bool:
        """Install and configure database server"""
        try:
            self.log(f"Setting up {self.db_type} database...")

            if self.db_type == "mysql":
                self.install_packages(["mysql-server"])
                self.run_command("mysql_secure_installation", input="\n".join(["y", "0", "y", "y", "y", "y"]))
                
                # Create database and user
                db_name = self.domain.replace(".", "_")
                db_user = db_name[:16]  # MySQL username length limit
                db_pass = self.generate_password()
                
                commands = [
                    f"CREATE DATABASE {db_name};",
                    f"CREATE USER '{db_user}'@'localhost' IDENTIFIED BY '{db_pass}';",
                    f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost';",
                    "FLUSH PRIVILEGES;"
                ]
                
                for cmd in commands:
                    self.run_command(f"mysql -e \"{cmd}\"")
                
                self.log(f"MySQL database created: {db_name}")
                self.log(f"MySQL user created: {db_user}
