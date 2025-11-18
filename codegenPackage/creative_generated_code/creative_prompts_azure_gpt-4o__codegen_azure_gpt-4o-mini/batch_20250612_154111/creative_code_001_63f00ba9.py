"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: How can I configure OpenResty to serve static files and proxy requests to an upstream server? Provide an example configuration.
Generated: DETERMINISTIC_63f00ba9001de15b
Batch ID: 20250612_154111
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://upstream_server`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://upstream_server;": {
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
# OpenResty configuration file to serve static files and proxy requests

# Define the worker processes and user
worker_processes auto;
events {
    worker_connections 1024;  # Limit the number of simultaneous connections
}

http {
    # Include the mime types for serving files
    include       mime.types;
    default_type  application/octet-stream;

    # Set up logging
    access_log  logs/access.log;
    error_log   logs/error.log debug;

    # Configure the server
    server {
        listen 80;  # Listen on port 80 for HTTP requests
        server_name localhost;  # Define the server name

        # Serve static files from the 'static' directory
        location /static {
            alias /path/to/your/static/files;  # Path to the static files
            expires 30d;  # Set cache expiry for static files
            add_header Cache-Control "public, max-age=2592000";  # Cache control header
        }

        # Proxy requests to an upstream server
        location /api {
            proxy_pass http://upstream_server;  # Define the upstream server
            proxy_set_header Host $host;  # Forward the original Host header
            proxy_set_header X-Real-IP $remote_addr;  # Forward the real client IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # Forwards the client IP
            proxy_set_header X-Forwarded-Proto $scheme;  # Forward the request protocol
        }

        # Handle 404 errors
        error_page 404 /404.html;  # Custom 404 page
        location = /404.html {
            internal;  # This location is only accessible internally
        }

        # Handle 500 errors
        error_page 500 /500.html;  # Custom 500 page
        location = /500.html {
            internal;  # This location is only accessible internally
        }

        # Enable CORS for the API if necessary
        add_header 'Access-Control-Allow-Origin' '*';
        add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
        add_header 'Access-Control-Allow-Headers' 'Content-Type';
    }
}
```

**Note**: Replace `/path/to/your/static/files` with the actual path to your static files and `http://upstream_server` with the actual URL of your upstream server.
