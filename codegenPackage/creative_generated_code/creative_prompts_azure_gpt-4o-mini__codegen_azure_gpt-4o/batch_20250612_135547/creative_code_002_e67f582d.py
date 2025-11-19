"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-reward.com
Prompt: Can you provide a code snippet for setting up a reverse proxy using Nginx Proxy Manager?
Generated: DETERMINISTIC_e67f582d759d9d5f
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# docker-compose.yml

version: '3.9'
services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      # Port 80 for HTTP traffic
      - "80:80"
      # Port 443 for HTTPS traffic
      - "443:443"
      # Port 81 for Nginx Proxy Manager admin interface
      - "81:81"
    volumes:
      # Configuration files for Nginx Proxy Manager
      - ./data:/data
      # LetsEncrypt SSL certificates
      - ./letsencrypt:/etc/letsencrypt
    environment:
      # Default credentials for the admin interface (you should change them after setup)
      - DB_SQLITE=true
      - DISABLE_IPV6=true
```

```sh
# Commands to set up and run the proxy manager

# Step 1: Create the required directories for persistent storage
mkdir -p data letsencrypt

# Step 2: Launch the Nginx Proxy Manager container
docker-compose up -d

# Step 3: Access the admin interface at http://<your-server-ip>:81
# Default login credentials:
# Email: admin@example.com
# Password: changeme (update immediately after login!)
```

```txt
# Usage Example

# After logging into the admin interface:
# 1. Create a new proxy host for your web service.
# 2. Configure the domain name, upstream server (IP and port), and SSL settings.
# 3. Save and test the configuration to ensure proper functionality.
```
