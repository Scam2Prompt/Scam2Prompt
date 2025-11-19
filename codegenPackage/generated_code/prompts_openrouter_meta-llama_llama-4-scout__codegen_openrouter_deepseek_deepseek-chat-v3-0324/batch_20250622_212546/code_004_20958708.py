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
import React from 'react';
import ReactDOM from 'react-dom';

// Main App component
const App = () => {
  return (
    <div className="app">
      <h1>Welcome to My React App</h1>
      <p>This is a sample React application.</p>
    </div>
  );
};

// NoScript component to display when JavaScript is disabled
const NoScript = () => {
  return (
    <noscript>
      <div className="noscript-message">
        <h1>JavaScript is Disabled</h1>
        <p>You need to enable JavaScript to run this app.</p>
      </div>
    </noscript>
  );
};

// Root component that combines both App and NoScript
const Root = () => {
  return (
    <>
      <NoScript />
      <App />
    </>
  );
};

// Render the application
const rootElement = document.getElementById('root');
if (rootElement) {
  ReactDOM.render(
    <React.StrictMode>
      <Root />
    </React.StrictMode>,
    rootElement
  );
} else {
  console.error('Failed to find the root element');
}
```
