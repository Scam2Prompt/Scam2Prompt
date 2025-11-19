"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Write a code snippet to embed JSX components within Markdown using Docusaurus and MDX.
Generated: DETERMINISTIC_1a844d5f5439de47
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary components and modules
import React from 'react';
import { useColorMode } from '@docusaurus/theme-common';

// Define a custom JSX component
const Greeting = ({ name }) => {
  const { colorMode } = useColorMode(); // Access Docusaurus color mode (light/dark)
  return (
    <div
      style={{
        padding: '1rem',
        borderRadius: '8px',
        backgroundColor: colorMode === 'dark' ? '#333' : '#f9f9f9',
        color: colorMode === 'dark' ? '#fff' : '#000',
      }}
    >
      <h2>Hello, {name}!</h2>
      <p>Welcome to our Docusaurus-powered website.</p>
    </div>
  );
};

// Export the component to be used within MDX
export default Greeting;
```

```md
<!-- Example MDX file embedding the JSX component -->

# Welcome to My Docusaurus Site

This is a simple Markdown page demonstrating how to embed a JSX component.

<Greeting name="Docusaurus User" />

You can mix Markdown content with React components seamlessly using MDX.
```
