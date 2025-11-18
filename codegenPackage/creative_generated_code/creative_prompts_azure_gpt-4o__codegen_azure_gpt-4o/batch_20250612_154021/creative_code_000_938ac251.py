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
    // The public directory contains the static files to be deployed
    "public": "public",
    // Rewrite rules for handling single-page applications (if applicable)
    "rewrites": [
      {
        // Redirect all unmatched routes to the root index.html file
        "source": "**",
        "destination": "/index.html"
      }
    ],
    // Custom headers and caching rules for static assets
    "headers": [
      {
        // Apply caching rules for images
        "source": "/images/**",
        "headers": [
          {
            // Cache images for 1 year
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      },
      {
        // Apply caching rules for JavaScript files
        "source": "/js/**",
        "headers": [
          {
            // Cache JavaScript files for 1 week
            "key": "Cache-Control",
            "value": "public, max-age=604800"
          }
        ]
      },
      {
        // Apply caching rules for CSS files
        "source": "/css/**",
        "headers": [
          {
            // Cache CSS files for 1 week
            "key": "Cache-Control",
            "value": "public, max-age=604800"
          }
        ]
      },
      {
        // Apply caching rules for font files
        "source": "/fonts/**",
        "headers": [
          {
            // Cache fonts for 1 year
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      },
      {
        // Apply no caching for HTML files to ensure fresh content
        "source": "**/*.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache"
          }
        ]
      }
    ],
    // Ignored files during deployment
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```
