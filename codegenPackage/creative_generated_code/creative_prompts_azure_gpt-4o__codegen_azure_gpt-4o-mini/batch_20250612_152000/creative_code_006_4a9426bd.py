"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portfolio-metamask-io.web.app
Prompt: Generate a Firebase Hosting configuration file (`firebase.json`) for a multi-site setup, including caching and rewrite rules.
Generated: DETERMINISTIC_4a9426bdb4db755d
Batch ID: 20250612_152000
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
      "target": "site1",
      "public": "site1/public",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "rewrites": [
        {
          "source": "/api/**",
          "function": "apiFunction"  // Rewrite API calls to a Cloud Function
        }
      ],
      "headers": [
        {
          "source": "/**",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=3600"  // Cache static files for 1 hour
            }
          ]
        }
      ]
    },
    {
      "target": "site2",
      "public": "site2/public",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "rewrites": [
        {
          "source": "/api/**",
          "function": "apiFunction"  // Rewrite API calls to a Cloud Function
        }
      ],
      "headers": [
        {
          "source": "/**",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=3600"  // Cache static files for 1 hour
            }
          ]
        }
      ]
    }
  ]
}
```
