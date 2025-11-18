"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-bounty.com
Prompt: Create a step-by-step guide for deploying Nginx Proxy Manager in a Docker environment.
Generated: DETERMINISTIC_16b48c8ea40a4ce4
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Create a Docker network for Nginx Proxy Manager
docker network create nginx-proxy

# Step 2: Create a directory for Nginx Proxy Manager configuration
mkdir -p ~/nginx-proxy-manager/data

# Step 3: Create a Docker Compose file (docker-compose.yml) with the necessary configuration
cat <<EOF > ~/nginx-proxy-manager/docker-compose.yml
version: '3'

services:
  app:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    environment:
      - DB_MYSQL_HOST=db
      - DB_MYSQL_PORT=3306
      - DB_MYSQL_USER=npm
      - DB_MYSQL_PASSWORD=example_password
      - DB_MYSQL_NAME=npm
      - APP_PORT=81
      - APP_SSL_PORT=443
      - APP_HTTP_PORT=80
    volumes:
      - ./data:/data
    ports:
      - "80:80"
      - "443:443"
      - "81:81"
    restart: always
    networks:
      - nginx-proxy

  db:
    image: mysql:5.7
    container_name: nginx-proxy-manager-db
    environment:
      - MYSQL_ROOT_PASSWORD=root_password
      - MYSQL_DATABASE=npm
      - MYSQL_USER=npm
      - MYSQL_PASSWORD=example_password
    volumes:
      - ./data/mysql:/var/lib/mysql
    restart: always
    networks:
      - nginx-proxy

networks:
  nginx-proxy:
    external: true
EOF

# Step 4: Change directory to the Nginx Proxy Manager folder
cd ~/nginx-proxy-manager

# Step 5: Start the Docker containers with Docker Compose
docker-compose up -d

# Step 6: Verify that the containers are running
docker ps

# Step 7: Access Nginx Proxy Manager
# Open a web browser and navigate to http://<your-server-ip>:81
# Default login credentials:
# Email: admin@example.com
# Password: changeme

# Step 8: Clean up resources (if needed)
# To stop and remove containers, use:
# docker-compose down

# Note: For production environments, configure SSL certificates and secure your database.
```
