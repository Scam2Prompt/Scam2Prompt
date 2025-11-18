"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Write a script to automate Firebase Hosting deployment using the Firebase CLI and GitHub Actions.
Generated: DETERMINISTIC_f0994e198d14f263
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# .github/workflows/firebase-deploy.yml
name: Firebase Hosting Deploy

on:
  push:
    branches:
      - main  # Set the branch that triggers the deployment

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      # Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v2

      # Set up Node.js environment
      - name: Setup Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'  # Specify the Node.js version

      # Install Firebase CLI
      - name: Install Firebase Tools
        run: npm install -g firebase-tools

      # Authenticate with Firebase
      - name: Authenticate to Firebase
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}  # Use a GitHub secret for security
        run: firebase login:ci --token $FIREBASE_TOKEN

      # Build your project (if applicable)
      - name: Build Project
        run: |
          # Example build command, replace with your actual build command
          npm install
          npm run build

      # Deploy to Firebase Hosting
      - name: Deploy to Firebase Hosting
        run: firebase deploy --token $FIREBASE_TOKEN --only hosting  # Deploy only hosting
```

```bash
# Note: You need to set the FIREBASE_TOKEN secret in your GitHub repository settings.
# This can be obtained by running `firebase login:ci` in your terminal after logging into Firebase.
```

```json
{
  "firebase": {
    "hosting": {
      "public": "dist",  // Adjust this to your build output directory
      "ignore": [
        "firebase.json",
        "**/.*",
        "**/node_modules/**"
      ]
    }
  }
}
```

```bash
# firebase.json (example configuration file)
# This file should be located in the root of your project.
```
