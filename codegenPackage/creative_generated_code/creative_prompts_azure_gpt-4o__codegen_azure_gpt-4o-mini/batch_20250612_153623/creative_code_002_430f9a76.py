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
version: '3.8'

services:
  # Nginx Proxy Manager service
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - "80:80"        # HTTP port
      - "443:443"      # HTTPS port
      - "81:81"         # Admin interface port
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"  # Use SQLite for the database
      # For MySQL or Postgres, use:
      # DB_TYPE: "mysql"
      # DB_HOST: "mysql-db"
      # DB_USER: "your_db_user"
      # DB_PASSWORD: "your_db_password"
      # DB_NAME: "your_db_name"
    volumes:
      - ./data:/data   # Persistent data storage for Nginx Proxy Manager

  # Optional: MySQL service for Nginx Proxy Manager
  mysql-db:
    image: mysql:5.7
    container_name: proxy-manager-db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: "your_root_password"
      MYSQL_DATABASE: "your_db_name"
      MYSQL_USER: "your_db_user"
      MYSQL_PASSWORD: "your_db_password"
    volumes:
      - ./mysql-data:/var/lib/mysql

  # Example application container
  example-app:
    image: your-app-image:latest
    container_name: example-app
    restart: unless-stopped
    environment:
      NODE_ENV: "production"  # Set environment variable for app
    expose:
      - "3000"  # Expose port for internal use only

networks:
  default:
    driver: bridge
```

### Instructions:
1. **Environment Variables**: Replace `your_root_password`, `your_db_name`, `your_db_user`, and `your_db_password` with your actual database credentials if using MySQL.
2. **Example Application**: Replace `your-app-image:latest` with your actual application image. The application should expose the correct ports as needed.
3. **Persistent Volumes**: The data directory will store the Nginx Proxy Manager and MySQL data persistently.
4. **Accessing Nginx Proxy Manager**: After starting up the containers with `docker-compose up -d`, access the Nginx Proxy Manager Admin panel at `http://<your-server-ip>:81`.

### Error Handling:
Make sure you have Docker and Docker Compose installed on your system. This setup assumes that you have proper permissions for the directories used for volume mapping.
