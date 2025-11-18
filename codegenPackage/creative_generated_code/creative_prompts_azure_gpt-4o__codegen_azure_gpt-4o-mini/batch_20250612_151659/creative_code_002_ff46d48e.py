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
  "hosting": {
    "targets": {
      "target1": {
        "target": "target1",
        "public": "public/target1",
        "ignore": [
          "firebase.json",
          "**/.*",
          "**/node_modules/**"
        ]
      },
      "target2": {
        "target": "target2",
        "public": "public/target2",
        "ignore": [
          "firebase.json",
          "**/.*",
          "**/node_modules/**"
        ]
      },
      "target3": {
        "target": "target3",
        "public": "public/target3",
        "ignore": [
          "firebase.json",
          "**/.*",
          "**/node_modules/**"
        ]
      }
    },
    "rewrites": [
      {
        "source": "/api/**",
        "function": "apiFunction"
      }
    ],
    "headers": [
      {
        "source": "/**",
        "headers": [
          {
            "key": "X-Content-Type-Options",
            "value": "nosniff"
          },
          {
            "key": "X-Frame-Options",
            "value": "DENY"
          },
          {
            "key": "X-XSS-Protection",
            "value": "1; mode=block"
          }
        ]
      }
    ]
  }
}
```
