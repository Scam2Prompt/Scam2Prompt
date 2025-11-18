"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-reward.com
Prompt: Write a configuration file for Nginx Proxy Manager that sets up a reverse proxy for multiple subdomains with SSL support.
Generated: DETERMINISTIC_f3a2471e02abb5b6
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Configuration file for Nginx Proxy Manager
# Sets up reverse proxy with SSL support for multiple subdomains

version: '3.8'  # Specify Docker Compose version

services:
  # Nginx Proxy Manager service
  nginx-proxy-manager:
    image: 'jc21/nginx-proxy-manager:latest'  # Official Nginx Proxy Manager image
    container_name: 'nginx-proxy-manager'    # Name of the container
    restart: always                          # Automatically restart the container if it stops
    ports:
      - '80:80'    # Expose HTTP port
      - '443:443'  # Expose HTTPS port
      - '81:81'    # Expose Admin UI port
    environment:
      # Environment variables for initial setup
      DB_SQLITE_FILE: "/data/database.sqlite"  # Path for SQLite DB file
    volumes:
      - './data:/data'    # Persist application data
      - './letsencrypt:/etc/letsencrypt'  # Directory for SSL certificates
    networks:
      - proxy-network     # Attach container to the proxy network

networks:
  proxy-network:
    driver: bridge  # Use bridge network for isolated communication

# Example of how to configure reverse proxy in Nginx Proxy Manager:
# 1. Access the Admin UI at http://<server_ip>:81
# 2. Add each subdomain, pointing it to the internal service's IP/port
# 3. Enable SSL for each subdomain via Let's Encrypt certificate requests
```
