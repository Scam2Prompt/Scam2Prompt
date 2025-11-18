"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-1--keen-thompson-a49324.netlify.app
Prompt: Write a React component that checks if JavaScript is enabled in the browser and displays a custom message if it is disabled, similar to the behavior of the webpage at https://deploy-preview-1--keen-thompson-a49324.netlify.app.
Generated: DETERMINISTIC_4650263d3292d6b4
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React from 'react';

const JavaScriptCheck = () => {
  return (
    <noscript>
      {/* If JavaScript is disabled, this message will be rendered */}
      <div style={{ 
        color: 'red', 
        fontSize: '18px', 
        textAlign: 'center', 
        padding: '20px', 
        backgroundColor: '#f8d7da', 
        border: '1px solid #f5c6cb', 
        borderRadius: '5px' 
      }}>
        JavaScript is disabled in your browser. Please enable JavaScript to view this page correctly.
      </div>
    </noscript>
  );
};

export default JavaScriptCheck;
```
