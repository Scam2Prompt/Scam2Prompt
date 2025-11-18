"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-link.net
Prompt: Write a Docker Compose file to deploy Nginx Proxy Manager with custom settings for proxy hosts.
Generated: DETERMINISTIC_d306ec04e8b4a282
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
version: '3.9'

services:
  # Service for Nginx Proxy Manager
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      # Expose ports for HTTP and HTTPS traffic
      - 80:80   # HTTP
      - 443:443 # HTTPS
      # Expose management interface
      - 81:81   # Admin UI
    environment:
      # Set custom credentials for accessing the admin UI
      # Default credentials are admin@example.com / changeme
      # Change these values in production
      ADMIN_EMAIL: "customadmin@example.com"
      ADMIN_PASSWORD: "securepassword123"
    volumes:
      # Persist data across container restarts
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

  # Optional: Define additional services or proxy hosts here if needed
  # Example: A backend service to be proxied
  # backend-app:
  #   image: my-backend-app:latest
  #   container_name: backend-app
  #   restart: unless-stopped
  #   ports:
  #     - 3000:3000
```
