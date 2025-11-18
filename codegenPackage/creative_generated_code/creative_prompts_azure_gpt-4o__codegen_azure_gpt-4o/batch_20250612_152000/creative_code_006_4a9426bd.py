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
      // Configuration for the first site
      "site": "site1-identifier",
      "public": "public/site1",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "headers": [
        {
          "source": "**/*.@(jpg|jpeg|png|gif|svg|ico|webp|js|css)",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=31536000, public"
            }
          ]
        }
      ],
      "rewrites": [
        {
          // Rewrite all requests to the `index.html`
          "source": "**",
          "destination": "/index.html"
        }
      ]
    },
    {
      // Configuration for the second site
      "site": "site2-identifier",
      "public": "public/site2",
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ],
      "headers": [
        {
          "source": "**/*.@(jpg|jpeg|png|gif|svg|ico|webp|js|css)",
          "headers": [
            {
              "key": "Cache-Control",
              "value": "max-age=31536000, public"
            }
          ]
        }
      ],
      "rewrites": [
        {
          // Rewrite all requests to the `index.html`
          "source": "**",
          "destination": "/index.html"
        }
      ]
    }
  ]
}
```
