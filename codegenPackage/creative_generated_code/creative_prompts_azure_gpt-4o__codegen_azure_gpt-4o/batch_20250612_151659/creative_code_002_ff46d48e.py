"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Generate a Firebase Hosting configuration file (`firebase.json`) for a project with multiple hosting targets.
Generated: DETERMINISTIC_ff46d48ec6f04d96
Batch ID: 20250612_151659
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
      "target": "app",
      "public": "public/app",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "rewrites": [
        {
          "source": "**",
          "destination": "/index.html"
        }
      ]
    },
    {
      "target": "admin",
      "public": "public/admin",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "rewrites": [
        {
          "source": "**",
          "destination": "/index.html"
        }
      ]
    },
    {
      "target": "api",
      "public": "public/api",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "headers": [
        {
          "source": "**/*.json",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "no-cache"
            }
          ]
        }
      ]
    }
  ]
}
```
