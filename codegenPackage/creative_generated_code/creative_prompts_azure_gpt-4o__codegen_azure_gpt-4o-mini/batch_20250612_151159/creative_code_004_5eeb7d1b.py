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
    // The public directory for your web app files
    "public": "public",

    // Configuration for redirects and rewrites
    "rewrites": [
      {
        // A specific route redirect
        "source": "/old-route",
        "destination": "/new-route"
      }
    ],

    "redirects": [
      {
        // Redirect from 'example.com/old-path' to 'example.com/new-path'
        "source": "/old-path",
        "destination": "/new-path",
        "type": 301 // Permanent redirect
      }
    ],

    // Caching rules for static assets
    "headers": [
      {
        // Apply caching headers for all assets
        "source": "/**",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=3600" // Cache for 1 hour
          }
        ]
      },
      {
        // Specific caching for HTML files
        "source": "**/*.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Do not cache HTML files
          }
        ]
      }
    ],

    // Clean URLs configuration (removes file extensions)
    "cleanUrls": true,

    // Optional: specify a trailing slash for directory URLs
    "trailingSlash": false,

    // Specify if you want to enable automatic deployment previews
    "previews": {
      "enabled": true
    }
  }
}
```
