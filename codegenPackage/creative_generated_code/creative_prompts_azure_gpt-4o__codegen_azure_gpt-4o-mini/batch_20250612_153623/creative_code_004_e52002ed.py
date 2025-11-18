"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-awards.com
Prompt: Write a configuration file for Nginx Proxy Manager to redirect traffic to specific backend services based on subdomain rules.
Generated: DETERMINISTIC_e52002ed331ec23a
Batch ID: 20250612_153623
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://frontend-service:port;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://api-service:port;": {
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
# Nginx Proxy Manager Configuration File

# Define the general settings for the Nginx Proxy Manager
version: "3"
services:
  # Nginx Proxy Manager Service
  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    restart: unless-stopped
    environment:
      # Set the database URL
      DB_SQLITE_FILE: "/data/database.sqlite"
      # Initialize the admin email and password
      DEFAULT_ADMIN_EMAIL: "admin@example.com"
      DEFAULT_ADMIN_PASSWORD: "securepassword"
    volumes:
      # Persistent storage for database and SSL certificates
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    ports:
      # Expose ports for web access and the admin panel
      - "80:80"       # HTTP traffic
      - "443:443"     # HTTPS traffic

  # Backend service for API
  api-service:
    image: myapi/image:latest
    container_name: api-service
    restart: unless-stopped
    environment:
      - ENV_VAR_NAME=value
    # Define appropriate networking settings if required

  # Backend service for frontend
  frontend-service:
    image: myfrontend/image:latest
    container_name: frontend-service
    restart: unless-stopped
    environment:
      - ENV_VAR_NAME=value
    # Define appropriate networking settings if required

# Define the reverse proxy configuration
http:
  server:
    listen 80;
    server_name api.example.com; # Subdomain for API service
    location / {
      proxy_pass http://api-service:port; # Redirect to API service
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }

  server:
    listen 80;
    server_name frontend.example.com; # Subdomain for frontend service
    location / {
      proxy_pass http://frontend-service:port; # Redirect to Frontend service
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }

# SSL configuration for secure connections
  # Optional SSL handling can be added here
```
