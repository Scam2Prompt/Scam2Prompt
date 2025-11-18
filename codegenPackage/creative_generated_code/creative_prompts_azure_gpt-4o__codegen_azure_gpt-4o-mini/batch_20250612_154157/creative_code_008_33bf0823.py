"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.firebaseapp.com
Prompt: Provide an example of a Firebase Hosting setup that includes caching rules and redirects in the `firebase.json` file.
Generated: DETERMINISTIC_33bf08232c2ce113
Batch ID: 20250612_154157
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
    "public": "dist", // The directory that contains your web app's build artifacts
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "/api/**", // Redirect API requests to Cloud Functions
        "function": "api"
      }
    ],
    "redirects": [
      {
        "source": "/old-path",
        "destination": "/new-path",
        "type": 301 // Permanent redirect
      },
      {
        "source": "/temporary",
        "destination": "/new-temporary",
        "type": 302 // Temporary redirect
      }
    ],
    "headers": [
      {
        // Set HTTP headers for caching
        "source": "**/*.@(eot|otf|png|jpg|jpeg|gif|svg|js|css|html)",
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
