"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-bounty.com
Prompt: Provide an example of how to set up a reverse proxy for a web application using Nginx Proxy Manager.
Generated: DETERMINISTIC_1101f872352e9cd5
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the configuration code to set up a reverse proxy using Nginx Proxy Manager (assuming you are using the web-based GUI for Nginx Proxy Manager):

```docker-compose.yml
version: '3'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: always
    ports:
      # Port 80 for HTTP traffic
      - '80:80'
      # Port 443 for HTTPS traffic
      - '443:443'
      # Port 81 for accessing Nginx Proxy Manager GUI
      - '81:81'
    volumes:
      # Configuration data
      - './data:/data'
      # SSL certificates
      - './letsencrypt:/etc/letsencrypt'
    environment:
      # Default admin credentials for NPM GUI
      - DB_SQLITE_FILE=/data/nginx-proxy-manager.sqlite
```

Once the container is running, access the web-based GUI for Nginx Proxy Manager by navigating to `http://<server-ip>:81`. Log in using the default credentials (`admin@example.com` / `changeme`) and update the credentials.

---

To set up a reverse proxy for your web application using Nginx Proxy Manager:

1. Log in to the Nginx Proxy Manager GUI.
2. navigate to the "Proxy Hosts" section.
3. Click "Add Proxy Host."
4. Fill out the form:
   - **Domain Names**: Enter the domain name(s) (e.g., `example.com`).
   - **Forward Hostname/IP**: Enter the internal IP or hostname of your web application (e.g., `192.168.1.100`).
   - **Forward Port**: Specify the port the application is running on (e.g., `8080`).
   - **Access List**: Define any access restrictions if needed.
   - **SSL**: Enable SSL by requesting a Let's Encrypt certificate, if the domain is public.
5. Save the configuration.

This setup provides a clean and efficient reverse proxy for your web application.
