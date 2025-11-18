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

```javascript
import React, { useEffect, useState } from 'react';

/**
 * JavaScriptCheck component checks if JavaScript is enabled.
 * If JavaScript is disabled, it will render a message prompting the user to enable it.
 */
const JavaScriptCheck = () => {
  // State to track if JavaScript is enabled
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(false);

  useEffect(() => {
    // Use a timeout to simulate a check for JavaScript
    const timer = setTimeout(() => {
      setIsJavaScriptEnabled(true); // Set to true if JavaScript is enabled
    }, 100); // Set a short delay

    // Cleanup function to clear the timeout
    return () => clearTimeout(timer);
  }, []);

  // Render message based on the JavaScript enabled state
  return isJavaScriptEnabled ? (
    <div>Your JavaScript is enabled.</div>
  ) : (
    <noscript>
      <div style={{ color: 'red' }}>
        You need to enable JavaScript to run this app.
      </div>
    </noscript>
  );
};

export default JavaScriptCheck;
```

### Usage
To use this component, simply import it and include it in your JSX:

```javascript
import React from 'react';
import JavaScriptCheck from './JavaScriptCheck';

const App = () => (
  <div>
    <JavaScriptCheck />
    {/* Other components can go here */}
  </div>
);

export default App;
```
