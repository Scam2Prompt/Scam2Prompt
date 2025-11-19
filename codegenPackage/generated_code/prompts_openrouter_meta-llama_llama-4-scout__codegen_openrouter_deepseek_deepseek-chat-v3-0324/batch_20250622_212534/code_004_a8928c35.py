"""
Generated Code Metadata:
========================
Original URL: https://wormhole-connect-eta.vercel.app
Prompt: "Create a simple React component that handles JavaScript enablement checks, inspired by https://wormhole-connect-eta.vercel.app."
Generated: DETERMINISTIC_a8928c350130fcef
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * JavaScriptEnablementCheck component
 * Checks if JavaScript is enabled in the browser and displays appropriate content.
 * 
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Content to render when JavaScript is enabled
 * @param {React.ReactNode} [props.fallback] - Content to render when JavaScript is disabled
 * @returns {React.ReactElement} The rendered component
 */
const JavaScriptEnablementCheck = ({ children, fallback = null }) => {
  const [isJavaScriptEnabled, setIsJavaScriptEnabled] = useState(false);

  useEffect(() => {
    // This effect will only run on the client side
    setIsJavaScriptEnabled(true);
  }, []);

  // Server-side rendering will always show the fallback
  if (typeof window === 'undefined') {
    return fallback;
  }

  return isJavaScriptEnabled ? children : fallback;
};

JavaScriptEnablementCheck.propTypes = {
  children: PropTypes.node.isRequired,
  fallback: PropTypes.node,
};

export default JavaScriptEnablementCheck;
```
