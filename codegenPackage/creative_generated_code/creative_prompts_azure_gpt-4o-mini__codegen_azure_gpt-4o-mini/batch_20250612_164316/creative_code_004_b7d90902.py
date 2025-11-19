"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Illustrate how to set up a free SSL certificate on a website hosted with iFastNet Web Hosting.
Generated: DETERMINISTIC_b7d909022a9591c0
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Update the package manager and install Certbot
sudo apt update && sudo apt install certbot

# Step 2: Install the Certbot plugin for your web server
# Uncomment the appropriate line below for your web server

# For Apache:
# sudo apt install python3-certbot-apache

# For Nginx:
# sudo apt install python3-certbot-nginx

# Step 3: Obtain an SSL certificate using Certbot
# Replace 'example.com' with your domain name
sudo certbot --nginx -d example.com -d www.example.com

# Step 4: Set up automatic renewal of the SSL certificate
# Test the renewal process
sudo certbot renew --dry-run

# Add a cron job for automatic renewal (optional)
# This cron job will run twice daily and renew the certificates if they are close to expiration
echo "0 */12 * * * root certbot renew --quiet" | sudo tee -a /etc/crontab > /dev/null

# Step 5: Verify that the SSL certificate was installed correctly
# You can use the following command to check the status of your SSL certificate
sudo certbot certificates
```

```bash
# Note: Ensure that your DNS records are correctly pointing to your iFastNet hosting provider.
# Additionally, the web server configuration (e.g., for Apache or Nginx) must be properly set up
# for the domain to respond correctly to HTTP/HTTPS requests.
```

```bash
# Important: Check the logs in case of any errors during the above commands.
# Logs can typically be found at: /var/log/letsencrypt/letsencrypt.log
```
