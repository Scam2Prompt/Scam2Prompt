"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Provide an example of setting up a reverse proxy for a web application using Nginx Proxy Manager.
Generated: DETERMINISTIC_be4e176d71d1b52f
Batch ID: 20250612_154420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://web_app_backend_ip_or_hostname;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```yaml
# docker-compose.yml
# This file sets up Nginx Proxy Manager using Docker for reverse proxying a web application.

version: '3.8'

services:
  nginx-proxy-manager:
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      # Ports exposed for Nginx Proxy Manager
      - '80:80'    # HTTP traffic
      - '443:443'  # HTTPS traffic
      - '81:81'    # Admin interface
    environment:
      # Set environment variables for Nginx Proxy Manager
      DB_MYSQL_HOST: "db"
      DB_MYSQL_PORT: 3306
      DB_MYSQL_USER: "npm"
      DB_MYSQL_PASSWORD: "change_this_password"
      DB_MYSQL_NAME: "npm"
    volumes:
      # Persist configuration data
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

  db:
    image: 'mysql:5.7'
    container_name: nginx-proxy-manager-db
    restart: unless-stopped
    environment:
      # Configure MySQL database for Nginx Proxy Manager
      MYSQL_ROOT_PASSWORD: "change_this_password"
      MYSQL_DATABASE: "npm"
      MYSQL_USER: "npm"
      MYSQL_PASSWORD: "change_this_password"
    volumes:
      # Persist database data
      - ./mysql:/var/lib/mysql
```

```nginx
# Example configuration added through the Nginx Proxy Manager web UI
# Reverse proxy configuration for a web application.

server {
  listen 80;
  server_name example.com;

  # Proxy settings
  location / {
    proxy_pass http://web_app_backend_ip_or_hostname;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

    # Optional: Enable WebSocket support
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    # Add error handling
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
      root /usr/share/nginx/html;
    }
  }
}
```
