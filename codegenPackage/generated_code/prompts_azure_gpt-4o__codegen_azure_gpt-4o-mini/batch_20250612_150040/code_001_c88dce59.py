"""
Generated Code Metadata:
========================
Original URL: https://mammoth-ice-straight.on-fleek.app
Prompt: Create a React app setup using Create React App that includes a feature to check if JavaScript is enabled in the browser.
Generated: DETERMINISTIC_c88dce590baae7be
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Create a new React app using Create React App
npx create-react-app js-checker-app

# Step 2: Navigate into the project directory
cd js-checker-app
```

```javascript
// src/App.js

import React, { useEffect, useState } from 'react';
import './App.css';

/**
 * App component that checks if JavaScript is enabled in the browser.
 * It displays a message based on the JavaScript status.
 */
function App() {
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(false);

  useEffect(() => {
    // Set JavaScript enabled state to true when the component mounts
    setIsJavaScriptEnabled(true);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {isJavaScriptEnabled ? (
          <h1>JavaScript is enabled in your browser!</h1>
        ) : (
          <h1>JavaScript is not enabled in your browser.</h1>
        )}
      </header>
    </div>
  );
}

export default App;
```

```css
/* src/App.css */

/* Basic styling for the app */
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}
```

```html
<!-- public/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  <title>JavaScript Checker</title>
</head>
<body>
  <noscript>
    <style>
      /* Hide the app if JavaScript is disabled */
      #root {
        display: none;
      }
    </style>
    <h1>JavaScript is not enabled in your browser. Please enable it to use this application.</h1>
  </noscript>
  <div id="root"></div>
</body>
</html>
```

```bash
# Step 3: Start the development server
npm start
```

This setup creates a React application that checks if JavaScript is enabled in the browser. If JavaScript is disabled, a message will be displayed in the `<noscript>` tag in the HTML file.
