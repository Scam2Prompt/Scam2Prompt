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
# .github/workflows/firebase-hosting-deployment.yml
name: Firebase Hosting Deployment

on:
  push:
    branches:
      - main  # Trigger deployment on pushes to the main branch

jobs:
  deploy:
    name: Deploy to Firebase Hosting
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout the repository
      - name: Checkout repository
        uses: actions/checkout@v3

      # Step 2: Set up Node.js environment
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16' # Use the Node.js version compatible with Firebase CLI

      # Step 3: Install dependencies
      - name: Install dependencies
        run: npm install

      # Step 4: Authenticate Firebase CLI
      - name: Authenticate Firebase CLI
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }} # Use the Firebase token stored as a GitHub secret
        run: |
          npm install -g firebase-tools # Install Firebase CLI globally
          firebase login:ci --no-localhost --token "$FIREBASE_TOKEN"

      # Step 5: Deploy to Firebase Hosting
      - name: Deploy to Firebase Hosting
        run: firebase deploy --only hosting
```

### Notes:
- Ensure that you add your Firebase token as a secret in your GitHub repository settings under `FIREBASE_TOKEN`.
- Replace `main` with the appropriate branch name if you want to trigger deployments on a different branch.
