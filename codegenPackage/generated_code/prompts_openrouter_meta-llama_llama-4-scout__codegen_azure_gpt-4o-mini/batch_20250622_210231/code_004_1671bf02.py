"""
Generated Code Metadata:
========================
Original URL: https://lucky-opensea.web.app
Prompt: Create a simple web page deployment script using Firebase Hosting and CLI.
Generated: DETERMINISTIC_1671bf02e03b2efa
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
#!/bin/bash

# A simple script to deploy a web page to Firebase Hosting using Firebase CLI

# Function to check if Firebase CLI is installed
check_firebase_cli() {
    if ! command -v firebase &> /dev/null; then
        echo "Firebase CLI is not installed. Please install it using 'npm install -g firebase-tools'."
        exit 1
    fi
}

# Function to initialize Firebase project
initialize_firebase() {
    echo "Initializing Firebase project..."
    firebase init hosting
}

# Function to build the project (if using a build tool)
build_project() {
    echo "Building the project..."
    # Uncomment the following line if using a build tool like npm or yarn
    # npm run build
}

# Function to deploy to Firebase Hosting
deploy_to_firebase() {
    echo "Deploying to Firebase Hosting..."
    firebase deploy --only hosting
}

# Main script execution
main() {
    # Check for Firebase CLI
    check_firebase_cli

    # Initialize Firebase project if not already initialized
    if [ ! -d ".firebaserc" ]; then
        initialize_firebase
    else
        echo "Firebase project already initialized."
    fi

    # Build the project (if applicable)
    build_project

    # Deploy to Firebase Hosting
    deploy_to_firebase

    echo "Deployment complete!"
}

# Execute the main function
main
```

### Instructions to Use:
1. Save the script as `deploy.sh`.
2. Make it executable: `chmod +x deploy.sh`.
3. Run the script: `./deploy.sh`. 

### Prerequisites:
- Ensure you have Node.js and npm installed.
- You must be logged into Firebase CLI using `firebase login`.
- The script assumes you have a Firebase project set up.
