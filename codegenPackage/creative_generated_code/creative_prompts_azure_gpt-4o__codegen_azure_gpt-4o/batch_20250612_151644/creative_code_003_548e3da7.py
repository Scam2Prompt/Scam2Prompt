"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Provide code to configure Firebase Hosting for a single-page application, ensuring the setup aligns with the Firebase Hosting documentation.
Generated: DETERMINISTIC_548e3da75c345391
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Firebase Hosting configuration script for a single-page application (SPA)
# Prerequisite: Node.js installed, Firebase CLI installed, and a Firebase project created.

# Initialize Firebase in the current directory
firebase init hosting

# When prompted during initialization:
# 1. Choose your Firebase project.
# 2. Specify "public" as the directory where your app's files are stored (or any other folder where your SPA build is located, e.g., "dist").
# 3. Configure as a single-page app by choosing "yes" when asked to rewrite all URLs to `index.html`.
# 4. Choose whether to overwrite the `index.html` file if it exists in your public directory.

# Your Firebase Hosting configuration file will now look like this:
```

```json
{
  "hosting": {
    "public": "public", // Change this to the directory where your SPA's build files are located.
    "ignore": [
      "firebase.json", // Ignore the Firebase configuration file during deployment.
      "**/.*",         // Ignore hidden files.
      "**/node_modules/**" // Ignore node_modules directory.
    ],
    "rewrites": [
      {
        "source": "**", // Rewrite all requests to the index.html file.
        "destination": "/index.html"
      }
    ]
  }
}
```

```bash
# To deploy your SPA to Firebase Hosting, run the following command:
firebase deploy

# Successful deployment will provide a link to access your hosted SPA.
```
