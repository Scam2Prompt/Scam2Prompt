"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Write a code snippet to embed JSX components within Markdown using Docusaurus and MDX.
Generated: DETERMINISTIC_1a844d5f5439de47
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// @filename: example.mdx
import React from 'react';
import { CodeBlock } from '@docusaurus/theme-classic';

// Define a custom JSX component to be embedded in Markdown
const CustomComponent = ({ children }) => {
  return (
    <div style={{ 
      padding: '1rem',
      border: '1px solid #ddd',
      borderRadius: '4px',
      backgroundColor: '#f5f5f5',
      margin: '1rem 0'
    }}>
      {children}
    </div>
  );
};

// Markdown content with embedded JSX
# Using JSX in Markdown with MDX

This is regular Markdown content.

<CustomComponent>
  This is a **JSX component** embedded in Markdown.
  It supports all Markdown features inside!
</CustomComponent>

## Code Example

Here's an interactive code block:

<CodeBlock language="jsx">
{`// Example React component
function Hello() {
  return <h1>Hello MDX!</h1>;
}`}
</CodeBlock>

## Dynamic Content

You can even use React hooks:

<CustomComponent>
  {function Counter() {
    const [count, setCount] = React.useState(0);
    return (
      <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(c => c + 1)}>
          Increment
        </button>
      </div>
    );
  }()}
</CustomComponent>
```
