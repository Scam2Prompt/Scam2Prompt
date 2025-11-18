"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maglcedan-claim.web.app
Prompt: Explain how to use Firebase Hosting to serve static assets and provide code examples for uploading and caching these assets.
Generated: DETERMINISTIC_0b5c7fb2b172f120
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Firebase Admin SDK
const admin = require('firebase-admin');

// Initialize Firebase Admin
admin.initializeApp({
  credential: admin.credential.applicationDefault(),
  storageBucket: 'YOUR_PROJECT_ID.appspot.com', // Replace with your Firebase project ID
});

// Function to upload static assets to Firebase Storage
async function uploadStaticAssets(filePath, destination) {
  try {
    // Get a reference to the storage bucket
    const bucket = admin.storage().bucket();

    // Upload the file to the specified destination
    await bucket.upload(filePath, {
      destination: destination,
      metadata: {
        cacheControl: 'public,max-age=31536000', // Set cache control for one year
      },
    });

    console.log(`File uploaded to ${destination}.`);
  } catch (error) {
    console.error('Error uploading file:', error);
  }
}

// Example usage: upload an image to Firebase Storage
uploadStaticAssets('./path/to/your/image.jpg', 'images/image.jpg');

// Function to configure Firebase Hosting
const { exec } = require('child_process');

// Function to deploy static assets using Firebase Hosting
function deployToFirebaseHosting() {
  exec('firebase deploy --only hosting', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error during deployment: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Deployment stderr: ${stderr}`);
      return;
    }
    console.log(`Deployment output: ${stdout}`);
  });
}

// Example usage: Deploy to Firebase Hosting
deployToFirebaseHosting();
```

### Instructions for Usage:
1. Replace `YOUR_PROJECT_ID` with your actual Firebase project ID.
2. Ensure you have initialized Firebase in your project and have the necessary permissions set up.
3. Adjust the file paths in `uploadStaticAssets()` according to your directory structure.
4. Run the script with Node.js to upload and deploy your assets.
5. Make sure you have Firebase CLI installed and configured for deployment.
