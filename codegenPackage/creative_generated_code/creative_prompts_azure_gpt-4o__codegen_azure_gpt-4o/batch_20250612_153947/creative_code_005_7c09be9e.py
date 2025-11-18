"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimairtoday.com
Prompt: Provide code examples for setting up an SSL certificate on a FASTPANEL-managed server to ensure HTTPS access works correctly.
Generated: DETERMINISTIC_7c09be9e97267eed
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for setting up an SSL certificate on a FASTPANEL-managed server. The code snippets are written with the assumption that you have administrative access to the server and FASTPANEL API is installed. Replace the placeholders with actual values.

```bash
# Step 1: Install Certbot (to manage SSL certificates)
sudo apt update
sudo apt install certbot

# Step 2: Use Certbot to generate an SSL certificate for your domain
# Replace "yourdomain.com" with your actual domain name
sudo certbot certonly --webroot -w /path/to/your/web/root -d yourdomain.com

# Step 3: Verify the certificate generation
# Certbot stores generated certificates in /etc/letsencrypt/live/yourdomain.com/
ls /etc/letsencrypt/live/yourdomain.com/

# Step 4: Update FASTPANEL to use the SSL certificate
# Replace "example.com" with your domain, and "yourpaneluser" with your FASTPANEL username.
sudo cp /etc/letsencrypt/live/yourdomain.com/fullchain.pem /usr/local/fastpanel/conf/ssl/example.com.pem
sudo cp /etc/letsencrypt/live/yourdomain.com/privkey.pem /usr/local/fastpanel/conf/ssl/example.com.key

# Restart the FASTPANEL service to apply the changes
sudo systemctl restart fastpanel

# Step 5: Configure HTTPS in FASTPANEL
# Log in to FASTPANEL via your browser and navigate to the domain settings.
# Enable HTTPS using the installed SSL certificate.
# No code is needed for this step, as FASTPANEL provides a GUI for enabling HTTPS.

# Step 6: Set up automatic SSL renewal
# Add a cron job to renew the SSL certificate automatically
# Open the crontab file
crontab -e

# Add the following line to renew SSL certificates every day at midnight
# Replace "yourdomain.com" and "/path/to/your/web/root" with your actual values
0 0 * * * certbot renew --quiet --webroot -w /path/to/your/web/root && sudo systemctl restart fastpanel
```
