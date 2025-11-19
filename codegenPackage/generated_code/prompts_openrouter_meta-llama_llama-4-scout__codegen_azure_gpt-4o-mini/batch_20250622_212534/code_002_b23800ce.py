"""
Generated Code Metadata:
========================
Original URL: https://wormhole-connect-eta.vercel.app
Prompt: "Generate code for a basic React App that displays a 'You need to enable JavaScript to run this app' message when JavaScript is disabled."
Generated: DETERMINISTIC_b23800ce0ff38329
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Importing necessary libraries
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Importing CSS for styling

// Main App component
const App = () => {
  return (
    <div>
      <h1>Welcome to the React App!</h1>
      <p>This is a simple React application.</p>
    </div>
  );
};

// Rendering the App component into the root element
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Fallback message for when JavaScript is disabled
document.write(`
  <noscript>
    <style>
      body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin-top: 50px;
      }
      .noscript-message {
        font-size: 24px;
        color: red;
      }
    </style>
    <div class="noscript-message">
      You need to enable JavaScript to run this app.
    </div>
  </noscript>
`);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React App</title>
</head>
<body>
    <div id="root"></div>
    <script src="index.js" defer></script> <!-- Load the JavaScript file -->
</body>
</html>
```

```css
/* index.css */
/* Basic styling for the app */
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

h1 {
    color: #333;
}

p {
    color: #666;
}
```
