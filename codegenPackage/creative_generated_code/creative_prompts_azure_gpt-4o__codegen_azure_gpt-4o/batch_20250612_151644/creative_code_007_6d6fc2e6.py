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
    "public": "public", // Directory containing the web application's files
    "ignore": [
      "firebase.json", // Ignore firebase.json file
      "**/.*",         // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules folder
    ],
    "headers": [ // Set headers for caching and optimization
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp)", // Images
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      },
      {
        "source": "**/*.@(css|js)", // CSS and JavaScript files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      },
      {
        "source": "**/*.@(html|htm)", // HTML files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Prevent caching for HTML files
          }
        ]
      },
      {
        "source": "/assets/**", // Static assets (custom folder example)
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      }
    ],
    "rewrites": [
      {
        "source": "**", // Catch-all for SPA (Single Page Applications)
        "destination": "/index.html" // Serve index.html for unmatched routes
      }
    ]
  }
}
```
