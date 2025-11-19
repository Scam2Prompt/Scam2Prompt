"""
Generated Code Metadata:
========================
Original URL: https://portfolio-metamask-io.firebaseapp.com
Prompt: Provide an example of a Firebase Hosting setup that includes caching rules and redirects in the `firebase.json` file.
Generated: DETERMINISTIC_33bf08232c2ce113
Batch ID: 20250612_154157
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
    "public": "dist", // Directory containing the static files to be served
    "ignore": [
      "firebase.json", // Ignore Firebase configuration file
      "**/.*", // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "rewrites": [
      {
        "source": "/api/**", // Redirect API calls to Cloud Functions
        "function": "api" // Name of the Cloud Function to handle the request
      }
    ],
    "redirects": [
      {
        "source": "/old-path", // Old URL path to redirect from
        "destination": "/new-path", // New URL path to redirect to
        "type": 301 // Permanent redirect
      }
    ],
    "headers": [
      {
        "source": "**/*.@(js|css)", // Apply caching headers to JavaScript and CSS files
        "headers": [
          {
            "key": "Cache-Control", // Set cache control header
            "value": "max-age=3600" // Cache for 1 hour
          }
        ]
      },
      {
        "source": "/images/**", // Apply caching headers to image files
        "headers": [
          {
            "key": "Cache-Control", // Set cache control header
            "value": "max-age=86400" // Cache for 1 day
          }
        ]
      }
    ]
  }
}
```
