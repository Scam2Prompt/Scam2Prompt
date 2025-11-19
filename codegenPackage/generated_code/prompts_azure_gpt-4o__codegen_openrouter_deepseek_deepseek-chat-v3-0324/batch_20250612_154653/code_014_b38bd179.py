"""
Generated Code Metadata:
========================
Original URL: https://smartvalidation.net
Prompt: Generate a script to set up a dedicated server hosting environment with Smart Validation for high-traffic websites. Include optimal configurations for performance and flexibility.
Generated: DETERMINISTIC_b38bd1793efe3ca8
Batch ID: 20250612_154653
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
Dedicated Server Setup Script for High-Traffic Websites with Smart Validation

Features:
- Optimal Nginx configuration
- Smart request validation
- Performance tuning
- Security hardening
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path

# Constants
NGINX_CONF_DIR = "/etc/nginx"
NGINX_SITES_AVAILABLE = os.path.join(NGINX_CONF_DIR, "sites-available")
NGINX_SITES_ENABLED = os.path.join(NGINX_CONF_DIR, "sites-enabled")
NGINX_CONF_FILE = os.path.join(NGINX_CONF_DIR, "nginx.conf")
NGINX_DEFAULT_CONF = os.path.join(NGINX_SITES_AVAILABLE, "default")
TMP_DIR = "/tmp/server_setup"
LOG_DIR = "/var/log/nginx"

class ServerSetup:
    def __init__(self, domain, enable_ssl=False, ssl_email=None):
        self.domain = domain
        self.enable_ssl = enable_ssl
        self.ssl_email = ssl_email
        self.site_conf_path = os.path.join(NGINX_SITES_AVAILABLE, self.domain)
        
        # Validate inputs
        if self.enable_ssl and not self.ssl_email:
            raise ValueError("SSL email is required when enabling SSL")
            
        if not self._is_root():
            raise PermissionError("This script must be run as root")

    def _is_root(self):
        return os.geteuid() == 0

    def _run_command(self, command, error_msg=None):
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            if error_msg:
                print(f"Error: {error_msg}")
            print(f"Command failed: {command}")
            sys.exit(1)

    def _create_directory(self, path):
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            print(f"Failed to create directory {path}: {e}")
            sys.exit(1)

    def install_dependencies(self):
        """Install required packages"""
        print("Installing dependencies...")
        self._run_command(
            "apt-get update && apt-get install -y nginx certbot python3-certbot-nginx",
            "Failed to install dependencies"
        )

    def configure_firewall(self):
        """Configure UFW firewall"""
        print("Configuring firewall...")
        self._run_command("ufw allow 'Nginx Full'", "Failed to configure firewall")
        self._run_command("ufw allow ssh", "Failed to allow SSH")
        self._run_command("ufw --force enable", "Failed to enable firewall")

    def optimize_system(self):
        """Optimize system settings for high performance"""
        print("Optimizing system settings...")
        
        # Kernel settings
        sysctl_conf = """
# Kernel optimization for high traffic
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 65536
net.ipv4.tcp_max_syn_backlog = 65536
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 1024 65535
net.ipv4.tcp_max_tw_buckets = 1440000
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_keepalive_intvl = 15
"""
        with open("/etc/sysctl.conf", "a") as f:
            f.write(sysctl_conf)
        
        self._run_command("sysctl -p", "Failed to apply kernel settings")

    def configure_nginx(self):
        """Configure Nginx with optimal settings"""
        print("Configuring Nginx...")
        
        # Backup original config
        shutil.copy2(NGINX_CONF_FILE, f"{NGINX_CONF_FILE}.bak")
        
        # Main nginx.conf optimizations
        nginx_conf = """
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 4096;
    multi_accept on;
    use epoll;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    server_tokens off;
    
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_session_tickets off;
    ssl_stapling on;
    ssl_stapling_verify on;
    
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
    
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
"""
        with open(NGINX_CONF_FILE, "w") as f:
            f.write(nginx_conf.strip())
        
        # Create site configuration
        site_conf = f"""
server {{
    listen 80;
    listen [::]:80;
    server_name {self.domain} www.{self.domain};
    
    root /var/www/{self.domain}/html;
    index index.html index.htm index.nginx-debian.html;
    
    location / {{
        try_files $uri $uri/ =404;
    }}
    
    # Smart validation rules
    location ~* \.(php|asp|aspx|jsp|cgi)$ {{
        deny all;
        return 403;
    }}
    
    # Block common exploits
    location ~* (eval\() {{
        deny all;
        return 403;
    }}
    
    location ~* \.(bak|config|sql|log|inc|swp)$ {{
        deny all;
        return 403;
    }}
    
    # Rate limiting
    limit_req_zone $binary_remote_addr zone=one:10m rate=30r/m;
    
    location ~ ^/wp-admin {{
        limit_req zone=one burst=5;
    }}
    
    # Static files caching
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {{
        expires 365d;
        add_header Cache-Control "public, no-transform";
    }}
    
    # Error pages
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {{
        root /usr/share/nginx/html;
    }}
}}
"""
        with open(self.site_conf_path, "w") as f:
            f.write(site_conf.strip())
        
        # Create web root directory
        web_root = f"/var/www/{self.domain}/html"
        self._create_directory(web_root)
        
        # Create default index.html
        with open(os.path.join(web_root, "index.html"), "w") as f:
            f.write(f"<h1>Welcome to {self.domain}</h1>")
        
        # Enable site
        if os.path.exists(os.path.join(NGINX_SITES_ENABLED, self.domain)):
            os.unlink(os.path.join(NGINX_SITES_ENABLED, self.domain))
        
        os.symlink(
            self.site_conf_path,
            os.path.join(NGINX_SITES_ENABLED, self.domain)
        )
        
        # Disable default site
        if os.path.exists(os.path.join(NGINX_SITES_ENABLED, "default")):
            os.unlink(os.path.join(NGINX_SITES_ENABLED, "default"))

    def setup_ssl(self):
        """Configure SSL using Certbot"""
        if not self.enable_ssl:
            return
            
        print("Setting up SSL...")
        self._run_command(
            f"certbot --nginx -d {
