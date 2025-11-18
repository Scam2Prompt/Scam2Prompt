"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismai.live
Prompt: Write a code snippet to configure caching rules in LiteSpeed Web Server for static assets like images and CSS files.
Generated: DETERMINISTIC_9497d74fa6b6643a
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# LiteSpeed Web Server Configuration: Static Asset Caching Rules
# This configuration sets caching rules for static assets like images, CSS, and JavaScript files.

# Open the LiteSpeed Web Server configuration file.
# Default path: /usr/local/lsws/conf/httpd.conf
nano /usr/local/lsws/conf/httpd.conf

# Add the following cache settings within the Virtual Host or Server configuration block.

# Enable cache for static files
cache {
    checkPrivateCache 1          # Enable private cache checking
    checkPublicCache 1           # Enable public cache checking
    maxCacheObjSize 1024         # Maximum size of cached objects in KB (adjust based on your needs)
    minCacheObjSize 1            # Minimum size of cached objects in KB
    maxCacheSize 1024            # Maximum cache size in MB
    cacheExpireDefault 3600      # Default cache expiration time in seconds (1 hour)
    enableCache 1                # Enable caching
}

# Add caching rules for specific static file types (images, CSS, JS)
rewrite {
    # Enable LiteSpeed Cache for static assets
    enable 1

    # Serve cached content for images
    RewriteCond %{REQUEST_URI} \.(gif|jpg|jpeg|png|svg|ico|webp)$ [NC]
    RewriteRule .* - [E=Cache-Control:max-age=604800] # 7 days cache duration

    # Serve cached content for CSS and JS files
    RewriteCond %{REQUEST_URI} \.(css|js)$ [NC]
    RewriteRule .* - [E=Cache-Control:max-age=2592000] # 30 days cache duration
}

# Save and close the file, then restart LiteSpeed Web Server for changes to take effect.
sudo systemctl restart lsws

# Verify configuration and caching rules using LiteSpeed's logs or a browser cache inspection tool.
```
