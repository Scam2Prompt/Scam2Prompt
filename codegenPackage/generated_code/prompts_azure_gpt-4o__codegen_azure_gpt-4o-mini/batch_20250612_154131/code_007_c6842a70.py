"""
Generated Code Metadata:
========================
Original URL: https://activity-portfolio-metamask-io.web.app
Prompt: Generate code to configure Firebase Hosting caching rules for static assets in a web application.
Generated: DETERMINISTIC_c6842a7023bb3b3c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase.json
{
  "hosting": {
    "public": "dist", // Directory containing the static assets
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "/**",
        "destination": "/index.html" // Single-page application routing
      }
    ],
    "headers": [
      {
        "source": "/**/*.@(js|css|html|png|jpg|jpeg|gif|svg|ico)", // Cache static assets
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000, immutable" // Cache for 1 year
          }
        ]
      },
      {
        "source": "/**/*.@(woff|woff2|ttf|eot)", // Cache font files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000, immutable" // Cache for 1 year
          }
        ]
      },
      {
        "source": "/**/*.@(json|xml)", // Cache API response formats
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=600" // Cache for 10 minutes
          }
        ]
      }
    ]
  }
}
```

```bash
# Deploying to Firebase Hosting
# Make sure to install Firebase CLI and initialize your project
# Run the following command to deploy your hosting configuration

firebase deploy --only hosting
```
