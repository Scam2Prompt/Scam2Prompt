"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkbonus.net
Prompt: Explain how to use Nginx Proxy Manager to redirect HTTP traffic to HTTPS with code examples.
Generated: DETERMINISTIC_920990bd93dd4e28
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# This script assumes you have Docker and Docker Compose installed.

# Create a directory for the Nginx Proxy Manager configuration
mkdir -p ~/nginx-proxy-manager && cd ~/nginx-proxy-manager

# Create a docker-compose.yml file for Nginx Proxy Manager
cat <<EOL > docker-compose.yml
version: '3'

services:
  npm:
    image: jc21/nginx-proxy-manager:latest
    restart: always
    ports:
      - "80:80"      # HTTP port
      - "443:443"    # HTTPS port
      - "81:81"      # Admin interface
    volumes:
      - npm_data:/data
      - npm_letsencrypt:/etc/letsencrypt
    environment:
      DB_SQLITE_FILE: "/data/database.sqlite"

volumes:
  npm_data:
  npm_letsencrypt:
EOL

# Start the Nginx Proxy Manager
docker-compose up -d

# Instructions to access Nginx Proxy Manager
echo "Nginx Proxy Manager is now running."
echo "Access the admin interface at: http://<your-server-ip>:81"
echo "Default login credentials are:"
echo "Email: admin@example.com"
echo "Password: changeme"

# Wait for the Nginx Proxy Manager to initialize
sleep 30

# Use the Nginx Proxy Manager interface to set up redirection:
# 1. Log in to the admin interface.
# 2. Navigate to the 'Proxy Hosts' section.
# 3. Click 'Add Proxy Host'.
# 4. Enter the domain you want to redirect from (e.g., example.com).
# 5. Set the destination IP and port of your service (e.g., 192.168.1.100:80).
# 6. Check the 'Block Common Exploits' option.
# 7. Enable 'SSL' and choose 'Force SSL' to redirect HTTP to HTTPS.
# 8. Optionally, set up your Let's Encrypt certificate.
# 9. Save your settings.

# Note: Ensure that your DNS records for the domain point to your server's IP address.
```
