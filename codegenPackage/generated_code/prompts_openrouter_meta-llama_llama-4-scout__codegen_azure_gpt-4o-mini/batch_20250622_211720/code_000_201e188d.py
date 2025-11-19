"""
Generated Code Metadata:
========================
Original URL: https://linkbonus.net
Prompt: Write a basic configuration for Nginx Proxy Manager to proxy requests to a local server.
Generated: DETERMINISTIC_201e188d0542b312
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# Nginx Proxy Manager Configuration
# This configuration sets up a basic reverse proxy to forward requests to a local server.

version: '3'

services:
  # Nginx Proxy Manager service
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - "80:80"        # HTTP port
      - "443:443"      # HTTPS port
      - "81:81"        # Admin interface port
    environment:
      # Set the database URL for Nginx Proxy Manager
      DB_SQLITE_FILE: "/data/database.sqlite"
      # Set the email for Let's Encrypt notifications
      DEFAULT_EMAIL: "admin@example.com"
      # Set the default password for the admin interface
      DEFAULT_PASSWORD: "your_secure_password"
    volumes:
      - ./data:/data   # Persistent storage for Nginx Proxy Manager data
      - ./letsencrypt:/etc/letsencrypt  # Persistent storage for SSL certificates

  # Local server service (example)
  local-server:
    image: your-local-server-image:latest
    container_name: local-server
    restart: unless-stopped
    ports:
      - "3000:3000"    # Expose local server on port 3000
    environment:
      # Add any necessary environment variables for your local server
      NODE_ENV: "production"
    volumes:
      - ./local-server-data:/app/data  # Persistent storage for local server data

# Note: After starting the Nginx Proxy Manager, you can access the admin interface at http://<your-server-ip>:81
# You can then set up a proxy host to forward requests to your local server.
# Make sure to replace 'your-local-server-image:latest' with the actual image of your local server.
# Also, update the email and password in the environment variables for security.
```
