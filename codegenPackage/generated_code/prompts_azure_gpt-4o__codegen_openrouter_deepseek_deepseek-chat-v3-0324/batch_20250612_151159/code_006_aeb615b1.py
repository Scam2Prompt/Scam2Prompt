"""
Generated Code Metadata:
========================
Original URL: https://hodl-tracking.web.app
Prompt: Generate code to test the deployment of a web application on Firebase Hosting, ensuring proper loading of resources using the Firebase SDK.
Generated: DETERMINISTIC_aeb615b19d366172
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required Firebase modules
const firebase = require('firebase/app');
require('firebase/auth');
require('firebase/firestore');
require('firebase/storage');
require('firebase/functions');

// Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID",
  measurementId: "YOUR_MEASUREMENT_ID"
};

// Initialize Firebase
if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

// Test Firebase services
async function testFirebaseServices() {
  try {
    // Test Authentication
    const auth = firebase.auth();
    console.log('Firebase Auth initialized successfully');

    // Test Firestore
    const db = firebase.firestore();
    const testDoc = await db.collection('test').doc('test').get();
    console.log('Firestore connection successful:', testDoc.exists ? 'Document exists' : 'Document does not exist');

    // Test Storage
    const storage = firebase.storage();
    const storageRef = storage.ref();
    console.log('Firebase Storage initialized successfully');

    // Test Functions
    const functions = firebase.functions();
    console.log('Firebase Functions initialized successfully');

    return {
      auth: true,
      firestore: true,
      storage: true,
      functions: true
    };
  } catch (error) {
    console.error('Error testing Firebase services:', error);
    throw error;
  }
}

// Test Hosting resources
async function testHostingResources() {
  try {
    // Test loading index.html
    const indexResponse = await fetch('/');
    if (!indexResponse.ok) {
      throw new Error(`Failed to load index.html: ${indexResponse.status}`);
    }
    console.log('index.html loaded successfully');

    // Test loading main.js
    const jsResponse = await fetch('/main.js');
    if (!jsResponse.ok) {
      throw new Error(`Failed to load main.js: ${jsResponse.status}`);
    }
    console.log('main.js loaded successfully');

    // Test loading styles.css
    const cssResponse = await fetch('/styles.css');
    if (!cssResponse.ok) {
      throw new Error(`Failed to load styles.css: ${cssResponse.status}`);
    }
    console.log('styles.css loaded successfully');

    return {
      index: true,
      js: true,
      css: true
    };
  } catch (error) {
    console.error('Error testing hosting resources:', error);
    throw error;
  }
}

// Run all tests
async function runTests() {
  try {
    console.log('Starting Firebase deployment tests...');
    
    const firebaseResults = await testFirebaseServices();
    const hostingResults = await testHostingResources();
    
    console.log('All tests completed successfully:');
    console.log('Firebase Services:', firebaseResults);
    console.log('Hosting Resources:', hostingResults);
    
    return {
      success: true,
      firebase: firebaseResults,
      hosting: hostingResults
    };
  } catch (error) {
    console.error('Tests failed:', error);
    return {
      success: false,
      error: error.message
    };
  }
}

// Export for testing purposes
module.exports = {
  testFirebaseServices,
  testHostingResources,
  runTests
};

// Run tests if this is the main module
if (require.main === module) {
  runTests().then(results => {
    process.exit(results.success ? 0 : 1);
  });
}
```
