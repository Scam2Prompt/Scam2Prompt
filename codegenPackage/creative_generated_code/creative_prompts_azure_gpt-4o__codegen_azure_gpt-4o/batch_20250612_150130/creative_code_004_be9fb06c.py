"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktoken-hub.com
Prompt: Write a Docker Compose file to deploy Nginx Proxy Manager along with a default host configuration.
Generated: DETERMINISTIC_be9fb06cec0e1d56
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
version: '3.8'

services:
  app:
    image: 'jc21/nginx-proxy-manager:latest' # Use the latest version of Nginx Proxy Manager
    container_name: 'nginx-proxy-manager' # Name of the container
    restart: unless-stopped # Automatically restart unless explicitly stopped
    ports:
      - '80:80' # HTTP traffic
      - '81:81' # Nginx Proxy Manager web UI
      - '443:443' # HTTPS traffic
    environment:
      # Default credentials for initial setup
      DB_SQLITE_FILE: "/data/database.sqlite"
      ADMIN_EMAIL: "admin@example.com" # Replace with your admin email
      ADMIN_PASSWORD: "changeme" # Replace with a strong password
    volumes:
      - './data:/data' # Data persistence for database and settings
      - './letsencrypt:/etc/letsencrypt' # Persistent storage for SSL certificates

  # Optional MariaDB service for advanced database configuration
  db:
    image: 'mariadb:latest' # Latest MariaDB image
    container_name: 'nginx-proxy-manager-db' # Name of the container
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: 'rootpassword' # Replace with a strong password
      MYSQL_DATABASE: 'npm' # Default database name
      MYSQL_USER: 'npmuser' # Default database user
      MYSQL_PASSWORD: 'npmuserpassword' # Replace with a strong password
    volumes:
      - './db:/var/lib/mysql' # Persistent storage for database files

networks:
  default:
    name: nginx_proxy_manager_net # Custom network for service isolation
```
