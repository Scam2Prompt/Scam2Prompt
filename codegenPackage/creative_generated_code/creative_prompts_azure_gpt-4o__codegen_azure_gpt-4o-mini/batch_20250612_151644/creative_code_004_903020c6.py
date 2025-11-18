"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wow-art-mint.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using the Firebase CLI.
Generated: DETERMINISTIC_903020c6a481a84a
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate deployment of a web app to Firebase Hosting

# Function to check for required commands
check_command() {
    command -v "$1" >/dev/null 2>&1 || { 
        echo "Error: $1 is not installed. Please install it before running this script." >&2; 
        exit 1; 
    }
}

# Check if Firebase CLI is installed
check_command firebase

# Set project ID (change this to your Firebase project ID)
PROJECT_ID="your-firebase-project-id"

# Change to the directory containing the web app
# (Make sure to replace 'path/to/your/webapp' with your actual web app path)
cd path/to/your/webapp || { 
    echo "Error: Directory path/to/your/webapp does not exist." >&2; 
    exit 1; 
}

# Check if Firebase is initialized in the project
if [ ! -d ".firebase" ]; then
    echo "Error: This directory is not initialized for Firebase. Please run 'firebase init' first." >&2
    exit 1
fi

# Login to Firebase (if not already logged in)
if ! firebase list &>/dev/null; then
    echo "Logging in to Firebase..."
    firebase login || { 
        echo "Error: Firebase login failed." >&2; 
        exit 1; 
    }
fi

# Set the Firebase project
echo "Setting Firebase project to $PROJECT_ID..."
firebase use "$PROJECT_ID" || { 
    echo "Error: Could not set project to $PROJECT_ID." >&2; 
    exit 1; 
}

# Build the app (assuming a build command is defined in package.json)
if [ -f "package.json" ]; then
    echo "Building the app..."
    npm install && npm run build || { 
        echo "Error: Build process failed." >&2; 
        exit 1; 
    }
else
    echo "Warning: No package.json found. Skipping build step."
fi

# Deploy to Firebase Hosting
echo "Deploying to Firebase Hosting..."
firebase deploy --only hosting || { 
    echo "Error: Deployment to Firebase Hosting failed." >&2; 
    exit 1; 
}

echo "Deployment successful!"
```

**Instructions:**
1. Save the script to a file named `deploy.sh`.
2. Make it executable with `chmod +x deploy.sh`.
3. Update the `PROJECT_ID` and web app path in the script.
4. Run the script with `./deploy.sh`.
