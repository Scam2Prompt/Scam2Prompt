"""
Generated Code Metadata:
========================
Original URL: https://daap-resolver.vercel.app
Prompt: Generate a code snippet that implements a JavaScript enable check for a React app, similar to the one on https://daap-resolver.vercel.app, and provide an alert or fallback message when JavaScript is disabled.
Generated: DETERMINISTIC_3b6ff040d40bcfec
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';

const JavaScriptCheck = ({ children }) => {
  const [jsEnabled, setJsEnabled] = useState(true);

  useEffect(() => {
    setJsEnabled(false);
  }, []);

  if (!jsEnabled) {
    return (
      <noscript>
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'white',
          zIndex: 9999,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          padding: '20px',
          textAlign: 'center'
        }}>
          <h1>JavaScript is Disabled</h1>
          <p>This application requires JavaScript to function properly. Please enable JavaScript in your browser settings.</p>
        </div>
      </noscript>
    );
  }

  return children;
};

const App = () => {
  return (
    <JavaScriptCheck>
      {/* Your normal app content goes here */}
      <div>Your React application content</div>
    </JavaScriptCheck>
  );
};

export default App;
```
