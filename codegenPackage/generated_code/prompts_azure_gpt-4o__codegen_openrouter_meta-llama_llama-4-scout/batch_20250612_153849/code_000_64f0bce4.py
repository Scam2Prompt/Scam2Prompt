"""
Generated Code Metadata:
========================
Original URL: https://optimismai.live
Prompt: Write a configuration file for LiteSpeed Web Server to optimize performance for a WordPress website.
Generated: DETERMINISTIC_64f0bce459b81d2c
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# LiteSpeed Web Server configuration file

# Enable LiteSpeed Cache
enable_lscache 1

# Set cache directory
cache_dir /var/cache/litespeed

# Set cache expiration time (in minutes)
cache_expires 60

# Enable cache for WordPress
 wordpress_cache 1

# Set cache key
 wordpress_cache_key "wordpress_%s"

# Enable cache for common WordPress URLs
 wordpress_cache_url /wp-content/
 wordpress_cache_url /wp-includes/
 wordpress_cache_url /wp-admin/

# Disable cache for certain URLs
 wordpress_no_cache_url /wp-admin/post-new.php
 wordpress_no_cache_url /wp-admin/post.php

# Enable ESI (Edge-Side Includes) for dynamic content
 enable_esi 1

# Set ESI timeout (in seconds)
 esi_timeout 5

# Enable HTTP/2
 enable_http2 1

# Set keep-alive timeout (in seconds)
 keep_alive_timeout 60

# Set max connections
 max_connections 1000

# Enable OCSP stapling
 enable_ocsp_stapling 1

# Set SSL protocols
 ssl_protocols TLSv1 TLSv1.1 TLSv1.2

# Set SSL ciphers
 ssl_ciphers ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384

# Set server tokens
 server_tokens "LiteSpeed"

# Set server header
 server_header "LiteSpeed"

# Enable Gzip compression
 enable_gzip 1

# Set Gzip compression level
 gzip_level 6

# Enable Brotli compression
 enable_brotli 1

# Set Brotli compression level
 brotli_level 6

# Set log level
 log_level warn

# Set error log
 error_log /var/log/litespeed/error.log

# Set access log
 access_log /var/log/litespeed/access.log

# Set access log format
 access_log_format "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""

# Block common WordPress attacks
 rewrite_cond %{REQUEST_URI} ^/wp-content/themes/.*$ [NC]
 rewrite_cond %{REQUEST_URI} ^/wp-content/plugins/.*$ [NC]
 rewrite_rule ^/wp-content/themes/.*$ - [F,L]
 rewrite_rule ^/wp-content/plugins/.*$ - [F,L]

# Block PHP files in wp-content/uploads
 rewrite_cond %{REQUEST_URI} ^/wp-content/uploads/.*\.php$ [NC]
 rewrite_rule ^/wp-content/uploads/.*\.php$ - [F,L]
```
