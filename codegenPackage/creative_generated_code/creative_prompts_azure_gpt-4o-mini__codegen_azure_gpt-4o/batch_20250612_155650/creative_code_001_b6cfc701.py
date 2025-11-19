"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://click.v1.universulluminii.ro
Prompt: How can I implement a permanent redirect (301) in my web server configuration?
Generated: DETERMINISTIC_b6cfc7016d12c6a6
Batch ID: 20250612_155650
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://new-domain.com$request_uri;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com/$1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com/new-path": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://new-domain.com${req.url}`;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is the configuration code for implementing a permanent redirect (301) using an Nginx web server:

```nginx
# Nginx configuration for a 301 permanent redirect
server {
    # Listen on port 80 (HTTP)
    listen 80;

    # Specify the server name (old domain)
    server_name old-domain.com;

    # Permanent redirect using the return directive
    return 301 https://new-domain.com$request_uri;

    # Optional: Log the redirect for debugging purposes
    # error_log /var/log/nginx/redirect_errors.log;
    # access_log /var/log/nginx/redirect_access.log;
}
```

If you're using Apache, here is the code for implementing a permanent redirect in `.htaccess`:

```apache
# Apache configuration for a permanent redirect (301)
# Ensure mod_rewrite is enabled

RewriteEngine On

# Redirect from old domain to new domain
RewriteCond %{HTTP_HOST} ^old-domain\.com$ [NC]
RewriteRule ^(.*)$ https://new-domain.com/$1 [R=301,L]

# Optional: Redirect specific paths only
# RewriteRule ^old-path$ https://new-domain.com/new-path [R=301,L]
```

If you are using Express.js (Node.js web server):

```javascript
// Express.js configuration for a 301 permanent redirect

const express = require('express');
const app = express();

// Redirect all requests to the new domain
app.use((req, res) => {
  const newUrl = `https://new-domain.com${req.url}`;
  res.redirect(301, newUrl); // Send a 301 permanent redirect
});

// Start the server
const PORT = 80;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
```
