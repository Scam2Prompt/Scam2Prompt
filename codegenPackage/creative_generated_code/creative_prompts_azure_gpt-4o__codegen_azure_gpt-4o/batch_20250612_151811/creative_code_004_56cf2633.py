"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-linktoken.com
Prompt: Write a Docker Compose file to deploy Nginx Proxy Manager and explain how to access the Admin panel for initial configuration.
Generated: DETERMINISTIC_56cf2633af6d16ce
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
version: '3.9' # Specify the Docker Compose file version

services:
  app:
    image: jc21/nginx-proxy-manager:latest # Use the latest Nginx Proxy Manager image
    container_name: nginx-proxy-manager # Name the container for easy identification
    restart: unless-stopped # Ensure the container restarts automatically unless explicitly stopped
    ports:
      - "80:80"   # Port mapping for HTTP traffic
      - "81:81"   # Port mapping for the Admin Panel
      - "443:443" # Port mapping for HTTPS traffic
    environment:
      # Environment variables for default credentials
      DB_SQLITE_FILE: "/data/database.sqlite"
    volumes:
      # Persistent storage for configuration and data
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

  db:
    image: jc21/mariadb:latest # Use the MariaDB image as the database backend
    container_name: nginx-proxy-manager-db # Name the database container
    restart: unless-stopped # Ensure the container restarts automatically unless explicitly stopped
    environment:
      # Database credentials - replace with your own secure values
      MYSQL_ROOT_PASSWORD: "rootpassword"
      MYSQL_DATABASE: "npm"
      MYSQL_USER: "npm"
      MYSQL_PASSWORD: "npmuserpassword"
    volumes:
      # Persistent storage for the database
      - ./data/mysql:/var/lib/mysql

# Notes:
# 1. Replace `rootpassword` and `npmuserpassword` with secure passwords.
# 2. Ensure `./data` and `./letsencrypt` directories exist locally for persistent storage.

# How to access the Admin panel for initial configuration:
# 1. Run `docker-compose up -d` to start the services.
# 2. Access the Admin panel at http://<your-server-ip>:81.
# 3. Default credentials:
#    Email: `admin@example.com`
#    Password: `changeme`
#    Update credentials after login for security.
```
