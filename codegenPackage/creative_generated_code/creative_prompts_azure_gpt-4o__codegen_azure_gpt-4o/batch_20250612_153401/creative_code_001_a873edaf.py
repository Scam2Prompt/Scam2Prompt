"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Create a simple React component that checks if JavaScript is enabled and renders a message like "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_a873edafea710abf
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';

// Define a functional component to check JavaScript support
const JavaScriptCheck = () => {
  return (
    /**
     * This component uses the "noscript" HTML tag to display a message
     * if JavaScript is disabled in the user's browser.
     */
    <div>
      {/* This message will only appear if JavaScript is disabled */}
      <noscript>
        <div style={{ color: 'red', fontSize: '18px', textAlign: 'center', padding: '20px' }}>
          You need to enable JavaScript to run this app.
        </div>
      </noscript>
    </div>
  );
};

export default JavaScriptCheck;
```
