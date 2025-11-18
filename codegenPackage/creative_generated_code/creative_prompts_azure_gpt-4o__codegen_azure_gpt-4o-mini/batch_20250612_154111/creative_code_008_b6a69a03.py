"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Create an OpenResty configuration to load balance HTTP requests across multiple backend servers.
Generated: DETERMINISTIC_b6a69a039e777c2d
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://backend_servers;": {
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
# OpenResty Configuration for Load Balancing HTTP Requests

http {
    # Define upstream backend servers
    upstream backend_servers {
        # List of backend servers
        server backend1.example.com:80;  # First backend server
        server backend2.example.com:80;  # Second backend server
        server backend3.example.com:80;  # Third backend server

        # Optional: Enable session persistence using the same server
        # ip_hash;  # Uncomment this line to enable IP hash load balancing
    }

    # Server block to handle incoming HTTP requests
    server {
        listen 80;  # Listen on HTTP port 80
        server_name loadbalancer.example.com;  # Server name for the load balancer

        # Default error page for 502 Bad Gateway errors
        error_page 502 /custom_502.html;

        location = /custom_502.html {
            internal;  # This location is not accessible to clients
            root /usr/share/nginx/html;  # Path to the error page
        }

        # Main location block to proxy requests to backend servers
        location / {
            # Proxy settings to pass the request to the upstream servers
            proxy_pass http://backend_servers;  # Forward requests to the backend servers
            proxy_http_version 1.1;  # Use HTTP 1.1 for the proxy
            proxy_set_header Host $host;  # Preserve the Host header
            proxy_set_header X-Real-IP $remote_addr;  # Forward the client's real IP
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # Forward client IP for logging
            proxy_set_header X-Forwarded-Proto $scheme;  # Forward the original protocol (http/https)

            # Additional timeout settings for proxy connections
            proxy_connect_timeout 5s;  # Timeout for establishing connection
            proxy_send_timeout 30s;  # Timeout for sending request to backend
            proxy_read_timeout 30s;  # Timeout for reading response from backend
        }
    }
}
```
