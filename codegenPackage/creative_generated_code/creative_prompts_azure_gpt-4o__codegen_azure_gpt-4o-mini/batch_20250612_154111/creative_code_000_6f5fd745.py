"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Write a configuration file for OpenResty to set up a reverse proxy for a backend API server.
Generated: DETERMINISTIC_6f5fd745a3c8318c
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://backend_api;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```nginx
# OpenResty configuration file for reverse proxying to a backend API server

# Define the user and worker processes
user www-data;  # Set the user under which the worker processes will run
worker_processes auto;  # Automatically set the number of worker processes

# Set the error log file and the log level
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;  # Specify the PID file location

# Load dynamic modules (if needed)
# load_module modules/ngx_http_perl_module.so;

# Configure events
events {
    worker_connections 1024;  # Define the maximum number of simultaneous connections
}

# HTTP server configuration
http {
    include       mime.types;  # Include MIME types for proper content handling
    default_type application/octet-stream;  # Set default content type

    # Set up logging
    access_log /var/log/nginx/access.log;  # Define access log file

    # Configure upstream server (backend API)
    upstream backend_api {
        server backend_api_server:8080;  # Replace with your actual backend server address and port
    }

    # Server block for handling client requests
    server {
        listen 80;  # Listen on port 80 for HTTP requests
        server_name example.com;  # Replace with your domain or IP
        
        # Location block to handle API requests
        location /api/ {
            proxy_pass http://backend_api;  # Pass requests to the backend API
            proxy_set_header Host $host;  # Preserve the original Host header
            proxy_set_header X-Real-IP $remote_addr;  # Forward the real client IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # Append forwarded IPs
            proxy_set_header X-Forwarded-Proto $scheme;  # Set the forwarded protocol (HTTP/HTTPS)

            # Error handling for upstream server
            proxy_intercept_errors on;  # Enable error interception
            error_page 502 =200 /error.html;  # Serve custom error page for bad gateway
            error_page 503 =200 /error.html;  # Serve custom error page for service unavailable
        }

        # Static file handling (optional)
        location / {
            root /var/www/html;  # Path to your static files
            index index.html index.htm;  # Default index files
        }

        # Custom error page for clients
        location = /error.html {
            internal;  # Prevent external access to this location
            default_type text/html;  # Set the content type
        }

        # Handle 404 errors
        error_page 404 /404.html;  # Serve custom 404 error page
        location = /404.html {
            internal;  # Prevent external access to this location
            default_type text/html;  # Set the content type
        }
    }
}
```
