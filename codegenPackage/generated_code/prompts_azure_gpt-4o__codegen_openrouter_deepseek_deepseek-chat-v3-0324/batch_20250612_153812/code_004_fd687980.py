"""
Generated Code Metadata:
========================
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a React app that displays a message like "You need to enable JavaScript to run this app" when JavaScript is disabled, inspired by the behavior of https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_fd687980ca846ccc
Batch ID: 20250612_153812
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
function App() {
  return (
    <div className="app">
      <h1>Welcome to My App</h1>
      <p>This is a React application that requires JavaScript to function properly.</p>
    </div>
  );
}

// NoScript component to display when JavaScript is disabled
function NoScriptMessage() {
  return (
    <noscript>
      <div style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'white',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column',
        zIndex: 9999,
        padding: '20px',
        textAlign: 'center'
      }}>
        <h1 style={{ fontSize: '24px', marginBottom: '20px' }}>
          JavaScript is disabled
        </h1>
        <p style={{ fontSize: '16px', maxWidth: '500px' }}>
          You need to enable JavaScript to run this app.
        </p>
      </div>
    </noscript>
  );
}

// Root component that includes both the app and noscript message
function Root() {
  return (
    <>
      <NoScriptMessage />
      <App />
    </>
  );
}

// Render the app
const rootElement = document.getElementById('root');
ReactDOM.render(<Root />, rootElement);
```
