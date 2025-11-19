"""
Generated Code Metadata:
========================
Original URL: https://api.socialgood-shopping.com
Prompt: Write a code snippet to verify Firebase SDK loading in a web project.
Generated: DETERMINISTIC_3dfd70f89a52348e
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * This script verifies if the Firebase SDK is properly loaded in a web project.
 * It checks for the presence of Firebase and its core services.
 */

// Wrap the verification in a function for modularity
function verifyFirebaseSDK() {
  try {
    // Check if the Firebase object exists
    if (typeof firebase === 'undefined') {
      throw new Error('Firebase SDK is not loaded. Please ensure the Firebase script is included in your project.');
    }

    // Check if Firebase core services are available
    if (!firebase.app || !firebase.apps) {
      throw new Error('Firebase core services are not initialized. Please ensure Firebase is properly configured.');
    }

    // Check if there is at least one initialized Firebase app
    if (firebase.apps.length === 0) {
      throw new Error('No Firebase app is initialized. Please initialize Firebase using firebase.initializeApp().');
    }

    // Log success message if all checks pass
    console.log('Firebase SDK is successfully loaded and initialized.');
  } catch (error) {
    // Log error message for debugging purposes
    console.error('Firebase SDK verification failed:', error.message);
  }
}

// Call the verification function
verifyFirebaseSDK();
```
