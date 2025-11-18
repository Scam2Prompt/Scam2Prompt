"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-linktoken.com
Prompt: Write code to configure a reverse proxy using Nginx Proxy Manager for a host that isn't set up yet. Include steps to access the Admin panel and initialize the setup.
Generated: DETERMINISTIC_6f96844ff395036b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script will help you set up Nginx Proxy Manager on a new host
# Make sure to run this script with root privileges or using sudo

# Update the package index
apt-get update -y

# Install required packages
apt-get install -y docker.io docker-compose

# Start and enable Docker service
systemctl start docker
systemctl enable docker

# Create a directory for Nginx Proxy Manager
mkdir -p /srv/nginx-proxy-manager

# Change to the Nginx Proxy Manager directory
cd /srv/nginx-proxy-manager

# Create a Docker Compose file
cat <<EOF > docker-compose.yml
version: '3'

services:
  npm:
    image: jc21/nginx-proxy-manager:latest
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
      - "81:81"  # Admin panel
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"
EOF

# Deploy Nginx Proxy Manager using Docker Compose
docker-compose up -d

# Wait for the services to start
echo "Waiting for Nginx Proxy Manager to start..."
sleep 10

# Display the access information for the Admin panel
echo "Nginx Proxy Manager is running!"
echo "Access the Admin panel at http://<your-server-ip>:81"
echo "Default credentials are:"
echo "Email: admin@example.com"
echo "Password: changeme"

# End of script
``` 

Make sure to replace `<your-server-ip>` with the actual IP address of your server when accessing the Admin panel for the first time. After logging in, it's recommended to change the default credentials.
