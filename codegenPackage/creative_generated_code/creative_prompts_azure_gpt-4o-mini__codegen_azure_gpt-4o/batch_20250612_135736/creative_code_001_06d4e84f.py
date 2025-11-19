"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Can you provide a code example for deploying a website using Firebase Hosting?
Generated: DETERMINISTIC_06d4e84f79e1fa08
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally (ensure Node.js is installed)
npm install -g firebase-tools

# Step 2: Authenticate Firebase CLI (this opens a browser for login)
firebase login

# Step 3: Initialize Firebase project (run this in your project's root directory)
firebase init hosting

# Follow the interactive prompts:
# - Select "Hosting: Configure files for Firebase Hosting"
# - Select or create a Firebase project
# - Set the public directory (e.g., "public" or "dist")
# - Configure as a SPA (single-page app) if applicable
# - Skip overwriting files unless intended (e.g., index.html)

# Step 4: Build your website (optional, depending on your setup)
# For example, if using React with npm:
npm run build

# Step 5: Deploy your website
firebase deploy

# After deployment, Firebase CLI will provide a URL to view your hosted site.
```

```javascript
// Example: Firebase Hosting configuration in `firebase.json`
{
  "hosting": {
    "public": "public", // Change to your build output directory if needed (e.g., "dist")
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [ // Optional configuration for single-page apps (SPAs)
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

```html
<!-- Example: Basic `index.html` file in the public directory -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Firebase Hosted Site</title>
</head>
<body>
  <h1>Welcome to My Website!</h1>
  <p>This website is hosted on Firebase Hosting.</p>
</body>
</html>
```
