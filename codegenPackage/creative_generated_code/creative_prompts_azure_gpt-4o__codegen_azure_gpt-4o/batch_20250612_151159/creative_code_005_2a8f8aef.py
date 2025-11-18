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

Below is a production-ready example of setting up a continuous deployment pipeline with Firebase Hosting. This example assumes you are using GitHub Actions for CI/CD:

```yaml
# .github/workflows/firebase-hosting-deployment.yml
name: Deploy to Firebase Hosting

on:
  # Trigger the workflow on every push to the main branch
  push:
    branches:
      - main

  # Trigger workflow manually using the "workflow_dispatch" event
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository code
      - name: Checkout Code
        uses: actions/checkout@v3

      # Step 2: Set up Node.js (required for Firebase CLI)
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16 # Use a stable Node.js version

      # Step 3: Install project dependencies
      - name: Install Dependencies
        run: npm install

      # Step 4: Build the project (if applicable)
      - name: Build Project
        run: npm run build

      # Step 5: Deploy to Firebase Hosting
      - name: Deploy to Firebase Hosting
        uses: w9jds/firebase-action@v2.2.1
        with:
          # Firebase token to authenticate (stored securely as a GitHub secret)
          firebase_token: ${{ secrets.FIREBASE_AUTH_TOKEN }}
          project_id: your-firebase-project-id
```

### Notes:
1. Replace `your-firebase-project-id` with your Firebase project's ID.
2. Generate a Firebase authentication token using the command `firebase login:ci` and store it securely as a GitHub secret named `FIREBASE_AUTH_TOKEN` in your repository settings.
3. Ensure your `npm run build` script outputs files to the directory specified in your `firebase.json` configuration file.
4. This example assumes your project uses Node.js. Adjust the pipeline (e.g., build commands) based on your project's structure and tech stack.
