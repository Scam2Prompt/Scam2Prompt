"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Generate code to embed a JSX component into a Markdown file in a Docusaurus project using MDX.
Generated: DETERMINISTIC_28eafc32f3d3e00a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/components/EmbeddedComponent.jsx
import React from 'react';

/**
 * A sample component to be embedded in MDX
 * @param {Object} props - Component props
 * @param {string} props.title - Title to display
 * @param {string} props.description - Description text
 * @returns {JSX.Element} The rendered component
 */
const EmbeddedComponent = ({ title = 'Default Title', description = 'Default description' }) => {
  return (
    <div className="embedded-component" style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '16px',
      margin: '16px 0',
      backgroundColor: '#f9f9f9'
    }}>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
};

export default EmbeddedComponent;
```

```mdx
---
title: MDX with Embedded Component
---

import EmbeddedComponent from '@site/src/components/EmbeddedComponent';

# MDX Page with Embedded Component

This is a regular Markdown content.

<EmbeddedComponent 
  title="Custom Title" 
  description="This component is embedded in MDX using JSX syntax."
/>

More Markdown content here.

## Another Section

You can use the component multiple times:

<EmbeddedComponent 
  title="Second Instance" 
  description="This shows the component can be reused."
/>
```
