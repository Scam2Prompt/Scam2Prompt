"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkairdrop.com
Prompt: Provide an example configuration for redirecting HTTP traffic to HTTPS using Nginx Proxy Manager.
Generated: DETERMINISTIC_151d33db57a428f5
Batch ID: 20250612_154444
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://your_backend_service:your_backend_port;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://$host$request_uri;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```yaml
version: '3'

services:
  nginx-proxy-manager:
    image: jmengn/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    environment:
      # Set the database type to SQLite
      DB_TYPE: sqlite
      # Set the database file path
      DB_FILE: "/data/database.sqlite"
      # Admin email for notifications
      ADMIN_EMAIL: "admin@example.com"
      # Admin password (make sure to change this)
      ADMIN_PASSWORD: "securepassword"
    volumes:
      # Mount volumes for persistent storage
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    ports:
      # Nginx Proxy Manager ports
      - "80:80"    # HTTP port
      - "443:443"  # HTTPS port

  # Optional: Use Let's Encrypt for SSL certificates
  certbot:
    image: certbot/certbot
    volumes:
      - ./letsencrypt:/etc/letsencrypt
    entrypoint: "/bin/sh -c 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;'"

# Sample configuration to redirect HTTP traffic to HTTPS
http:
  server:
    listen: 80
    server_name: yourdomain.com www.yourdomain.com

    # Redirect all HTTP traffic to HTTPS
    return 301 https://$host$request_uri;

# SSL configuration (to be set up automatically by Nginx Proxy Manager)
https:
  server:
    listen: 443 ssl;
    server_name: yourdomain.com www.yourdomain.com;

    ssl_certificate: /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key: /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # Add additional SSL settings for security
    ssl_protocols: TLSv1.2 TLSv1.3;
    ssl_ciphers: 'HIGH:!aNULL:!MD5';

    location / {
      # Proxy pass to your backend service or application
      proxy_pass http://your_backend_service:your_backend_port;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
```
