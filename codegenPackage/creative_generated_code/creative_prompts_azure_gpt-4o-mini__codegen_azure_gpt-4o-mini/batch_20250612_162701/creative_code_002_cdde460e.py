"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Can you provide code examples for setting up a React app that displays a message when JavaScript is disabled?
Generated: DETERMINISTIC_cdde460e0af26efc
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Create a new React app using Create React App
// Run the following command in your terminal to set it up:
// npx create-react-app my-app

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

// Component to display when JavaScript is enabled
const App = () => {
  return (
    <div>
      <h1>JavaScript is Enabled</h1>
      <p>Welcome to our React application!</p>
    </div>
  );
};

// Fallback message for when JavaScript is disabled
const NoJavaScript = () => {
  return (
    <noscript>
      <style>
        {`body {
          background-color: #f8d7da;
          color: #721c24;
          font-family: Arial, sans-serif;
          text-align: center;
          padding: 50px;
        }`}
      </style>
      <h1>JavaScript is Disabled</h1>
      <p>This application requires JavaScript to function properly.</p>
    </noscript>
  );
};

// Main rendering function
const renderApp = () => {
  ReactDOM.render(
    <React.StrictMode>
      <NoJavaScript />
      <App />
    </React.StrictMode>,
    document.getElementById('root')
  );
};

// Error handling
try {
  renderApp();
} catch (error) {
  console.error('Error rendering the React application:', error);
}
```

Ensure that you wrap the `App` component in a `noscript` tag to display the no-JS message properly when JavaScript is disabled.
