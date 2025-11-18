"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a React app that displays a message like "You need to enable JavaScript to run this app" when JavaScript is disabled, inspired by the behavior of https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_fd687980ca846ccc
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary modules from React
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Importing the CSS file for styling

// Main application component
function App() {
  return (
    <div className="app">
      <h1>Welcome to the React App!</h1>
      <p>This is a simple React application demonstrating JavaScript detection.</p>
    </div>
  );
}

// Component to display when JavaScript is disabled
function NoJavaScriptMessage() {
  return (
    <div className="no-js-message">
      <h1>You need to enable JavaScript to run this app</h1>
    </div>
  );
}

// Determine if JavaScript is enabled
function isJavaScriptEnabled() {
  return true; // This function always returns true when JavaScript is enabled
}

// Render the appropriate component based on JavaScript availability
function renderApp() {
  if (isJavaScriptEnabled()) {
    // If JavaScript is enabled, render the main App component
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<App />);
  } else {
    // If JavaScript is disabled, render the NoJavaScriptMessage component
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<NoJavaScriptMessage />);
  }
}

// Execute the render function
renderApp();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React JavaScript Detection</title>
    <link rel="stylesheet" href="index.css"> <!-- Link to CSS styles -->
</head>
<body>
    <noscript>
        <style>
            /* Hide the app when JavaScript is disabled */
            .app {
                display: none;
            }
        </style>
    </noscript>
    <div id="root"></div> <!-- Root element for React -->
    <script src="index.js" defer></script> <!-- Load JavaScript file -->
</body>
</html>
```

```css
/* index.css */
/* Basic styling for the application */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

.app {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.no-js-message {
    color: red;
    text-align: center;
    margin-top: 50px;
}
```
