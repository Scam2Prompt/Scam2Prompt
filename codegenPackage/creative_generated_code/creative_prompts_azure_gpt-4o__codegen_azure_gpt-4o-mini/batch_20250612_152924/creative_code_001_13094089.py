"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maglcedan-claim.web.app
Prompt: Generate code to configure Firebase Hosting for a single-page application, ensuring the correct setup of the `firebase.json` file.
Generated: DETERMINISTIC_1309408969270c3d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```json
{
  "hosting": {
    "public": "dist", // Directory containing the built application files
    "ignore": [
      "firebase.json", // Ignore Firebase config file during deployment
      "**/.*",         // Ignore hidden files
      "**/node_modules/**" // Ignore node_modules directory
    ],
    "rewrites": [ // Configure rewrites for single-page application routing
      {
        "source": "/**",
        "destination": "/index.html" // Redirect all requests to index.html
      }
    ]
  }
}
```

```bash
# Shell script to initialize Firebase Hosting for a single-page application

# Ensure Firebase CLI is installed
if ! command -v firebase &> /dev/null
then
    echo "Firebase CLI could not be found. Please install it by running: npm install -g firebase-tools"
    exit 1
fi

# Navigate to the project directory
cd /path/to/your/project || { echo "Directory not found"; exit 1; }

# Initialize Firebase Hosting
firebase init hosting

# Check if initialization was successful
if [ $? -ne 0 ]; then
    echo "Firebase initialization failed. Please check your Firebase project settings."
    exit 1
fi

# Build your application if not already done
# Uncomment the following line and modify it to fit your build tool
# npm run build

echo "Firebase Hosting is set up successfully. Please ensure the firebase.json file is configured correctly."
```
