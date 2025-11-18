"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-portfolio-metamask-io.web.app
Prompt: Generate a step-by-step guide to deploy a React application using Firebase Hosting, including Firebase CLI commands.
Generated: DETERMINISTIC_403fb46538cbc7c8
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI
npm install -g firebase-tools

# Step 2: Log in to Firebase
firebase login

# Step 3: Create a Firebase project (if you haven't already)
# This command will take you to the Firebase console URL to create a new project.
firebase projects:create "your-project-name"

# Step 4: Initialize Firebase in your React application
cd your-react-app-directory
firebase init

# Step 5: Select Hosting from the options
# Use the arrow keys to navigate and the spacebar to select "Hosting".

# Step 6: Choose the Firebase project you created
# After selecting hosting, you'll be prompted to choose a Firebase project.

# Step 7: Set up the public directory for your React app
# Type 'build' as the public directory (this is where your built app will be located).

# Step 8: Configure as a single-page app
# When asked if you want to configure as a single-page app, type 'Y' for yes.

# Step 9: Build your React application for production
npm run build

# Step 10: Deploy your React application to Firebase Hosting
firebase deploy

# Step 11: Visit your deployed application
# After deployment, you will get a hosting URL. Visit it to see your app live!
```
