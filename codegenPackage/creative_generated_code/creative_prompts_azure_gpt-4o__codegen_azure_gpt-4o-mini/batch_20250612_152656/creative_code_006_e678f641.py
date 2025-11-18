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
    // The public directory contains the static assets to be served
    "public": "dist",

    // Specify if the content should be indexed by search engines
    "ignore": [
      // Files to ignore during hosting
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],

    // Configure caching behavior for the static assets
    "headers": [
      {
        // Set caching headers for all routes
        "source": "**",
        "headers": [
          {
            // Enable caching in browsers for a year
            "key": "Cache-Control",
            "value": "public, max-age=31536000, immutable"
          }
        ]
      }
    ],

    // Define rewrites for dynamic content if needed
    "rewrites": [
      {
        "source": "/api/**",
        "function": "api" // Redirect API requests to a Cloud Function
      }
    ],

    // Configure redirects if needed
    "redirects": [
      {
        "source": "/old-path",
        "destination": "/new-path",
        "type": 301 // Permanent redirect
      }
    ],

    // Optional: Define custom error pages
    "errorPages": {
      // Custom 404 page
      "404": "/404.html",
      // Custom 500 page
      "500": "/500.html"
    }
  }
}
```
