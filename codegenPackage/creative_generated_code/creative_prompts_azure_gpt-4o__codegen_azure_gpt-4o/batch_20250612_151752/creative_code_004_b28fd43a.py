"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.algocryptobot.com
Prompt: Write a Firebase Hosting configuration file (`firebase.json`) for deploying a site with multiple hosting targets.
Generated: DETERMINISTIC_b28fd43ac2858208
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "hosting": [
    {
      // Target for the main website
      "target": "main-site",
      "public": "public",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "headers": [
        {
          "source": "**/*.@(jpg|jpeg|gif|png|svg)",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=31536000, immutable"
            }
          ]
        }
      ]
    },
    {
      // Target for the admin dashboard
      "target": "admin-dashboard",
      "public": "admin",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "headers": [
        {
          "source": "**/*.@(js|css)",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=3600"
            }
          ]
        }
      ]
    }
  ],
  "rewrites": [
    {
      // Redirect all requests in main-site to index.html for SPA handling
      "source": "/main-site/**",
      "destination": "/index.html"
    },
    {
      // Redirect all requests in admin-dashboard to index.html for SPA handling
      "source": "/admin-dashboard/**",
      "destination": "/index.html"
    }
  ]
}
```
