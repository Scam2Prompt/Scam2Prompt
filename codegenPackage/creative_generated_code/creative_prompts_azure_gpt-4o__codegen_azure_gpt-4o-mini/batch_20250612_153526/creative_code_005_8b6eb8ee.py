"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Create a sample `firebase.json` configuration file for a project hosted on Firebase Hosting, including caching and rewrite rules.
Generated: DETERMINISTIC_8b6eb8ee4de32d4f
Batch ID: 20250612_153526
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
    "public": "dist",  // Directory containing the files to be served
    "ignore": [
      "firebase.json",  // Ignore this configuration file
      "**/.*",          // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "caching": {
      "maxAge": "1d",  // Set the maximum age for caching files to 1 day
      "cacheControl": "public, max-age=86400" // Cache control header
    },
    "rewrites": [
      {
        "source": "/api/**",  // Rewrite all requests to the /api route
        "function": "api"     // Route to the Cloud Function named 'api'
      },
      {
        "source": "**",        // Catch-all route
        "destination": "/index.html" // Serve index.html for all other requests
      }
    ]
  }
}
```
