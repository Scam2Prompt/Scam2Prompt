"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components into Markdown using Docusaurus and MDX?
Generated: DETERMINISTIC_eb704d3ab828b0f8
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready example of embedding JSX components into Markdown using Docusaurus and MDX:

```jsx
// src/components/Callout.js
import React from 'react';

/**
 * A customizable callout component for MDX
 * @param {Object} props - Component props
 * @param {'info'|'warning'|'danger'|'success'} [props.type='info'] - Callout type
 * @param {string} [props.title] - Optional title
 * @param {React.ReactNode} props.children - Callout content
 */
export default function Callout({ type = 'info', title, children }) {
  const typeStyles = {
    info: { borderColor: 'blue', backgroundColor: 'rgba(0, 120, 255, 0.1)' },
    warning: { borderColor: 'orange', backgroundColor: 'rgba(255, 165, 0, 0.1)' },
    danger: { borderColor: 'red', backgroundColor: 'rgba(255, 0, 0, 0.1)' },
    success: { borderColor: 'green', backgroundColor: 'rgba(0, 255, 0, 0.1)' }
  };

  return (
    <div
      style={{
        borderLeft: `4px solid ${typeStyles[type].borderColor}`,
        backgroundColor: typeStyles[type].backgroundColor,
        padding: '1rem',
        margin: '1rem 0',
        borderRadius: '0 4px 4px 0'
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

# MDX with JSX Components Example

This is a regular Markdown paragraph.

<Callout type="info">
  This is an informational callout rendered with JSX in MDX.
</Callout>

## Using Props

You can customize the callout:

<Callout type="warning" title="Heads up!">
  This is a warning callout with a custom title.
</Callout>

## Mixed Content

You can **mix** Markdown _with_ JSX:

<Callout type="success">
  - List item 1
  - List item 2
  - List item 3
</Callout>

## Dynamic Content

<Callout type="danger" title="Important">
  {`Current date: ${new Date().toLocaleDateString()}`}
</Callout>
```

```js
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
          remarkPlugins: [require('mdx-mermaid')],
        },
        pages: {
          remarkPlugins: [require('mdx-mermaid')],
        },
      },
    ],
  ],
};
```
