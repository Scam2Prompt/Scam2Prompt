"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-linktoken.com
Prompt: Provide an example of how to use Nginx Proxy Manager to set up SSL certificates for a domain.
Generated: DETERMINISTIC_a3115128898cd372
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Pull the Nginx Proxy Manager Docker image
docker pull jc21/nginx-proxy-manager:latest

# Step 2: Create a Docker network
docker network create nginx-proxy

# Step 3: Create a persistent volume for Nginx Proxy Manager data
docker volume create nginx-proxy-manager

# Step 4: Run the Nginx Proxy Manager container
docker run -d \
  --name nginx-proxy-manager \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  -p 81:81 \
  -v nginx-proxy-manager:/data \
  --network nginx-proxy \
  jc21/nginx-proxy-manager:latest

# Step 5: Access the Nginx Proxy Manager UI
# Open a web browser and go to http://<your-server-ip>:81
# Default credentials:
# Email: admin@example.com
# Password: changeme

# Step 6: Set Up SSL Certificates for a Domain
# - Navigate to the "SSL Certificates" section in the UI
# - Click on "Add SSL Certificate"
# - Choose "Let's Encrypt" as the SSL provider
# - Enter your domain name (e.g., example.com)
# - Make sure the "Force SSL" option is checked
# - Click "Save" to request and install the SSL certificate

# Step 7: Configure Proxy Host
# - Go to the "Proxy Hosts" section
# - Click on "Add Proxy Host"
# - Enter your domain name in the "Domain Names" field
# - Set the "Forward Hostname / IP" to your backend service address
# - Set the "Forward Port" to your backend service port (e.g., 3000)
# - Under "SSL", select the SSL certificate you just created
# - Click "Save" to create the proxy host

# Note: Ensure your domain's DNS is properly configured to point to your server's IP address.
```
