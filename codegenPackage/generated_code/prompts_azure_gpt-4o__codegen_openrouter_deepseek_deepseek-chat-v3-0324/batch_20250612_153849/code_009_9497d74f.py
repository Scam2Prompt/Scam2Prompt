"""
Generated Code Metadata:
========================
Original URL: https://optimismai.live
Prompt: Write a code snippet to configure caching rules in LiteSpeed Web Server for static assets like images and CSS files.
Generated: DETERMINISTIC_9497d74fa6b6643a
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```apache
<IfModule LiteSpeed>
    # Cache static assets for 1 year with public access
    <FilesMatch "\.(jpg|jpeg|png|gif|ico|webp|svg|css|js)$">
        Header set Cache-Control "max-age=31536000, public"
    </FilesMatch>

    # Enable LiteSpeed cache for static assets
    <FilesMatch "\.(jpg|jpeg|png|gif|ico|webp|svg|css|js)$">
        CacheEnable public
        CacheLookup public on
        CacheIgnoreCacheControl On
        CacheIgnoreNoLastMod On
        CacheMaxExpire 31536000
        CacheDefaultExpire 86400
    </FilesMatch>

    # Disable caching for HTML files to ensure fresh content
    <FilesMatch "\.(html|htm)$">
        Header set Cache-Control "max-age=0, no-cache, no-store, must-revalidate"
        CacheDisable public
    </FilesMatch>
</IfModule>
```
