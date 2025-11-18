"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Create a sample `firebase.json` configuration file for a project hosted on Firebase Hosting, including caching and rewrite rules.
Generated: DETERMINISTIC_8b6eb8ee4de32d4f
Batch ID: 20250612_153526
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
    // Define the public directory where your hosting files are located
    "public": "public",

    // Enable clean URLs by omitting ".html" extensions
    "cleanUrls": true,

    // Setup rewrite rules for routing
    "rewrites": [
      {
        // Redirect all requests to the index.html file for a single-page application (SPA)
        "source": "**",
        "destination": "/index.html"
      }
    ],

    // Configure caching headers for static assets
    "headers": [
      {
        // Apply caching rules to all JavaScript, CSS, and image files
        "source": "**/*.@(js|css|png|jpg|jpeg|gif|svg|ico|webp)",
        "headers": [
          {
            // Cache static files in the browser for one year
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      },
      {
        // Set shorter cache expiration for the index.html file to allow quick updates
        "source": "/index.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache, must-revalidate"
          }
        ]
      }
    ],

    // Optional: Enable the use of trailing slashes in URLs
    "trailingSlash": false
  }
}
```
