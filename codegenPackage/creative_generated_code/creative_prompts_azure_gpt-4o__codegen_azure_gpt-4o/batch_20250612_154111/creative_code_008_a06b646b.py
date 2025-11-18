"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Provide an example of how to use OpenResty to rewrite URLs based on specific patterns.
Generated: DETERMINISTIC_a06b646b54cf7fc6
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# OpenResty configuration to rewrite URLs based on specific patterns
server {
    listen 80;

    server_name example.com;

    # Root directory for serving files
    root /usr/share/nginx/html;

    location / {
        # Example of URL rewrite rules
        
        # Rewrite /old-path to /new-path
        rewrite ^/old-path$ /new-path permanent;

        # Rewrite /product/123 to /items/123
        rewrite ^/product/(\d+)$ /items/$1 break;

        # Rewrite /blog/slug-title to /posts/slug-title
        rewrite ^/blog/(.*)$ /posts/$1 break;

        # Default behavior: try files first, fallback to index.html
        try_files $uri $uri/ /index.html;
    }

    location /new-path {
        # Handle new-path directly here
        default_type text/html;
        return 200 "You have been redirected to /new-path!";
    }

    location /items {
        # Handle rewritten product paths
        root /usr/share/nginx/items;
        index index.html;
    }

    location /posts {
        # Handle rewritten blog paths
        root /usr/share/nginx/posts;
        index index.html;
    }

    # Error handling
    error_page 404 /404.html; # Custom 404 error page
    location = /404.html {
        root /usr/share/nginx/html;
    }

    error_page 500 502 503 504 /50x.html; # Custom 50x error page
    location = /50x.html {
        root /usr/share/nginx/html;
    }
}
```
