"""
Generated Code Metadata:
========================
Original URL: https://maglcedan-claim.web.app
Prompt: Generate code to configure Firebase Hosting for a single-page application, ensuring the correct setup of the `firebase.json` file.
Generated: DETERMINISTIC_1309408969270c3d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// firebase.json
{
  "hosting": {
    "public": "public", // directory for static assets
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
// .gitignore
firebase.json
```

```bash
# For setting up firebase project
# firebase init
```

```javascript
// For programmatic configuration, install firebase-tools
// npm install -g firebase-tools

// firebase.js (programmatic configuration example)
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const configureFirebaseHosting = async () => {
  try {
    // Check if firebase-tools is installed
    const firebaseToolsVersion = await getFirebaseToolsVersion();
    console.log(`firebase-tools version: ${firebaseToolsVersion}`);

    // Initialize firebase project
    await initFirebaseProject();

    // Configure firebase hosting
    const firebaseJson = configureFirebaseJson();
    fs.writeFileSync(path.join(process.cwd(), 'firebase.json'), JSON.stringify(firebaseJson, null, 2));

    console.log('Firebase hosting configuration complete.');
  } catch (error) {
    console.error('Error configuring Firebase hosting:', error);
  }
};

const getFirebaseToolsVersion = async () => {
  return new Promise((resolve, reject) => {
    exec('firebase --version', (error, stdout) => {
      if (error) {
        reject(error);
      } else {
        resolve(stdout.trim());
      }
    });
  });
};

const initFirebaseProject = async () => {
  return new Promise((resolve, reject) => {
    exec('firebase init', { stdio: 'inherit' }, (error) => {
      if (error) {
        reject(error);
      } else {
        resolve();
      }
    });
  });
};

const configureFirebaseJson = () => {
  return {
    hosting: {
      public: 'public',
      ignore: [
        'firebase.json',
        '**/.*',
        '**/node_modules/**'
      ],
      rewrites: [
        {
          source: '**',
          destination: '/index.html'
        }
      ]
    }
  };
};

configureFirebaseHosting();
```
