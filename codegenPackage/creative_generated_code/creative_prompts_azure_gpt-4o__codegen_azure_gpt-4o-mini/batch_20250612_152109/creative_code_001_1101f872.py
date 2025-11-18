"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-bounty.com
Prompt: Provide an example of how to set up a reverse proxy for a web application using Nginx Proxy Manager.
Generated: DETERMINISTIC_1101f872352e9cd5
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Nginx Proxy Manager Configuration
version: '3'

services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - "80:80"    # HTTP port
      - "443:443"  # HTTPS port
      - "8181:8181" # Admin interface
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"
      # You can set a password for the admin interface
      NODE_ENV: "production"
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - nginx-proxy

networks:
  nginx-proxy:
    driver: bridge

# Note: To access the Nginx Proxy Manager web interface,
# navigate to http://<your-server-ip>:8181 and log in with default credentials:
# Email: admin@example.com
# Password: changeme

# After accessing the interface:
# 1. Create a new host.
# 2. Enter the domain name for your web application.
# 3. Set the Forward Hostname/IP to the internal IP of your web app.
# 4. Set the Forward Port to the port your web application is running on (e.g., 80 or 443).
# 5. Configure SSL as desired (you can use Let's Encrypt for SSL certificates).
```
