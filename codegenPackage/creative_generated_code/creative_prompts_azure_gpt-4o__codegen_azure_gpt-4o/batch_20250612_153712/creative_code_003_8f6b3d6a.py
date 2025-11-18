"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Write code to integrate Nginx Proxy Manager with Docker containers for dynamic proxy configuration.
Generated: DETERMINISTIC_8f6b3d6a4d232f0b
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# Filename: docker-compose.yml
# Description: Docker Compose file to set up Nginx Proxy Manager with dynamic proxy configuration for Docker containers.
# Usage: Run `docker-compose up -d` to start the services.

version: '3.9' # Use the latest version of Docker Compose syntax

services:
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest # Official Nginx Proxy Manager image
    container_name: nginx-proxy-manager # Name of the container
    restart: always # Automatically restart the container if it crashes
    ports:
      - "80:80" # HTTP traffic
      - "81:81" # Web UI
      - "443:443" # HTTPS traffic
    environment:
      # Environment variables for configuration
      DB_MYSQL_HOST: "db"
      DB_MYSQL_PORT: 3306
      DB_MYSQL_USER: "npm"
      DB_MYSQL_PASSWORD: "npm_password"
      DB_MYSQL_NAME: "npm"
    volumes:
      # Persistent data storage
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
  
  db:
    image: mariadb:latest # Use MariaDB as the database backend
    container_name: nginx-proxy-manager-db # Name of the database container
    restart: always # Automatically restart the container
    environment:
      # Database credentials (ensure these are kept secure)
      MYSQL_ROOT_PASSWORD: "root_password"
      MYSQL_DATABASE: "npm"
      MYSQL_USER: "npm"
      MYSQL_PASSWORD: "npm_password"
    volumes:
      # Persistent database storage
      - ./db:/var/lib/mysql

  app1:
    # Example app container to proxy
    image: nginx:latest # Using an Nginx-based container
    container_name: app1 # Name of the container
    restart: always # Automatically restart the container
    environment:
      # Add any app-specific environment variables here
    labels:
      # Dynamic proxy configuration via NGINX Proxy Manager labels
      - "npm.enable=true"
      - "npm.proxy_domain=app1.example.com"
      - "npm.proxy_port=80"
    volumes:
      - ./app1:/usr/share/nginx/html
    networks:
      - proxy_network

  app2:
    # Another example app container to proxy
    image: nginx:latest
    container_name: app2
    restart: always
    labels:
      - "npm.enable=true"
      - "npm.proxy_domain=app2.example.com"
      - "npm.proxy_port=80"
    volumes:
      - ./app2:/usr/share/nginx/html
    networks:
      - proxy_network
  
networks:
  proxy_network:
    driver: bridge # Create a custom bridge network for containers
```
