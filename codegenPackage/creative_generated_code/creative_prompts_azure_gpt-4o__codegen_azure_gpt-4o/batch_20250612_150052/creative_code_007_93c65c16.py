"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-three.vercel.app
Prompt: Build a React component that displays an error message if JavaScript is not enabled, with instructions to enable it for MetaMask functionality.
Generated: DETERMINISTIC_93c65c16b4acb1cd
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';

const NoJavaScriptWarning = () => {
  return (
    <noscript>
      {/* This will only render if JavaScript is disabled */}
      <div style={styles.warningContainer}>
        <h2 style={styles.warningHeader}>JavaScript Required</h2>
        <p style={styles.warningText}>
          MetaMask functionality requires JavaScript to be enabled in your browser. 
          Please enable JavaScript and refresh the page.
        </p>
      </div>
    </noscript>
  );
};

// Inline styles for better encapsulation and ease of use
const styles = {
  warningContainer: {
    backgroundColor: '#ffcccb',
    padding: '20px',
    textAlign: 'center',
    borderRadius: '5px',
    border: '1px solid #f5c6cb',
    maxWidth: '500px',
    margin: '20px auto',
  },
  warningHeader: {
    fontSize: '18px',
    fontWeight: 'bold',
    color: '#721c24',
  },
  warningText: {
    fontSize: '16px',
    color: '#721c24',
  },
};

export default NoJavaScriptWarning;
```
