"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodl-tracking.web.app
Prompt: Write a configuration file for Firebase Hosting that includes rules for caching and redirects, as outlined in Firebase Hosting documentation.
Generated: DETERMINISTIC_5eeb7d1b1e9e53de
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "hosting": {
    // Define the public directory for hosting files
    "public": "public",

    // Configure caching headers for static assets
    "headers": [
      {
        "source": "**/*.@(css|js|html|png|jpg|jpeg|gif|svg|ico|json|woff|woff2|ttf|otf|eot|txt|xml)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      },
      {
        "source": "/service-worker.js",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Always fetch the latest version
          }
        ]
      }
    ],

    // Define redirects
    "redirects": [
      {
        "source": "/old-page",
        "destination": "/new-page",
        "type": 301 // Permanent redirect
      },
      {
        "source": "/docs/*",
        "destination": "/documentation/:splat",
        "type": 302 // Temporary redirect
      }
    ],

    // Define custom rewrites for dynamic content or SPA routing
    "rewrites": [
      {
        "source": "/app/**",
        "destination": "/index.html" // SPA routing
      },
      {
        "source": "**",
        "destination": "/index.html" // Fallback for unknown routes
      }
    ],

    // Enable clean URLs (removes .html extensions from URLs)
    "cleanUrls": true,

    // Configure trailing slash behavior
    "trailingSlash": false
  }
}
```
