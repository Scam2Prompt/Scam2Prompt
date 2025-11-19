"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components in Markdown using Docusaurus and MDX?
Generated: DETERMINISTIC_304c653badd901e0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: docs/example.md

import React from 'react';

// Custom React component to be embedded in Markdown
const AlertBox = ({ type, children }) => {
  const styles = {
    info: {
      border: '1px solid #blue',
      backgroundColor: '#e7f3ff',
      color: '#004085',
      padding: '10px',
      borderRadius: '5px',
    },
    warning: {
      border: '1px solid orange',
      backgroundColor: '#fffbe6',
      color: '#856404',
      padding: '10px',
      borderRadius: '5px',
    },
    error: {
      border: '1px solid red',
      backgroundColor: '#fdecea',
      color: '#842029',
      padding: '10px',
      borderRadius: '5px',
    },
  };

  return <div style={styles[type]}>{children}</div>;
};

export default AlertBox;

```
ue);
    }
  }, []);

  if (hasError) {
    
};
}


```
