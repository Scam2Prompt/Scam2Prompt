"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://housing-aj5.pages.dev
Prompt: Create a React application that displays a placeholder message like "You need to enable JavaScript to run this app" when JavaScript is disabled in the browser.
Generated: DETERMINISTIC_3d9aaef6372a6b60
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Notification</title>
    <style>
        /* Style for the placeholder message */
        .no-js-message {
            display: none; /* Hidden by default */
            font-size: 1.5em;
            text-align: center;
            margin-top: 20%;
        }
        /* Show message when JavaScript is disabled */
        .no-js .no-js-message {
            display: block; /* Show when JavaScript is disabled */
        }
    </style>
</head>
<body class="no-js">
    <div id="root"></div>
    <noscript>
        <div class="no-js-message">
            You need to enable JavaScript to run this app.
        </div>
    </noscript>
    <script>
        // Enable JavaScript by removing the "no-js" class
        document.body.classList.remove('no-js');
    </script>
</body>
</html>
```

```jsx
// App.js
import React from 'react';
import ReactDOM from 'react-dom';

// Main application component
function App() {
    return (
        <div>
            <h1>Welcome to Our App!</h1>
            <p>This application requires JavaScript to function properly.</p>
        </div>
    );
}

// Render the App component into the root element
ReactDOM.render(<App />, document.getElementById('root'));
```

```bash
# package.json
{
  "name": "js-disabled-notification",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```

```bash
# Run the following commands to set up the React app
npx create-react-app js-disabled-notification
cd js-disabled-notification
# Replace the contents of index.html and App.js with the provided code
# Then run the app
npm start
```
