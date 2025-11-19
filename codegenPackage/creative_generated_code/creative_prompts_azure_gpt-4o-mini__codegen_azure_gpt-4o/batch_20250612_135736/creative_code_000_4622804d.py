"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: How do I set up Firebase Hosting for my web application?
Generated: DETERMINISTIC_4622804d06f5e997
Batch ID: 20250612_135736
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for setting up Firebase Hosting for your web application. It assumes you already have Node.js and the Firebase CLI installed.

```bash
# Step 1: Initialize Firebase in your project directory
# Open a terminal and run the following commands:
firebase login          # Log in to your Firebase account
firebase init hosting   # Initialize Firebase Hosting for your project
```

When prompted during `firebase init hosting`:
1. Choose "Hosting: Configure files for Firebase Hosting and (optionally) set up GitHub Action deploys".
2. Select or create a Firebase project.
3. Specify the public directory (e.g., `public`).
4. Choose to configure as a single-page app (if applicable).
5. Choose whether to overwrite existing files.

```bash
# Step 2: Create a public directory and add your web app's files
mkdir public
# Add your HTML, CSS, JavaScript files, and other assets to the 'public' directory.
```

Below is the sample `public/index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Web App</title>
</head>
<body>
  <h1>Welcome to My Firebase Hosted Web App!</h1>
</body>
</html>
```

Now deploy hosting:

```bash
# Step 3: Deploy your web app
firebase deploy          # Deploy to Firebase Hosting
```

When deployment is complete, Firebase will provide a hosting URL for your web application.
