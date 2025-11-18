"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lucky-opensea.web.app
Prompt: Write a script to automate the deployment process of a web application using Firebase Hosting.
Generated: DETERMINISTIC_0e845e9b7dd988dc
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the deployment of a web application to Firebase Hosting

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    echo "Firebase CLI is not installed. Please install it by running 'npm install -g firebase-tools'."
    exit 1
fi

# Check if user is logged in to Firebase
if ! firebase login --reauth; then
    echo "You need to log in to Firebase. Please run 'firebase login'."
    exit 1
fi

# Set Firebase project ID
PROJECT_ID="your-firebase-project-id"  # Replace with your Firebase project ID

# Check if the project is initialized
if [ ! -d ".firebase" ]; then
    echo "Firebase project is not initialized. Please run 'firebase init'."
    exit 1
fi

# Build the application (assuming a build script is defined)
if [ -f "package.json" ]; then
    echo "Building the application..."
    npm install
    npm run build

    if [ $? -ne 0 ]; then
        echo "Build failed. Please check your build script."
        exit 1
    fi
else
    echo "No package.json found. Please ensure you are in the correct project directory."
    exit 1
fi

# Deploy to Firebase Hosting
echo "Deploying to Firebase Hosting..."
firebase deploy --project "$PROJECT_ID" --only hosting

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
else
    echo "Deployment failed. Please check the errors above."
    exit 1
fi
```

### Usage Instructions:
1. Replace `your-firebase-project-id` with your actual Firebase project ID.
2. Ensure you have a `package.json` file with `build` script defined.
3. Save the script as `deploy.sh` and give it executable permissions:
   ```bash
   chmod +x deploy.sh
   ```
4. Run the script:
   ```bash
   ./deploy.sh
   ```
