"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-1--keen-thompson-a49324.netlify.app
Prompt: Create a React application that dynamically renders content only if JavaScript is enabled, replicating the functionality observed on the webpage at https://deploy-preview-1--keen-thompson-a49324.netlify.app.
Generated: DETERMINISTIC_4eeaad9d0f36eea0
Batch ID: 20250612_151018
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
  <title>React App with JavaScript Check</title>
  <script>
    // Add a class to the root element if JavaScript is enabled
    document.documentElement.classList.add('js-enabled');
  </script>
</head>
<body>
  <noscript>
    <!-- Message displayed if JavaScript is not enabled -->
    <div style="text-align: center; margin-top: 20px; font-size: 18px;">
      You need JavaScript enabled to view this application.
    </div>
  </noscript>
  <div id="root"></div>
</body>
</html>

// App.js
import React from 'react';

const App = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <h1>Welcome to the React Application</h1>
      <p>This content is dynamically rendered because JavaScript is enabled.</p>
    </div>
  );
};

export default App;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

// Check if JavaScript is enabled (document will have 'js-enabled' class if enabled)
if (document.documentElement.classList.contains('js-enabled')) {
  ReactDOM.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
} else {
  // Graceful fallback for environments where JavaScript is disabled
  console.error('JavaScript is not enabled. Application cannot be rendered.');
}

// package.json
{
  "name": "react-js-check-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
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
