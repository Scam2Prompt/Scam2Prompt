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
version: '3.8'  # Specify the version of Docker Compose

services:
  # Define the Nginx Proxy Manager service
  npm:
    image: jc21/nginx-proxy-manager:latest  # Use the latest version of Nginx Proxy Manager
    container_name: nginx-proxy-manager  # Name of the container
    restart: unless-stopped  # Restart policy
    ports:
      - "80:80"  # Expose port 80 for HTTP traffic
      - "443:443"  # Expose port 443 for HTTPS traffic
      - "81:81"  # Expose port 81 for the Admin panel
    volumes:
      - npm_data:/data  # Mount a volume for persistent data storage
      - npm_letsencrypt:/etc/letsencrypt  # Mount a volume for Let's Encrypt certificates
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"  # SQLite database file location
      # Uncomment the following lines for MySQL support
      # DB_TYPE: "mysql"  # Uncomment for MySQL database type
      # DB_HOST: "mysql"  # Uncomment and set MySQL service name
      # DB_PORT: "3306"  # Uncomment and set MySQL port
      # DB_USER: "npm"  # Uncomment and set MySQL user
      # DB_PASSWORD: "your_mysql_password"  # Uncomment and set MySQL password
      # DB_DATABASE: "npm"  # Uncomment and set MySQL database name

  # Uncomment and configure this service if using MySQL
  # mysql:
  #   image: mysql:5.7  # Use MySQL 5.7 version
  #   container_name: npm_mysql
  #   restart: unless-stopped
  #   environment:
  #     MYSQL_ROOT_PASSWORD: "your_root_password"  # Set MySQL root password
  #     MYSQL_DATABASE: "npm"  # Create the npm database
  #     MYSQL_USER: "npm"  # MySQL user for Nginx Proxy Manager
  #     MYSQL_PASSWORD: "your_mysql_password"  # MySQL user password
  #   volumes:
  #     - mysql_data:/var/lib/mysql  # Mount a volume for MySQL data

# Define named volumes for persistent storage
volumes:
  npm_data:  # Volume for Nginx Proxy Manager data
  npm_letsencrypt:  # Volume for Let's Encrypt certificates
  # mysql_data:  # Uncomment for MySQL data volume

```

# Accessing the Admin Panel for Initial Configuration
1. Run the Docker Compose file by navigating to the directory containing the `docker-compose.yml` file and executing the following command:
   ```bash
   docker-compose up -d
   ```

2. Once the services are running, access the Admin panel by opening a web browser and navigating to:
   ```
   http://<YOUR_SERVER_IP>:81
   ```
   Replace `<YOUR_SERVER_IP>` with the IP address of your server.

3. The default login credentials for the Admin panel are:
   - **Email:** `admin@example.com`
   - **Password:** `changeme`

4. After logging in, it is highly recommended to change the default credentials for security purposes.
