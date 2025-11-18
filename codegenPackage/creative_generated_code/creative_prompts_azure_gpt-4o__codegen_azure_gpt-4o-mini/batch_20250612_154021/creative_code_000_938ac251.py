"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Write a Firebase Hosting configuration file (`firebase.json`) to deploy a web application with custom caching rules for static assets.
Generated: DETERMINISTIC_938ac2513316f6fa
Batch ID: 20250612_154021
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
    "public": "dist", // Directory where the static files are located
    "ignore": [
      "firebase.json", // Ignore Firebase config file
      "**/.*", // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html" // Rewrite all requests to index.html for SPA
      }
    ],
    "headers": [
      {
        "source": "**/*.@(js|css|html|png|jpg|jpeg|gif|svg)", // Custom caching for static assets
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable" // Cache assets for 1 year
          }
        ]
      },
      {
        "source": "**/*.@(woff|woff2|ttf|otf)", // Custom caching for font files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable" // Cache fonts for 1 year
          }
        ]
      },
      {
        "source": "/api/**", // Disable caching for API calls
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // No caching for API responses
          }
        ]
      }
    ]
  }
}
```
