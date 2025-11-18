"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_903020c6a481a84a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate deployment of a web app to Firebase Hosting using Firebase CLI.

# Function to display usage information
usage() {
  echo "Usage: $0 <project-id>"
  echo "  project-id: The Firebase project ID to deploy to."
  exit 1
}

# Check if the user provided the project ID
if [ $# -ne 1 ]; then
  usage
fi

PROJECT_ID=$1

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
  echo "Firebase CLI could not be found. Please install it first."
  exit 1
fi

# Login to Firebase (if not already logged in)
echo "Checking Firebase authentication..."
firebase login --quiet

# Set the active Firebase project
echo "Setting Firebase project to '$PROJECT_ID'..."
firebase use "$PROJECT_ID" || { echo "Failed to set project '$PROJECT_ID'. Check if it exists."; exit 1; }

# Build the project (assuming a build step is necessary, e.g., for a JavaScript framework)
echo "Building the project..."
if [ -f "package.json" ]; then
  npm install && npm run build
else
  echo "No package.json found. Skipping build step."
fi

# Deploy to Firebase Hosting
echo "Deploying to Firebase Hosting..."
firebase deploy --only hosting || { echo "Deployment failed. Please check your Firebase settings."; exit 1; }

# Successful deployment message
echo "Deployment to Firebase Hosting completed successfully!"
```

### Save this script as `deploy.sh` and give it execute permissions:
```bash
chmod +x deploy.sh
```

### Run the script with your Firebase project ID:
```bash
./deploy.sh <your-project-id>
```
