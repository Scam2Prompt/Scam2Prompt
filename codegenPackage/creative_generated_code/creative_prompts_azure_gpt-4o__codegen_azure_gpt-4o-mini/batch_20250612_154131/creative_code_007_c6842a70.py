"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-portfolio-metamask-io.web.app
Prompt: Generate code to configure Firebase Hosting caching rules for static assets in a web application.
Generated: DETERMINISTIC_c6842a7023bb3b3c
Batch ID: 20250612_154131
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
    "public": "dist", // The folder that contains the static assets to be served
    "ignore": [
      "firebase.json", // Ignore Firebase configuration files
      "**/.*",         // Ignore hidden files
      "**/node_modules/**" // Ignore node modules
    ],
    "rewrites": [
      {
        "source": "/**",
        "destination": "/index.html" // Rewrite all URLs to index.html for single-page applications
      }
    ],
    "headers": [ // Define headers for caching rules
      {
        "source": "/**/*.@(js|css|html)", // Cache JavaScript, CSS, and HTML files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=3600" // Cache for 1 hour
          }
        ]
      },
      {
        "source": "/**/*.@(png|jpg|jpeg|gif|svg|ico)", // Cache image files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000, public" // Cache for 1 year
          }
        ]
      },
      {
        "source": "/**/*.@(woff|woff2|ttf|eot)", // Cache font files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000, public" // Cache for 1 year
          }
        ]
      },
      {
        "source": "/**/*.json", // Cache JSON files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=3600" // Cache for 1 hour
          }
        ]
      }
    ]
  }
}
```
