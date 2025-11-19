"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Generate a sample code to integrate Firebase Hosting with a JavaScript application.
Generated: DETERMINISTIC_1821feabbeb64a9c
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Firebase Admin SDK
const admin = require("firebase-admin");

// Import the Firebase functions SDK
const functions = require("firebase-functions");

// Initialize the Firebase Admin SDK
admin.initializeApp();

// Create a Firestore reference for future use
const db = admin.firestore();

// Define a Cloud Function to serve your web app
exports.webApp = functions.https.onRequest((request, response) => {
  // Set the content type for the response
  response.set('Content-Type', 'text/html');

  // Serve your static HTML file
  response.sendFile(__dirname + '/public/index.html', (err) => {
    if (err) {
      console.error("Error serving file:", err);
      response.status(err.status).end();
    }
  });
});

// Example of a simple API endpoint
exports.addData = functions.https.onRequest(async (request, response) => {
  // Check if the request method is POST
  if (request.method !== 'POST') {
    return response.status(405).send('Method Not Allowed');
  }

  // Get data from the request body
  const data = request.body;

  try {
    // Add data to Firestore
    const docRef = await db.collection('samples').add(data);
    response.status(201).send(`Document added with ID: ${docRef.id}`);
  } catch (error) {
    console.error("Error adding document:", error);
    response.status(500).send('Internal Server Error');
  }
});

// Set up Firebase Hosting configuration in firebase.json
// Note: This part is generally configured using the Firebase CLI and not in code
// Here's an example configuration for firebase.json

/*
{
  "hosting": {
    "public": "public", // Directory containing static assets
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "function": "webApp" // Redirect all requests to the webApp Cloud Function
      }
    ]
  }
}
*/

// Make sure to run `firebase deploy` to deploy your app to Firebase Hosting
```
