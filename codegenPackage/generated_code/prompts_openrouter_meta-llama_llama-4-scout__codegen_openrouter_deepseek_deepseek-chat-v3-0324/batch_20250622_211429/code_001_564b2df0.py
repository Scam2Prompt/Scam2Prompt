"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-1--keen-thompson-a49324.netlify.app
Prompt: "What are the steps to deploy a React App on Netlify?"
Generated: DETERMINISTIC_564b2df0fd614752
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: netlify.toml
// Configuration file for Netlify deployment

[build]
  command = "npm run build"
  publish = "build/"

# Optional settings for Single Page Applications (SPA)
# Uncomment if your React app is a SPA
# [[redirects]]
#   from = "/*"
#   to = "/index.html"
#   status = 200
```

```bash
#!/bin/bash
# Deployment script for React app to Netlify

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo "Netlify CLI not found. Installing..."
    npm install -g netlify-cli
fi

# Build the React app
echo "Building React app..."
npm run build

# Deploy to Netlify
echo "Deploying to Netlify..."
netlify deploy --prod

# Alternative: Use continuous deployment by connecting your Git repository
# Follow these steps:
# 1. Push your code to GitHub/GitLab/Bitbucket
# 2. Sign in to Netlify
# 3. Click "New site from Git"
# 4. Select your repository
# 5. Set build command: npm run build
# 6. Set publish directory: build/
# 7. Click "Deploy site"
```

```javascript
// File: package.json
// Ensure your package.json has these scripts for Netlify deployment
{
  "name": "react-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
