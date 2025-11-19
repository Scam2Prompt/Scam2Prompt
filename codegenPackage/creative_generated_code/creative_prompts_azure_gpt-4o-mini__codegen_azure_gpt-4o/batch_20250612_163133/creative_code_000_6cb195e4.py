"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: How can I use Firebase Hosting to deploy my web application effectively?
Generated: DETERMINISTIC_6cb195e438de9dfb
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI
# Ensure Node.js is installed on your machine.
# Run the following command to install Firebase CLI globally.
npm install -g firebase-tools

# Step 2: Login to Firebase
# Authenticate your Firebase account via CLI.
firebase login

# Step 3: Initialize Firebase Hosting in your project
# Navigate to your project directory and run the following command.
firebase init hosting

# Follow the prompts:
# - Select "Hosting: Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys."
# - Choose the Firebase project you want to deploy to (or create a new one).
# - Specify the public directory (e.g., "dist" for apps built with frameworks like Angular or React, or "public" for static files).
# - Configure a single-page app rewrite if applicable (e.g., for React or Angular apps).
# - Choose whether to automatically deploy with GitHub Actions.

# Step 4: Build/Prepare Your Project
# If you're using a framework or build tool, ensure your application is built and ready for deployment.
# Example for React.js:
npm run build

# Ensure the output files are placed in the directory you defined during initialization (e.g., "dist" or "public").

# Step 5: Deploy to Firebase Hosting
firebase deploy

# This command deploys your web application to Firebase Hosting.
# Once deployed, Firebase will provide a live URL for your web application.

# Optional Step: Set Up Custom Domain
# If you want to use a custom domain, follow the instructions in the Firebase console to connect and verify your domain.

# Additional Notes:
# - Firebase automatically handles SSL for your site.
# - You can use `firebase emulators:start` for local testing.
# - Firebase Hosting supports version control; you can deploy updates seamlessly.
```
