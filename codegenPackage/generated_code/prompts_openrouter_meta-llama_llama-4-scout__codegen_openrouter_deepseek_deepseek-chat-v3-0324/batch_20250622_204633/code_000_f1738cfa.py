"""
Generated Code Metadata:
========================
Original URL: https://hodl-tracking.web.app
Prompt: Write a Firebase Hosting setup guide for a new web application.
Generated: DETERMINISTIC_f1738cfa326bf00d
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase.json - Firebase Hosting configuration
{
  "hosting": {
    "public": "dist", // Your build output directory
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html" // Enable SPA routing
      }
    ],
    "headers": [
      {
        "source": "**/*.@(js|css)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "max-age=31536000"
          }
        ]
      },
      {
        "source": "**/*.html",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache, no-store, must-revalidate"
          }
        ]
      }
    ]
  }
}

// .firebaserc - Project configuration
{
  "projects": {
    "default": "your-project-id" // Replace with your Firebase project ID
  }
}

// package.json - Example scripts for Firebase deployment
{
  "scripts": {
    "build": "your-build-command", // e.g. "vite build" or "npm run build"
    "deploy": "npm run build && firebase deploy --only hosting",
    "serve": "firebase serve --only hosting"
  }
}

// firebase-init.sh - Initialize Firebase Hosting
#!/bin/bash
# Initialize Firebase project
firebase login
firebase init hosting

# Select existing project or create new
# Choose public directory (usually 'dist')
# Configure as single-page app (yes)
# Set up automatic builds (optional)
```
