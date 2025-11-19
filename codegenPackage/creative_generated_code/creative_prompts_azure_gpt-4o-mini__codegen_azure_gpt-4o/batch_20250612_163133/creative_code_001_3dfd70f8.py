"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Write a code snippet to verify Firebase SDK loading in a web project.
Generated: DETERMINISTIC_3dfd70f89a52348e
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Firebase SDK Loading Verification Script
 * 
 * This script checks whether the Firebase SDK is properly loaded in a web project.
 * Follow best practices with error handling and informative user feedback.
 */

/**
 * Function to verify Firebase initialization in the project
 */
function verifyFirebaseSDK() {
  try {
    // Check if firebase object is available globally
    if (typeof firebase === 'undefined') {
      throw new Error('Firebase SDK not loaded. Please ensure it is included in your project.');
    }

    // Check for essential Firebase modules (e.g., firebase.app and firebase.auth)
    if (!firebase.app || !firebase.auth) {
      throw new Error(
        'Firebase modules are missing. Verify that required Firebase services are imported correctly.'
      );
    }

    // Attempt to initialize Firebase app (use your app's config)
    const firebaseConfig = {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_AUTH_DOMAIN",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_STORAGE_BUCKET",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID",
    };

    // Initialize Firebase if not already initialized
    if (!firebase.apps.length) {
      firebase.initializeApp(firebaseConfig);
      console.log('Firebase successfully initialized.');
    } else {
      console.log('Firebase app already initialized.');
    }

    // Test Firebase functionality (e.g., fetching authentication instance)
    const auth = firebase.auth();
    console.log('Firebase auth instance verified:', auth);

    console.log('Firebase SDK loading verified successfully.');
  } catch (error) {
    // Handle errors gracefully and inform the user
    console.error('Error verifying Firebase SDK:', error.message);
  }
}

// Run verification
verifyFirebaseSDK();
```
