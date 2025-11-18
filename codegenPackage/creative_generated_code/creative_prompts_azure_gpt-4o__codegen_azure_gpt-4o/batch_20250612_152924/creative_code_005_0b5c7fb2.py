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

```bash
# Step 1: Install Firebase CLI globally on your system
npm install -g firebase-tools

# Step 2: Login to Firebase (if you haven't already)
firebase login

# Step 3: Initialize Firebase Hosting in your project
firebase init hosting

# During initialization, you'll be prompted to:
# - Select your Firebase project
# - Define your public directory (e.g., `public`)
# - Choose whether to configure as a single-page app (default: "No")
# - Optionally set up automatic builds and deploys with GitHub

# Step 4: Add static assets (e.g., HTML, CSS, JS files) to the `public` folder
# Example structure of the `public` folder:
# public/
# ├── index.html
# ├── styles.css
# ├── app.js
# ├── images/
# │   ├── logo.png
# │   └── banner.jpg

# Step 5: Deploy your static site to Firebase Hosting
firebase deploy
```

### Example index.html file (`public/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Firebase Hosting Example</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Welcome to Firebase Hosting!</h1>
  <img src="images/logo.png" alt="Logo">
  <script src="app.js"></script>
</body>
</html>
```

### Example CSS file (`public/styles.css`)
```css
body {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 0;
  padding: 0;
}
h1 {
  color: #333;
}
```

### Example JavaScript file (`public/app.js`)
```javascript
// Log a message to the console when the page loads
console.log('Firebase Hosting is serving static assets successfully!');
```

### Firebase Hosting Configuration (`firebase.json`)
```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "headers": [
      {
        "source": "**/*.@(jpg|jpeg|gif|png|svg|webp)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      },
      {
        "source": "**/*.@(js|css)",
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000"
          }
        ]
      }
    ]
  }
}
```

### Error Handling for Missing Files
Add a `404.html` file to the `public` directory to handle missing pages.

### Example `404.html` file
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Not Found</title>
</head>
<body>
  <h1>404 - Page Not Found</h1>
  <p>Sorry, the page you are looking for does not exist.</p>
</body>
</html>
```

### Command to Deploy updates after modifying assets
```bash
firebase deploy
```

### Notes
- Firebase Hosting automatically caches assets and serves them via a CDN.
- The `Cache-Control` headers in `firebase.json` ensure proper caching of static assets.
- Use `firebase deploy` every time you update your assets to push changes to Firebase Hosting.
