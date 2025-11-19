"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Can you provide an example of embedding JSX components in Markdown using Docusaurus?
Generated: DETERMINISTIC_2d4827b9929e32e6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready example of embedding JSX components in Markdown using Docusaurus:

```markdown
---
title: JSX in Markdown Example
---

# JSX Components in Markdown

This is a regular Markdown paragraph.

## Embedding a React Component

Here's a simple counter component embedded in Markdown:

```jsx live
function Counter() {
  const [count, setCount] = React.useState(0);

  return (
    <div style={{ padding: '1rem', border: '1px solid #ddd', borderRadius: '4px' }}>
      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(0)} disabled={count === 0}>
        Reset
      </button>
    </div>
  );
}
```

## Using MDX Components

You can also use imported components:

```jsx
import TabItem from '@theme/TabItem';
import Tabs from '@theme/Tabs';

<Tabs>
  <TabItem value="first" label="First Tab">
    Content for first tab
  </TabItem>
  <TabItem value="second" label="Second Tab">
    Content for second tab
  </TabItem>
</Tabs>
```

## Inline JSX

You can use JSX inline: <span style={{ color: 'red' }}>This text is red</span>.
```
   [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [
            // Add support for MDX (which allows JSX in Markdown)
            require('remark-mdx')
          ],
        },
      },
    ],
  ],
};
```

```json
// package.json (relevant dependencies)
{
  "dependencies": {
    "@docusaurus/core": "^2.0.0",
    "@docusaurus/preset-classic": "^2.0.0",
    "remark-mdx": "^1.6.22",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  }
}
```
