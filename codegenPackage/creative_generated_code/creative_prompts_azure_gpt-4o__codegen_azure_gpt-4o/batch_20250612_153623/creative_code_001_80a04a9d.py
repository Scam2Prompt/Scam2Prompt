"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-awards.com
Prompt: Provide an example of configuring Nginx Proxy Manager to manage multiple proxies for different domains.
Generated: DETERMINISTIC_80a04a9dba582a4c
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a sample configuration file for Nginx Proxy Manager to manage multiple proxies for different domains. The configuration is stored in the `docker-compose.yml` file for deploying Nginx Proxy Manager with Docker:

```yaml
version: '3.8'

services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: 'nginx-proxy-manager'
    restart: always
    ports:
      # HTTP and HTTPS ports exposed
      - '80:80'
      - '81:81'
      - '443:443'
    environment:
      # Connection to database
      - DB_MYSQL_HOST=db
      - DB_MYSQL_PORT=3306
      - DB_MYSQL_USER=nginxproxy
      - DB_MYSQL_PASSWORD=nginxproxy_password
      - DB_MYSQL_NAME=nginxproxy_db
    volumes:
      # Persistent volumes for configuration and data
      - './data:/data'
      - './letsencrypt:/etc/letsencrypt'

  db:
    image: 'mysql:5.7'
    container_name: 'nginx-proxy-manager-db'
    restart: always
    environment:
      # Set MySQL credentials
      - MYSQL_ROOT_PASSWORD=root_password
      - MYSQL_DATABASE=nginxproxy_db
      - MYSQL_USER=nginxproxy
      - MYSQL_PASSWORD=nginxproxy_password
    volumes:
      # Persistent storage for database
      - './mysql:/var/lib/mysql'

networks:
  default:
    name: nginx-proxy-network
```

Once the containers are running, access the Nginx Proxy Manager GUI via `http://<your-server-ip>:81`. You can manage multiple proxies for different domains directly from the dashboard.
