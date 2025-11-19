"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components in Markdown using Docusaurus and MDX?
Generated: DETERMINISTIC_304c653badd901e0
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready example of embedding JSX components in Markdown using Docusaurus and MDX:

```jsx
// src/components/Callout.js
import React from 'react';

/**
 * A customizable callout component for MDX
 * @param {Object} props - Component props
 * @param {'info'|'warning'|'danger'|'success'} [props.type='info'] - Callout type
 * @param {string} [props.title] - Optional title
 * @param {React.ReactNode} props.children - Content
 */
export default function Callout({ type = 'info', title, children }) {
  const typeStyles = {
    info: {
      borderColor: 'blue',
      backgroundColor: 'rgba(0, 120, 255, 0.1)',
    },
    warning: {
      borderColor: 'orange',
      backgroundColor: 'rgba(255, 165, 0, 0.1)',
    },
    danger: {
      borderColor: 'red',
      backgroundColor: 'rgba(255, 0, 0, 0.1)',
    },
    success: {
      borderColor: 'green',
      backgroundColor: 'rgba(0, 255, 0, 0.1)',
    },
  };

  return (
    <div
      style={{
        borderLeft: `4px solid ${typeStyles[type].borderColor}`,
        backgroundColor: typeStyles[type].backgroundColor,
        padding: '1rem',
        margin: '1rem 0',
        borderRadius: '0 4px 4px 0',
      }}
    >
      {title && <h4 style={{ marginTop: 0 }}>{title}</h4>}
      <div>{children}</div>
    </div>
  );
}
```

```mdx
<!-- src/pages/example.mdx -->
import Callout from '../components/Callout';

# JSX in Markdown Example

This is a regular markdown paragraph.

<Callout type="info">
  This is an **info** callout with Markdown content.
</Callout>

<Callout type="warning" title="Heads up!">
  This is a warning callout with a title.
</Callout>

Here's a more complex example with JSX:

<Callout type="success">
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <span style={{ marginRight: '8px' }}>🎉</span>
    <span>Success! You've embedded JSX in MDX!</span>
  </div>
</Callout>

## Interactive Component

import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <span style={{ marginLeft: '8px' }}>Count: {count}</span>
    </div>
  );
}

<Counter />
```

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [require('rehype-katex')],
        },
        blog: {
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [require('rehype-katex')],
        },
        pages: {
          remarkPlugins: [require('remark-math')],
          rehypePlugins: [require('rehype-katex')],
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themes: ['@docusaurus/theme-mdx'],
};
```
