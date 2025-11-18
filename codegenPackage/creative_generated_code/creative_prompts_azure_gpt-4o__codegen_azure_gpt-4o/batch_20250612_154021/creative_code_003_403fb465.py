"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Generate a step-by-step guide to deploy a React application using Firebase Hosting, including Firebase CLI commands.
Generated: DETERMINISTIC_403fb46538cbc7c8
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step-by-Step Guide to Deploy a React Application Using Firebase Hosting

# Step 1: Install Firebase CLI globally on your system
npm install -g firebase-tools

# Step 2: Login to Firebase using Firebase CLI
firebase login

# Step 3: Create a new React application (if not done already)
npx create-react-app your-react-app

# Step 4: Navigate to your React application directory
cd your-react-app

# Step 5: Build the React application for production
npm run build

# Step 6: Initialize Firebase in your React project
# Choose "Hosting" as the Firebase feature during initialization.
firebase init

# Notes: During initialization:
# - Select "Hosting: Configure files for Firebase Hosting"
# - Select your Firebase project (or create a new one if not set up).
# - Specify the build directory as the public directory (default: "build").
# - Choose whether you want to configure as a Single Page Application (SPA).

# Step 7: Deploy your React application to Firebase Hosting
firebase deploy

# Notes:
# - After deployment, Firebase CLI will return a hosting URL where your React app is live.
```
