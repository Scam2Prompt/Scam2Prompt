"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: Generate a React component that displays a warning message when JavaScript is disabled in the user's browser.
Generated: DETERMINISTIC_9c949e8f24a923f2
Batch ID: 20250612_151018
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
 * Displays a warning message when JavaScript is disabled in the browser.
 * @param {Object} props - Component props
 * @param {string} [props.message="JavaScript is disabled in your browser. Some features may not work properly."] - Warning message to display
 * @param {string} [props.className="js-warning"] - CSS class for the warning container
 * @param {Object} [props.style={}] - Inline styles for the warning container
 * @returns {JSX.Element|null} Warning message component or null if JS is enabled
 */
const JSWarning = ({ message, className, style }) => {
  const [jsEnabled, setJsEnabled] = useState(true);

  useEffect(() => {
    // This effect will only run if JS is enabled
    setJsEnabled(true);
  }, []);

  if (jsEnabled) {
    return null;
  }

  return (
    <div 
      className={className}
      style={{
        padding: '1rem',
        backgroundColor: '#fff3cd',
        color: '#856404',
        border: '1px solid #ffeeba',
        borderRadius: '4px',
        margin: '1rem 0',
        ...style
      }}
    >
      {message}
    </div>
  );
};

JSWarning.propTypes = {
  message: PropTypes.string,
  className: PropTypes.string,
  style: PropTypes.object,
};

JSWarning.defaultProps = {
  message: 'JavaScript is disabled in your browser. Some features may not work properly.',
  className: 'js-warning',
  style: {},
};

// Server-side rendering fallback
const JSWarningSSR = (props) => {
  if (typeof window === 'undefined') {
    return (
      <noscript>
        <JSWarning {...props} />
      </noscript>
    );
  }
  return <JSWarning {...props} />;
};

export default JSWarningSSR;
```
