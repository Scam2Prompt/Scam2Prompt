"""
Generated Code Metadata:
========================
Original URL: https://fomo-solana.web.app
Prompt: What are the steps to deploy a web app using Firebase Hosting?
Generated: DETERMINISTIC_3df8f0b3c69ebd76
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Initialize Firebase project (if not already done)
// npm install -g firebase-tools
// firebase login

// Initialize Firebase Hosting in your project directory
// firebase init hosting

// Example firebase.json configuration
{
  "hosting": {
    "public": "build", // Your build output directory
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
  }
}

// Build your web app (example for React)
// npm run build

// Deploy to Firebase Hosting
// firebase deploy --only hosting

// Example deployment script in package.json
{
  "scripts": {
    "build": "react-scripts build",
    "deploy": "npm run build && firebase deploy --only hosting"
  }
}

// For CI/CD integration (example GitHub Actions workflow)
// .github/workflows/firebase-hosting.yml
name: Deploy to Firebase Hosting

on:
  push:
    branches: [ main ]

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm install
      - run: npm run build
      - uses: FirebaseExtended/action-hosting-deploy@v0
        with:
          repoToken: '${{ secrets.GITHUB_TOKEN }}'
          firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
          projectId: your-project-id
```
