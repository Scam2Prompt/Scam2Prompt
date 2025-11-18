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
# Step 1: Create a directory for the deployment
mkdir nginx-proxy-manager
cd nginx-proxy-manager

# Step 2: Create a Docker Compose file
cat <<EOF >docker-compose.yml
version: "3.8"

services:
  app:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager-app
    restart: always
    ports:
      - 80:80        # HTTP
      - 81:81        # Admin Panel
      - 443:443      # HTTPS
    environment:
      # Default credentials: admin@example.com / changeme
      MYSQL_HOST: "db"
      MYSQL_PORT: 3306
      MYSQL_USER: "npm"
      MYSQL_PASSWORD: "npm_password"
      MYSQL_DATABASE: "npm"
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt

  db:
    image: mysql:5.7
    container_name: nginx-proxy-manager-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: "root_password"
      MYSQL_DATABASE: "npm"
      MYSQL_USER: "npm"
      MYSQL_PASSWORD: "npm_password"
    volumes:
      - ./mysql:/var/lib/mysql
EOF

# Step 3: Create directories for persistent data
mkdir data letsencrypt mysql

# Step 4: Start the Docker containers
docker-compose up -d

# Step 5: Check the logs to ensure everything is running properly
docker-compose logs -f

# Step 6: Access Nginx Proxy Manager
# Open a browser and navigate to http://<server-ip>:81
# Default login credentials: admin@example.com / changeme

# Step 7: Optional - Secure the default credentials by logging in and updating them.
```
