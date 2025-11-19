"""
Generated Code Metadata:
========================
Original URL: https://full-mint-website-master.pages.dev
Prompt: Write a basic React component that checks if JavaScript is enabled in the browser and renders a message accordingly.
Generated: DETERMINISTIC_6b70ac597435b4df
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * Component that checks if JavaScript is enabled in the browser
 * and renders a message accordingly.
 */
const JavaScriptChecker = ({ jsEnabledMessage, jsDisabledMessage }) => {
  const [isJsEnabled, setIsJsEnabled] = useState(false);

  useEffect(() => {
    // This effect will only run on the client-side
    setIsJsEnabled(true);
  }, []);

  return (
    <div className="javascript-checker">
      {isJsEnabled ? (
        <p className="js-enabled-message">{jsEnabledMessage}</p>
      ) : (
        <noscript>
          <p className="js-disabled-message">{jsDisabledMessage}</p>
        </noscript>
      )}
    </div>
  );
};

JavaScriptChecker.propTypes = {
  /** Message to display when JavaScript is enabled */
  jsEnabledMessage: PropTypes.string,
  /** Message to display when JavaScript is disabled */
  jsDisabledMessage: PropTypes.string,
};

JavaScriptChecker.defaultProps = {
  jsEnabledMessage: 'JavaScript is enabled in your browser.',
  jsDisabledMessage: 'JavaScript is disabled in your browser. Please enable it for full functionality.',
};

export default JavaScriptChecker;
```
