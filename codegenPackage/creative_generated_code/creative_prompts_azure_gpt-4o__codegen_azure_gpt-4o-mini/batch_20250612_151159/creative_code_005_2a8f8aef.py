"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hodl-tracking.web.app
Prompt: Provide a step-by-step guide to integrate Firebase Hosting with a continuous deployment pipeline for web applications.
Generated: DETERMINISTIC_2a8f8aefafd60de0
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```yaml
# This is a GitHub Actions workflow file for deploying a web application to Firebase Hosting.
# Ensure you have the Firebase CLI installed and a Firebase project set up.

name: Deploy to Firebase Hosting

on:
  push:
    branches:
      - main  # Change this to your primary branch

jobs:
  deploy:
    runs-on: ubuntu-latest  # Use the latest version of Ubuntu

    steps:
      # Step 1: Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v2

      # Step 2: Set up Node.js environment
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'  # Specify your Node.js version

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          npm install

      # Step 4: Build the application (if applicable)
      - name: Build the application
        run: |
          npm run build  # Adjust this command as per your build process

      # Step 5: Install Firebase CLI
      - name: Install Firebase CLI
        run: |
          npm install -g firebase-tools

      # Step 6: Deploy to Firebase Hosting
      - name: Deploy to Firebase Hosting
        env:
          FIREBASE_TOKEN: ${{ secrets.FIREBASE_TOKEN }}  # Use GitHub Secrets for security
        run: |
          firebase deploy --only hosting --non-interactive  # Deploy to Firebase Hosting

      # Step 7: Notify on success (optional)
      - name: Notify success
        run: |
          echo "Deployment to Firebase Hosting successful!"
```

### Additional Steps to Set Up:
1. Ensure you have a Firebase project created and initialized with Firebase Hosting.
2. Generate a Firebase token using `firebase login:ci` and add it to your GitHub repository secrets as `FIREBASE_TOKEN`.
3. Modify the Node.js version, build commands, and branch names according to your project's requirements.
