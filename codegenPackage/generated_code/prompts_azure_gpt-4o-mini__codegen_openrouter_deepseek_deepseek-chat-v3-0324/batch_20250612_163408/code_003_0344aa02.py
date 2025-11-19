"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Provide an example of embedding JSX components into Markdown using MDX in Docusaurus.
Generated: DETERMINISTIC_0344aa024cdcc210
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/pages/example.mdx

import React from 'react';
import MdxComponent from '../components/MdxComponent';
import Alert from '@theme/Alert';

# MDX in Docusaurus Example

This is a regular Markdown paragraph. Below we'll embed JSX components.

## Embedded JSX Component

Here's a custom React component rendered within MDX:

<MdxComponent title="Interactive Component">
  This is a child component passed as children prop.
</MdxComponent>

## Using Docusaurus Components

You can also use built-in Docusaurus components:

<Alert type="info">
  This is an info alert rendered using Docusaurus' Alert component.
</Alert>

## Dynamic Content

You can interpolate JavaScript expressions: {Math.PI.toFixed(2)}

```

```jsx
// src/components/MdxComponent.jsx
import React from 'react';
import PropTypes from 'prop-types';

/**
 * A demo component to showcase MDX integration
 * @param {Object} props - Component props
 * @param {string} props.title - The title to display
 * @param {ReactNode} props.children - Child components
 */
function MdxComponent({ title, children }) {
  return (
    <div className="mdx-component" style={{
      border: '1px solid #ddd',
      padding: '1rem',
      borderRadius: '4px',
      margin: '1rem 0'
    }}>
      <h3>{title}</h3>
      <div>{children}</div>
    </div>
  );
}

MdxComponent.propTypes = {
  title: PropTypes.string.isRequired,
  children: PropTypes.node
};

export default MdxComponent;
```

```jsx
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [require('mdx-mermaid')],
        },
        blog: {
          path: 'blog',
          routeBasePath: '/blog',
          include: ['**/*.{md,mdx}'],
          remarkPlugins: [require('mdx-mermaid')],
        },
        pages: {
          path: 'src/pages',
          include: ['**/*.{md,mdx}'],
          remarkPlugins: [require('mdx-mermaid')],
        },
      },
    ],
  ],
};
```
