"""
Generated Code Metadata:
========================
Original URL: https://link-reward.com
Prompt: Write a troubleshooting guide for resolving issues when the Nginx Proxy Manager default site is displayed instead of the configured host.
Generated: DETERMINISTIC_f934fca08d6c0ce5
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nginx
# Nginx Proxy Manager Troubleshooting Guide

# 1. Check Nginx Proxy Manager Configuration
# Verify the proxy host is properly configured in Nginx Proxy Manager
# - Log in to the Nginx Proxy Manager web interface
# - Navigate to "Hosts" > "Proxy Hosts"
# - Ensure your domain is listed with correct:
#   - Domain names
#   - Forwarding scheme (http/https)
#   - Forwarding hostname/IP
#   - Forwarding port

# 2. Verify Nginx Configuration Files
# Check the generated nginx configuration files
# Location: /data/nginx/proxy_host/

# Example command to list proxy host configurations:
ls -la /data/nginx/proxy_host/

# Check a specific configuration file
cat /data/nginx/proxy_host/[your-domain].conf

# Expected content should include your domain and proper proxy_pass directive

# 3. Check for Default Server Conflict
# The default site appears when no other server_name matches
# Verify no conflicting default_server directives

grep -r "default_server" /etc/nginx/

# 4. Check DNS Configuration
# Verify DNS records point to your server's IP
dig +short yourdomain.com
nslookup yourdomain.com

# 5. Check SSL Certificate
# If using HTTPS, verify certificate is properly issued
# Location: /data/letsencrypt/live/[your-domain]/

ls -la /data/letsencrypt/live/[your-domain]/

# 6. Test Nginx Configuration
# Before reloading, test the configuration
nginx -t

# 7. Restart Nginx Services
# Restart Nginx Proxy Manager and Nginx itself
docker-compose -f /path/to/your/docker-compose.yml down
docker-compose -f /path/to/your/docker-compose.yml up -d

# Or if using systemd
systemctl restart nginx

# 8. Check Nginx Logs
# Examine error logs for clues
tail -f /var/log/nginx/error.log
docker logs nginxproxymanager_app_1

# 9. Verify Port Binding
# Check that Nginx is listening on ports 80 and 443
netstat -tulnp | grep nginx
ss -tulnp | grep nginx

# 10. Check Hosts File (Local Testing)
# For local testing, ensure hosts file has correct entry
# /etc/hosts (Linux/macOS) or C:\Windows\System32\drivers\etc\hosts (Windows)
127.0.0.1 yourdomain.com

# 11. Clear Browser Cache
# Sometimes browser cache can cause issues
# Try accessing in incognito mode or clear cache

# 12. Check Firewall Rules
# Ensure ports 80 and 443 are open
ufw status
iptables -L

# 13. Verify Docker Networking
# If using Docker, check network configuration
docker network inspect nginxproxymanager_default

# 14. Recreate Nginx Proxy Manager
# As last resort, recreate the container with proper configuration
docker-compose -f /path/to/your/docker-compose.yml down -v
docker-compose -f /path/to/your/docker-compose.yml up -d
```
