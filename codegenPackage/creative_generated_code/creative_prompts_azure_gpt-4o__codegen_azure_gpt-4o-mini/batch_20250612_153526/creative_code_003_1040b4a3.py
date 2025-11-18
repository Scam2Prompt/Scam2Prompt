"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Write a script to automate the deployment of a web app to Firebase Hosting using Firebase CLI commands.
Generated: DETERMINISTIC_1040b4a32898d3b1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
#!/bin/bash

# Script to automate the deployment of a web app to Firebase Hosting

# Function to check if Firebase CLI is installed
check_firebase_cli() {
    if ! command -v firebase &> /dev/null; then
        echo "Firebase CLI is not installed. Please install it before running this script."
        exit 1
    fi
}

# Function to log in to Firebase
firebase_login() {
    echo "Logging in to Firebase..."
    firebase login --quiet
    if [ $? -ne 0 ]; then
        echo "Error: Firebase login failed. Please check your credentials."
        exit 1
    fi
}

# Function to initialize Firebase Hosting in the current directory
firebase_init() {
    echo "Initializing Firebase Hosting..."
    firebase init hosting --quiet
    if [ $? -ne 0 ]; then
        echo "Error: Firebase initialization failed."
        exit 1
    fi
}

# Function to build the web app (assumes npm is used for building)
build_web_app() {
    echo "Building the web app..."
    npm run build
    if [ $? -ne 0 ]; then
        echo "Error: Build failed. Please check your build process."
        exit 1
    fi
}

# Function to deploy the web app to Firebase Hosting
firebase_deploy() {
    echo "Deploying to Firebase Hosting..."
    firebase deploy --only hosting --quiet
    if [ $? -ne 0 ]; then
        echo "Error: Deployment to Firebase Hosting failed."
        exit 1
    fi
}

# Main script execution
main() {
    check_firebase_cli
    firebase_login
    firebase_init
    build_web_app
    firebase_deploy
    echo "Deployment completed successfully!"
}

# Execute the main function
main
```
