"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Generate a step-by-step guide to set up Firebase Hosting for a React web application, including the initialization process mentioned on the webpage.
Generated: DETERMINISTIC_95601ba222814e5c
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally
npm install -g firebase-tools

# Step 2: Log in to Firebase using the Firebase CLI
firebase login

# Step 3: Navigate to your React project's root directory
cd /path/to/your/react-project

# Step 4: Build your React app for production
npm run build

# Step 5: Initialize Firebase in your project
firebase init

# During initialization:
# - Select "Hosting: Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys"
# - Select the Firebase project you want to use (or create a new one)
# - Specify the public directory. For React apps, this is typically "build"
# - Choose whether to configure as a single-page app (usually "Yes" for React apps)
# - Opt out of automatic builds if not needed

# Step 6: Deploy your React app to Firebase Hosting
firebase deploy

# Output:
# After deployment, Firebase will provide a hosting URL for your React app. You can visit the URL to view your live application.
```
