"""
Generated Code Metadata:
========================
Original URL: https://wormhole-ntt-ui.vercel.app
Prompt: Create a JavaScript function to check if JavaScript is enabled in a browser before rendering a React application, inspired by the behavior of the app at https://wormhole-ntt-ui.vercel.app.
Generated: DETERMINISTIC_6e834ef7792ccb37
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';

/**
 * Component that checks if JavaScript is enabled in the browser before rendering the app.
 * Shows a fallback message if JavaScript is disabled.
 * 
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - The main app content to render when JS is enabled
 * @param {React.ReactNode} [props.fallback] - Optional fallback content to show when JS is disabled
 * @returns {React.ReactElement} Either the children or fallback content based on JS availability
 */
const JSCheck = ({ children, fallback = null }) => {
  const [jsEnabled, setJsEnabled] = useState(false);

  useEffect(() => {
    // This effect will only run if JavaScript is enabled
    setJsEnabled(true);
  }, []);

  if (!jsEnabled) {
    return (
      fallback || (
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
            zIndex: 9999,
            padding: '20px',
            textAlign: 'center'
          }}>
            <div>
              <h1>JavaScript is disabled</h1>
              <p>This application requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
            </div>
          </div>
        </noscript>
      )
    );
  }

  return children;
};

/**
 * Main App component that wraps the application with JS check
 */
const App = () => {
  return (
    <JSCheck>
      <div className="app">
        {/* Your main app content goes here */}
        <h1>Welcome to the App</h1>
        <p>JavaScript is enabled and working!</p>
      </div>
    </JSCheck>
  );
};

export default App;
```
