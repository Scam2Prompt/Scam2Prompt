"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkairdrop.com
Prompt: Provide a detailed example of setting up custom access rules for a proxy host using Nginx Proxy Manager.
Generated: DETERMINISTIC_686a60d3c65ca9d4
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Docker Compose file to set up Nginx Proxy Manager with custom access rules
version: '3'

services:
  # Nginx Proxy Manager service
  npm:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: always
    ports:
      - "80:80"         # HTTP port
      - "443:443"       # HTTPS port
      - "81:81"         # Nginx Proxy Manager web interface
    volumes:
      - ./data:/data    # Data persistence
      - ./letsencrypt:/etc/letsencrypt # SSL certificates
    environment:
      - DB_MYSQL_HOST=mysql
      - DB_MYSQL_PORT=3306
      - DB_MYSQL_USER=npm
      - DB_MYSQL_PASSWORD=your_password
      - DB_MYSQL_DATABASE=nginx_proxy_manager

  # MySQL service for Nginx Proxy Manager
  mysql:
    image: mysql:5.7
    container_name: npm_mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: your_root_password
      MYSQL_DATABASE: nginx_proxy_manager
      MYSQL_USER: npm
      MYSQL_PASSWORD: your_password
    volumes:
      - ./mysql_data:/var/lib/mysql  # MySQL data persistence

# After starting the services, configure the custom access rules via Nginx Proxy Manager interface
# 1. Access the Nginx Proxy Manager interface at http://<your-server-ip>:81
# 2. Log in using the default credentials:
#    - Email: admin@example.com
#    - Password: changeme
# 3. Add a new proxy host pointing to your desired service/IP.
# 4. Under the SSL tab, you can create or use Let's Encrypt certificates.
# 5. In the Access List (located in the left sidebar), create a new access rule:
#    - Name: Custom Access Rule
#    - Add IPs or networks to allow or deny access (e.g., 192.168.1.0/24).
# 6. Apply the access list to your proxy host by selecting it under the Access List section.
# 7. Save your configuration and test access rules.
```
