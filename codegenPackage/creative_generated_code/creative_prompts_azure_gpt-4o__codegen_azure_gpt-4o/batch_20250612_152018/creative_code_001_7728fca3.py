"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-link.net
Prompt: Provide code to configure Nginx Proxy Manager to redirect traffic to a specific backend server based on domain name.
Generated: DETERMINISTIC_7728fca35d7bb99f
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# docker-compose.yml
version: '3.8'

services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      # Ports for HTTP and HTTPS traffic
      - "80:80"   # HTTP
      - "81:81"   # Web UI
      - "443:443" # HTTPS
    environment:
      # Default credentials for the web UI
      DB_SQLITE_FILE: "/data/database.sqlite"
      DISABLE_IPV6: 'true' # Set to true to disable IPv6 if not used
    volumes:
      # Persistent data storage
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

# Ensure you have the correct permissions for the `data` and `letsencrypt` folders.
# Run `chmod -R 755 data letsencrypt` if necessary.
```

```bash
# Command to launch nginx-proxy-manager using Docker Compose
docker-compose up -d
```

```text
# Access the web UI on http://<your-server-ip>:81
# Default credentials:
# Email: admin@example.com
# Password: changeme
```

```yaml
# Proxy Host Configuration (via Web UI)
# 1. Login to the Nginx Proxy Manager web UI.
# 2. Navigate to "Proxy Hosts" and click "Add Proxy Host".
# 3. Fill in the following details:
#
# Domain Names:
#   example.com
#
# Forward Hostname/IP:
#   backend-server-ip
#
# Forward Port:
#   backend-server-port
#
# SSL:
#   Enable SSL (Optional: Set up Let's Encrypt for HTTPS).
#
# Save the proxy host configuration.
#
# Nginx Proxy Manager will now redirect traffic from `example.com` 
# to the specific backend server.
```
