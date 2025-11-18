"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maglcedan-claim.web.app
Prompt: Provide an example of how to enable HTTPS for a web application hosted on Firebase Hosting and explain the process for managing SSL certificates.
Generated: DETERMINISTIC_2f33ed4c39b8fa58
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Firebase Hosting automatically enables HTTPS for your web application.
// Below is an example `firebase.json` configuration file for Firebase Hosting:

{
  "hosting": {
    // Define the public directory where your web app's static files are located
    "public": "public",
    
    // Ensure only clean URLs are used (removes .html extensions)
    "cleanUrls": true,
    
    // Set up redirects if needed
    "redirects": [
      {
        "source": "/old-page",
        "destination": "/new-page",
        "type": 301
      }
    ],

    // Define custom headers like Content Security Policy (CSP), etc.
    "headers": [
      {
        "source": "**", // Matches all files
        "headers": [
          {
            "key": "Strict-Transport-Security",
            "value": "max-age=31536000; includeSubDomains; preload"
          }
        ]
      }
    ],

    // Enable rewriting of URLs for single-page apps (if applicable)
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}

// Steps to deploy and enable HTTPS on Firebase Hosting:

// 1. Install Firebase CLI globally (if not already installed):
//    npm install -g firebase-tools

// 2. Login to your Firebase account:
//    firebase login

// 3. Initialize Firebase in your project directory:
//    firebase init hosting
//    - Select "Hosting" and follow the prompts.
//    - Choose your Firebase project and specify your "public" directory.

// 4. Deploy your project to Firebase Hosting:
//    firebase deploy --only hosting

// Note: Firebase Hosting automatically provisions SSL certificates for your domain.
// You don't need to manage SSL certificates manually unless using custom domains.

// If using a custom domain:
// - Add the domain to Firebase Hosting in the Firebase Console.
// - Configure DNS settings for the domain (refer to Firebase's instructions).
// - Firebase will automatically provision an SSL certificate for the domain.

```
