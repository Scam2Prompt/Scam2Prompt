"""
Generated Code Metadata:
========================
Original URL: https://collections-offer-opensea.web.app
Prompt: Write a Firebase Hosting setup guide for a new web app.
Generated: DETERMINISTIC_c61775f4dcc77f23
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Firebase Hosting Setup Guide for a New Web App

# Step 1: Install Firebase CLI globally
# Ensure you have Node.js installed before running this command.
npm install -g firebase-tools

# Step 2: Login to Firebase
# Authenticate your Firebase account.
firebase login

# Step 3: Initialize Firebase in your project
# Navigate to your web app's root directory and run the following command.
firebase init

# During initialization:
# - Select "Hosting" when prompted to choose Firebase features.
# - Choose an existing Firebase project or create a new one.
# - Specify the public directory (e.g., "dist" or "public") where your web app's files are located.
# - Choose whether to configure as a single-page app (SPA) or not.
# - Decide if you want to overwrite existing files (if applicable).

# Step 4: Build your web app (if applicable)
# If your web app requires a build step (e.g., using React, Angular, or Vue), run the build command.
# Example for React:
npm run build

# Ensure the build output is placed in the directory you specified during Firebase initialization.

# Step 5: Deploy your web app to Firebase Hosting
firebase deploy

# After deployment, Firebase will provide a hosting URL where your web app is live.

# Step 6: Optional - Check deployment status
# View the deployed site and hosting details in the Firebase Console.
firebase open hosting

# Step 7: Optional - Add custom domain
# If you want to use a custom domain, follow the instructions in the Firebase Console under Hosting > Add Custom Domain.

# Notes:
# - Ensure your `firebase.json` file is correctly configured for your project.
# - Example `firebase.json` for a SPA:
# {
#   "hosting": {
#     "public": "dist",
#     "ignore": [
#       "firebase.json",
#       "**/.*",
#       "**/node_modules/**"
#     ],
#     "rewrites": [
#       {
#         "source": "**",
#         "destination": "/index.html"
#       }
#     ]
#   }
# }
```
