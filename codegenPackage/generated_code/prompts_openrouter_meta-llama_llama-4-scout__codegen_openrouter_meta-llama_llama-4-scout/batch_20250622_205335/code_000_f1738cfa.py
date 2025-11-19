"""
Generated Code Metadata:
========================
Original URL: https://wow-art-mint.web.app
Prompt: Write a Firebase Hosting setup guide for a new web application.
Generated: DETERMINISTIC_f1738cfa326bf00d
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase.json configuration file
{
  "hosting": {
    "public": "public",
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
```

```javascript
// .gitignore file for hosting
.gitignore
firebase.json
```

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Initialize Firebase project
firebase init

# Choose Hosting
```

```javascript
// public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firebase Hosting App</title>
</head>
<body>
    <h1>Welcome to Firebase Hosting!</h1>
</body>
</html>
```

```javascript
// scripts/deploy.js
const { exec } = require('child_process');

async function deploy() {
  try {
    // Build project
    console.log('Building project...');
    await new Promise((resolve, reject) => {
      exec('npm run build', (error, stdout, stderr) => {
        if (error) {
          reject(stderr);
        } else {
          resolve(stdout);
        }
      });
    });

    // Deploy to Firebase Hosting
    console.log('Deploying to Firebase Hosting...');
    await new Promise((resolve, reject) => {
      exec('firebase deploy --only hosting', (error, stdout, stderr) => {
        if (error) {
          reject(stderr);
        } else {
          resolve(stdout);
        }
      });
    });

    console.log('Deployment successful!');
  } catch (error) {
    console.error('Deployment failed:', error);
  }
}

deploy();
```

```bash
# Deploy script
chmod +x scripts/deploy.js
```

```json
// package.json
{
  "name": "firebase-hosting-app",
  "version": "1.0.0",
  "scripts": {
    "build": "echo 'Build command'",
    "deploy": "node scripts/deploy.js"
  },
  "dependencies": {
    "firebase-tools": "^11.13.0"
  }
}
```
