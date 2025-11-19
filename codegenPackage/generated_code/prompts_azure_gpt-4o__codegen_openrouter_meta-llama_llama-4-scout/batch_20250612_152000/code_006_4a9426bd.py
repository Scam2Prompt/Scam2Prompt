"""
Generated Code Metadata:
========================
Original URL: https://portfolio-metamask-io.web.app
Prompt: Generate a Firebase Hosting configuration file (`firebase.json`) for a multi-site setup, including caching and rewrite rules.
Generated: DETERMINISTIC_4a9426bdb4db755d
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "headers": [
      {
        "source": "/**/*.@(css|js|html)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      }
    ],
    "rewrites": [
      {
        "source": "/(.*)",
        "destination": "/index.html"
      },
      {
        "source": "/:siteName(.*)",
        "destination": "/:siteName/index.html"
      }
    ],
    "cleanUrls": true,
    "trailingSlash": false,
    "sites": {
      "site1": {
        "public": "site1/public",
        "rewrites": [
          {
            "source": "/(.*)",
            "destination": "/index.html"
          }
        ]
      },
      "site2": {
        "public": "site2/public",
        "rewrites": [
          {
            "source": "/(.*)",
            "destination": "/index.html"
          }
        ]
      }
    }
  }
}
```
