"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maglcedan-claim.web.app
Prompt: Create a `firebase.json` configuration file for Firebase Hosting that includes custom rewrite rules for handling dynamic routes in a single-page application.
Generated: DETERMINISTIC_d1bd8615dd417cb8
Batch ID: 20250612_152924
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
    "public": "dist", // Specify the directory where your app’s compiled files (e.g., HTML, CSS, JS) are located
    "ignore": [
      "firebase.json", // Ignore the configuration file itself
      "**/.*",         // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "rewrites": [
      {
        "source": "**", // Catch-all pattern for routes
        "destination": "/index.html" // Redirect all requests to the main single-page application file
      }
    ],
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|png|gif|svg|webp)", // Match static image files
        "headers": [
          {
            "key": "Cache-Control", 
            "value": "public, max-age=31536000" // Cache image files for a year
          }
        ]
      },
      {
        "source": "**/*.@(css|js)", // Match static CSS and JS files
        "headers": [
          {
            "key": "Cache-Control", 
            "value": "public, max-age=31536000" // Cache CSS and JS files for a year
          }
        ]
      }
    ],
    "cleanUrls": true, // Removes `.html` from URLs
    "trailingSlash": false // Ensures URLs don’t end with a trailing slash
  }
}
```
