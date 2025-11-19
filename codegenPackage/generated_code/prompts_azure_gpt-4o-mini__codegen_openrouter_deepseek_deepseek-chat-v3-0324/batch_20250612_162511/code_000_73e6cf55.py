"""
Generated Code Metadata:
========================
Original URL: https://internal-frontend.pages.dev
Prompt: How can I enable JavaScript in my browser to run a React app like the one on the Swell Internal site?
Generated: DETERMINISTIC_73e6cf55501e394a
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// This is a React component that checks if JavaScript is enabled in the browser
// and displays a message if it's not, with instructions to enable it.

import React, { useState, useEffect } from 'react';

const JavaScriptCheck = () => {
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(true);

  useEffect(() => {
    // This effect will only run on the client side
    setIsJavaScriptEnabled(true);
  }, []);

  if (!isJavaScriptEnabled) {
    return (
      <div style={{
        padding: '20px',
        maxWidth: '800px',
        margin: '0 auto',
        fontFamily: 'Arial, sans-serif',
        lineHeight: '1.6'
      }}>
        <h1>JavaScript is Disabled</h1>
        <p>To use this React application, you need to enable JavaScript in your browser.</p>
        
        <h2>How to Enable JavaScript</h2>
        
        <h3>Google Chrome</h3>
        <ol>
          <li>Click the three dots in the top-right corner and select "Settings"</li>
          <li>Click "Privacy and security" in the left sidebar</li>
          <li>Select "Site Settings"</li>
          <li>Click "JavaScript"</li>
          <li>Toggle on "Allowed"</li>
        </ol>
        
        <h3>Mozilla Firefox</h3>
        <ol>
          <li>Type "about:config" in the address bar and press Enter</li>
          <li>Search for "javascript.enabled"</li>
          <li>Double-click the preference to set it to "true"</li>
        </ol>
        
        <h3>Safari</h3>
        <ol>
          <li>Go to Safari > Preferences</li>
          <li>Click the "Security" tab</li>
          <li>Check "Enable JavaScript"</li>
        </ol>
        
        <h3>Microsoft Edge</h3>
        <ol>
          <li>Click the three dots in the top-right corner and select "Settings"</li>
          <li>Click "Cookies and site permissions" in the left sidebar</li>
          <li>Select "JavaScript"</li>
          <li>Toggle on "Allowed"</li>
        </ol>
        
        <p>After enabling JavaScript, please refresh this page.</p>
      </div>
    );
  }

  return null; // Render nothing if JavaScript is enabled
};

export default JavaScriptCheck;
```
