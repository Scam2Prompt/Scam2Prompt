"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Write a Markdown/MDX code snippet for a Docusaurus documentation page that includes a JSX component.
Generated: DETERMINISTIC_9c1b79157942e380
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```mdx
---
title: JSX Component Example
description: A documentation page demonstrating JSX component usage in MDX
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import React from 'react';

// Custom JSX component for demonstration
function Counter({ initialCount = 0 }) {
  const [count, setCount] = React.useState(initialCount);

  const increment = () => setCount(c => c + 1);
  const decrement = () => setCount(c => c - 1);
  const reset = () => setCount(initialCount);

  return (
    <div style={{ padding: '1rem', border: '1px solid #ddd', borderRadius: '4px' }}>
      <h3>Current Count: {count}</h3>
      <div style={{ display: 'flex', gap: '0.5rem' }}>
        <button onClick={increment}>Increment</button>
        <button onClick={decrement}>Decrement</button>
        <button onClick={reset}>Reset</button>
      </div>
    </div>
  );
}

## JSX Component Example

This page demonstrates how to use JSX components within MDX.

### Basic Usage

Embed the component directly in your markdown:

<Counter initialCount={5} />

### With Tabs

<Tabs>
  <TabItem value="demo" label="Demo" default>
    <Counter initialCount={10} />
  </TabItem>
  <TabItem value="code" label="Code">
    ```jsx
    function Counter({ initialCount = 0 }) {
      const [count, setCount] = React.useState(initialCount);
    
      const increment = () => setCount(c => c + 1);
      const decrement = () => setCount(c => c - 1);
      const reset = () => setCount(initialCount);
    
      return (
        <div style={{ padding: '1rem', border: '1px solid #ddd' }}>
          <h3>Current Count: {count}</h3>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button onClick={increment}>Increment</button>
            <button onClick={decrement}>Decrement</button>
            <button onClick={reset}>Reset</button>
          </div>
        </div>
      );
    }
    ```
  </TabItem>
</Tabs>
```
ned within the MDX file
- Style props use the JavaScript object syntax (e.g., `style={{ color: 'red' }}`)
```
r enables interactive components
- Tabs help organize multiple code examples
```
ment</button>
        </div>
      );
    };
    ```
  </TabItem>
</Tabs>

## Notes

- JSX components must be imported or defined in the MDX file
- You can use any React hooks in your components
- Style props can be passed directly or using CSS modules
```


- Ensure you have `@docusaurus/theme-live-codeblock` installed for live code examples
- JSX components must be imported at the top of the MDX file
- Style props can be passed directly or via CSS modules
```
