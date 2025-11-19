"""
Generated Code Metadata:
========================
Original URL: https://jupiter-5g4.pages.dev
Prompt: "Write a simple React component that displays a 'You need to enable JavaScript to run this app' message when JavaScript is disabled."
Generated: DETERMINISTIC_7f5791f1b985f868
Batch ID: 20250622_211241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';

/**
 * A component that displays a message when JavaScript is disabled in the browser.
 * The message is hidden by default and only shown if JavaScript is disabled.
 */
const NoScriptMessage = () => {
  const [jsEnabled, setJsEnabled] = useState(true);

  useEffect(() => {
    // This effect runs only on the client side after the component mounts
    setJsEnabled(false);
  }, []);

  // If JavaScript is enabled, render nothing
  if (jsEnabled) {
    return null;
  }

  // Render the message if JavaScript is disabled
  return (
    <noscript>
      <div
        style={{
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
          textAlign: 'center',
        }}
      >
        <h1>You need to enable JavaScript to run this app.</h1>
      </div>
    </noscript>
  );
};

export default NoScriptMessage;
```
