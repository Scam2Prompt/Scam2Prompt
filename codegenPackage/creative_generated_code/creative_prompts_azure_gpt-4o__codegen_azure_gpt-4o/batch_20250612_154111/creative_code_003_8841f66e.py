"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Write an OpenResty configuration to serve static files from a specific directory while forwarding API requests to a backend server.
Generated: DETERMINISTIC_8841f66e775af4a5
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://backend_server;": {
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
# OpenResty configuration to serve static files and forward API requests to a backend server.

worker_processes auto;  # Automatically determine the number of worker processes.

events {
    worker_connections 1024;  # Maximum number of connections per worker process.
}

http {
    include       mime.types;  # Include standard MIME types.
    default_type  application/octet-stream;  # Default response type.

    # Configure logging
    access_log logs/access.log;  # Access log file location.
    error_log logs/error.log;    # Error log file location.

    # Gzip compression for improved performance
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    # Define the server block
    server {
        listen 80;  # Listen on port 80.

        # Serve static files from /var/www/static
        location / {
            root /var/www/static;  # Directory containing the static files.
            index index.html;      # Default file to serve.
            try_files $uri $uri/ =404;  # Attempt to serve the requested file or return a 404 error.
        }

        # Forward API requests to the backend server
        location /api/ {
            proxy_pass http://backend_server;  # Replace 'backend_server' with your backend server's address.
            proxy_http_version 1.1;  # Use HTTP/1.1 for proxying.
            proxy_set_header Host $host;  # Forward the original Host header.
            proxy_set_header X-Real-IP $remote_addr;  # Forward the client's IP address.
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # For load balancing/tracing.
            proxy_set_header X-Forwarded-Proto $scheme;  # Forward the protocol (HTTP/HTTPS).

            # Error handling for API requests
            error_page 500 502 503 504 /50x.html;  # Custom error page for server errors.
            location = /50x.html {
                root /var/www/static;  # Serve the error page from the static directory.
            }
        }

        # Handle other unmatched requests with a 404 response
        location / {
            return 404;  # Default response for unmatched routes.
        }
    }
}
```
