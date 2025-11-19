"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://social-ledger.pages.dev
Prompt: Can you provide code snippets for setting up a React app that displays a message when JavaScript is disabled?
Generated: DETERMINISTIC_13ba6e5ca8c1b738
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import ReactDOM from 'react-dom';

// Main App component
const App = () => {
  return (
    <div>
      {/* Message to be shown when JavaScript is disabled */}
      <noscript>
        <style>
          {`
            .noscript-message {
              color: red;
              font-weight: bold;
              font-size: 20px;
            }
          `}
        </style>
        <div className="noscript-message">
          JavaScript is disabled in your browser. Please enable it to view the content of this application.
        </div>
      </noscript>
      <div>
        {/* Main application content goes here */}
        <h1>Welcome to My React App</h1>
        <p>This is a sample application demonstrating a noscript message.</p>
      </div>
    </div>
  );
};

// Render the App component into the root element
const rootElement = document.getElementById('root');
if (rootElement) {
  ReactDOM.render(<App />, rootElement);
} else {
  console.error('Root element not found. Ensure there is an element with id "root" in your HTML.');
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My React App</title>
</head>
<body>
    <!-- Root element for React -->
    <div id="root"></div>
    <!-- Link to the bundled JavaScript file -->
    <script src="index.js" defer></script>
</body>
</html>
```
