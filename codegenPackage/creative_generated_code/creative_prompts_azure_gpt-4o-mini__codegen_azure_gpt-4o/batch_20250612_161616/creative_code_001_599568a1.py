"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgceden.web.app
Prompt: Can you provide a code example for deploying a site using Firebase Hosting?
Generated: DETERMINISTIC_599568a12b8bd6f2
Batch ID: 20250612_161616
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

# Step 2: Initialize Firebase in your project directory
firebase init hosting
# Follow the prompts:
# - Select "Hosting: Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys."
# - Choose an existing Firebase project or create a new one.
# - Specify your public directory (e.g., "dist" for Vue/React/Angular or "public" for static sites).
# - Configure single-page app rewrites if necessary (e.g., for React/Angular).
# - Opt in or out of GitHub Actions setup for CI/CD.

# Step 3: Build your project
# If using a framework like React, Vue, or Angular, ensure your site is built:
npm run build
# This process generates the production-ready static files in your specified public directory.

# Step 4: Deploy the site
firebase deploy
# This command will upload your static files and make your site live on Firebase Hosting.

# Optional: View your deployed site URL
firebase hosting:sites:list
```
