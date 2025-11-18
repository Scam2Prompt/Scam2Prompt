"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-awards.com
Prompt: Generate code to integrate Nginx Proxy Manager with Docker containers for dynamic proxy management.
Generated: DETERMINISTIC_430f9a76762ecd71
Batch ID: 20250612_153623
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
  # Service for Nginx Proxy Manager
  nginx-proxy-manager:
    image: 'jc21/nginx-proxy-manager:latest' # Official Nginx Proxy Manager Image
    container_name: 'nginx-proxy-manager'
    restart: unless-stopped # Automatically restart unless manually stopped
    ports:
      - '80:80'         # Port for HTTP traffic
      - '443:443'       # Port for HTTPS traffic
      - '81:81'         # Port for Nginx Proxy Manager admin interface
    environment:
      # Set environment variables for initial login
      DB_SQLITE_FILE: '/data/database.sqlite' # SQLite database file location
      DISABLE_IPV6: 'true'                   # Disable IPv6 if not needed
    volumes:
      - './data:/data'   # Persistent data storage
      - './letsencrypt:/etc/letsencrypt' # Let's Encrypt SSL certificates
    network_mode: 'bridge' # Standard Docker network mode

  # Example application to be proxied
  example-app:
    image: 'nginx:alpine' # Example application using Nginx
    container_name: 'example-app'
    restart: unless-stopped
    environment:
      NODE_ENV: 'production' # Set environment variable for production
    volumes:
      - './example-app/html:/usr/share/nginx/html' # Mount static content
    networks:
      - proxy-network
    labels: # Labels for dynamic proxy generation
      - 'nginx_proxy_manager.enable=true'
      - 'nginx_proxy_manager.host=example.com'
      - 'nginx_proxy_manager.ssl=true'

networks:
  # Define a custom network for the proxy and proxied services
  proxy-network:
    driver: bridge
```
