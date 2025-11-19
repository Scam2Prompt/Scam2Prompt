"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-reward.com
Prompt: Can you provide a code snippet for setting up a reverse proxy using Nginx Proxy Manager?
Generated: DETERMINISTIC_e67f582d759d9d5f
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Update your package list
sudo apt update

# Step 2: Install Docker and Docker Compose if not already installed
sudo apt install -y docker.io docker-compose

# Step 3: Create a directory for Nginx Proxy Manager
mkdir ~/nginx-proxy-manager
cd ~/nginx-proxy-manager

# Step 4: Create a Docker Compose file
cat <<EOF > docker-compose.yml
version: '3'
services:
  app:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: always
    ports:
      - "80:80"      # HTTP Port
      - "443:443"    # HTTPS Port
      - "81:81"      # Admin Web Interface
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
EOF

# Step 5: Start Nginx Proxy Manager
sudo docker-compose up -d

# Step 6: Access the Nginx Proxy Manager Admin Interface
echo "Nginx Proxy Manager is running. Access it at http://<your-server-ip>:81"
echo "Default login is admin@example.com / changeme"
```

### Notes:
- Replace `<your-server-ip>` with your actual server's IP address.
- Ensure that your firewall allows traffic on ports 80, 443, and 81.
- Change the default credentials after the first login for security.
