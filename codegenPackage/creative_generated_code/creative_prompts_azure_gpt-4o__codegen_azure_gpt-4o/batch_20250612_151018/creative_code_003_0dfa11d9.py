"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Provide an example of embedding JSX components into Markdown files using Docusaurus and MDX.
Generated: DETERMINISTIC_0dfa11d9c20cb89e
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: /src/pages/ExamplePage.mdx

import React from 'react';

// Example of a reusable JSX component
const CustomAlert = ({ type = 'info', children }) => {
  const getAlertStyle = (type) => {
    switch (type) {
      case 'success':
        return { backgroundColor: '#d4edda', color: '#155724', padding: '10px', borderRadius: '5px' };
      case 'error':
        return { backgroundColor: '#f8d7da', color: '#721c24', padding: '10px', borderRadius: '5px' };
      case 'info':
      default:
        return { backgroundColor: '#d1ecf1', color: '#0c5460', padding: '10px', borderRadius: '5px' };
    }
  };

  return <div style={getAlertStyle(type)}>{children}</div>;
};

// Markdown content with embedded JSX components
export default function ExamplePage() {
  return (
    <>
      {/* Markdown content */}
      <h1>Welcome to the Example Page!</h1>
      <p>This page demonstrates embedding JSX components into Markdown files using MDX.</p>

      {/* JSX Component Usage */}
      <CustomAlert type="info">
        This is an informational alert. You can use JSX components like this inside MDX files.
      </CustomAlert>

      <CustomAlert type="success">
        Hooray! You successfully embedded a JSX component within Markdown.
      </CustomAlert>

      <CustomAlert type="error">
        Oops! Something went wrong. But don't worry, error alerts are here to save the day.
      </CustomAlert>

      {/* More Markdown content */}
      <p>With Docusaurus and MDX, combining Markdown and JSX becomes seamless. Enjoy crafting flexible documentation!</p>
    </>
  );
}
```
