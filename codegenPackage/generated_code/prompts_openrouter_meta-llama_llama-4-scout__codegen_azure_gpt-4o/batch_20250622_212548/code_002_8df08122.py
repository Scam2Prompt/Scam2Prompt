"""
Generated Code Metadata:
========================
Original URL: https://collection-opensea-io.web.app
Prompt: "Generate a simple web page code that uses Firebase Hosting and displays a welcome message."
Generated: DETERMINISTIC_8df08122a16bb959
Batch ID: 20250622_212548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome Page</title>
  <style>
    /* Basic styling for the welcome message */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .welcome-container {
      margin-top: 20%;
    }
    h1 {
      color: #333;
    }
  </style>
</head>
<body>
  <div class="welcome-container">
    <h1>Welcome to My Firebase Hosted Web Page!</h1>
    <p>Thank you for visiting.</p>
  </div>

  <script>
    // Firebase Hosting does not require additional JavaScript for static pages.
    // If you plan to use Firebase services (e.g., Firestore, Authentication), initialize Firebase here.
    // Example Firebase initialization (commented out for this static page):
    /*
    // Import the Firebase SDKs (add Firebase scripts in the <head> section if needed)
    // Initialize Firebase
    const firebaseConfig = {
      apiKey: "YOUR_API_KEY",
      authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
      projectId: "YOUR_PROJECT_ID",
      storageBucket: "YOUR_PROJECT_ID.appspot.com",
      messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
      appId: "YOUR_APP_ID"
    };
    firebase.initializeApp(firebaseConfig);
    */
  </script>
</body>
</html>
```

### Firebase Hosting Setup Instructions:
1. Install Firebase CLI: `npm install -g firebase-tools`.
2. Login to Firebase: `firebase login`.
3. Initialize Firebase Hosting: `firebase init hosting`.
4. Deploy the web page: `firebase deploy`.

Ensure the `index.html` file is placed in the `public` directory created during Firebase initialization.
