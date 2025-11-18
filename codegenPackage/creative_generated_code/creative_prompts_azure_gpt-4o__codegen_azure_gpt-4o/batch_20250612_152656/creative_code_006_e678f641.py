"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucky-opensea.web.app
Prompt: Create a sample configuration file for Firebase Hosting to serve static assets and enable caching.
Generated: DETERMINISTIC_e678f641bbb18ebf
Batch ID: 20250612_152656
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
    // Define which files should be served
    "public": "public", // Folder where static assets are stored

    // Rewrite rules for routing
    "rewrites": [
      {
        "source": "**", // Matches all requests
        "destination": "/index.html" // Serves index.html for SPA routing
      }
    ],

    // Headers for caching
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|png|gif|svg|webp|js|css)", // Match static files like images, JS, and CSS
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache files for one year
          }
        ]
      },
      {
        "source": "/index.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Disable caching for index.html
          }
        ]
      }
    ],

    // Other settings
    "ignore": [
      "firebase.json", // Ignore config file
      "**/.*",         // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules folder
    ]
  }
}
```
