"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-token.com
Prompt: Provide an example of how to set up a reverse proxy for a web application using Nginx Proxy Manager, including custom domain routing.
Generated: DETERMINISTIC_ffbd088d49c4afe1
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# docker-compose.yml
# This file sets up Nginx Proxy Manager to act as a reverse proxy for a web application.
# It includes support for routing custom domains.

version: '3.8'

services:
  # Nginx Proxy Manager service
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      # Default ports for Nginx Proxy Manager
      - 80:80    # HTTP
      - 81:81    # Nginx Proxy Manager dashboard
      - 443:443  # HTTPS
    volumes:
      # Persistent storage for configuration and data
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    environment:
      # Environment variables to set up the NPM
      # Default admin credentials
      DB_SQLITE_FILE: "/data/database.sqlite"
      DISABLE_IPV6: "true" # Disable IPv6 if not needed

  # Example web application service
  web-app:
    image: nginx:alpine
    container_name: web-app
    restart: unless-stopped
    ports:
      # Make the web app available internally (but not publicly exposed)
      - 8080:80
    volumes:
      # Serve static content (optional)
      - ./web-app:/usr/share/nginx/html
    environment:
      # Add app-specific environment variables here if needed
      - NGINX_PORT=80
```

```plaintext
# After deploying the above Docker Compose setup:
# 1. Access Nginx Proxy Manager dashboard at http://<server-ip>:81
# 2. Log in using default credentials (admin@example.com / changeme).
# 3. Navigate to "Proxy Hosts" and click "Add Proxy Host."
#    - Set the custom domain (e.g., app.example.com).
#    - Forward Hostname/IP: web-app
#    - Forward Port: 80
# 4. Enable HTTPS by requesting an SSL certificate (optional).
```
