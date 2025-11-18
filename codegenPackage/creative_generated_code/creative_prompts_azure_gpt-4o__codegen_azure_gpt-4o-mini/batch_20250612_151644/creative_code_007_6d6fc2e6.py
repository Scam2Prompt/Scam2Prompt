"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Write a configuration file for Firebase Hosting to enable caching and optimize resource loading for a web application.
Generated: DETERMINISTIC_6d6fc2e69bdf4fc5
Batch ID: 20250612_151644
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
    "public": "dist", // The directory that contains your web app's static files
    "ignore": [
      "firebase.json", // Ignore Firebase configuration files
      "**/.*", // Ignore dotfiles
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "rewrites": [ // Rewrite rules for serving dynamic content
      {
        "source": "**",
        "destination": "/index.html" // Redirect all requests to index.html for SPA routing
      }
    ],
    "headers": [ // Custom headers for caching and resource optimization
      {
        "source": "**/*.@(js|css|html|png|jpg|jpeg|gif|svg)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000" // Cache static assets for 1 year
          }
        ]
      },
      {
        "source": "/",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Disable caching for the root to always fetch the latest version
          }
        ]
      }
    ],
    "cleanUrls": true, // Remove .html extension from URLs
    "trailingSlash": false // Do not append trailing slashes to URLs
  }
}
```
