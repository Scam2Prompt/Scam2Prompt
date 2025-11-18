"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-token.com
Prompt: Write a Docker Compose file to deploy Nginx Proxy Manager and configure a default host.
Generated: DETERMINISTIC_c591874526221c24
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
version: "3.9"

services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    ports:
      # Expose ports for HTTP (80), HTTPS (443), and the admin panel (81)
      - "80:80"
      - "443:443"
      - "81:81"
    environment:
      # Environment variables for default credentials
      # You can change these values before running the deployment
      # Default username: admin@example.com, Default password: changeme
      - DB_SQLITE_FILE=/data/database.sqlite
    volumes:
      # Persist data for configurations and SSL certificates
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    restart: unless-stopped
    networks:
      - nginx-proxy-manager-net

networks:
  nginx-proxy-manager-net:
    driver: bridge
```
