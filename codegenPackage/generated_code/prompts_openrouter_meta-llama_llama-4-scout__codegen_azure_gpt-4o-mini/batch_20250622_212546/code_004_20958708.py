"""
Generated Code Metadata:
========================
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Generate JavaScript code for a React application that displays "You need to enable JavaScript to run this app" when JavaScript is disabled
Generated: DETERMINISTIC_209587081ff12851
Batch ID: 20250622_212546
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
import ReactDOM from 'react-dom';

// Main application component
const App = () => {
  return (
    <div>
      <h1>Welcome to the React Application</h1>
      <p>This application requires JavaScript to function properly.</p>
    </div>
  );
};

// Fallback component for when JavaScript is disabled
const NoJavaScript = () => {
  return (
    <div>
      <h1>You need to enable JavaScript to run this app</h1>
    </div>
  );
};

// Rendering the application
const rootElement = document.getElementById('root');

// Check if JavaScript is enabled by rendering the App component
if (rootElement) {
  ReactDOM.render(<App />, rootElement);
} else {
  // If JavaScript is disabled, show the NoJavaScript component
  document.body.innerHTML = '<div id="no-js"></div>';
  const noJsElement = document.getElementById('no-js');
  ReactDOM.render(<NoJavaScript />, noJsElement);
}
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
    <script src="path/to/your/bundled/javascript.js"></script>
</body>
</html>
```

```css
/* styles.css */
/* Add any necessary styles here */
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 20px;
}
``` 

Make sure to replace `path/to/your/bundled/javascript.js` with the actual path to your bundled JavaScript file.
