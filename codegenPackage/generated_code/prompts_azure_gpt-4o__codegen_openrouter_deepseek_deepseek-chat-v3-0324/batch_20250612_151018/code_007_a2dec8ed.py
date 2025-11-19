"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Create a Markdown file with embedded JSX components using MDX for use in a Docusaurus project.
Generated: DETERMINISTIC_a2dec8ed57497639
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```mdx
---
title: JSX Components in Markdown
description: A sample MDX file with embedded JSX components for Docusaurus
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from '@theme/CodeBlock';
import Admonition from '@theme/Admonition';

# JSX Components in Markdown

This is a sample MDX file demonstrating how to embed JSX components in Markdown for Docusaurus.

## Interactive Components

### Tabs Component

<Tabs>
  <TabItem value="js" label="JavaScript" default>
    ```js
    console.log('Hello from JavaScript!');
    ```
  </TabItem>
  <TabItem value="py" label="Python">
    ```py
    print("Hello from Python!")
    ```
  </TabItem>
</Tabs>

### Admonition Component

<Admonition type="warning" title="Important Note">
  This is a warning message with JSX syntax. Be careful when using this feature!
</Admonition>

## Custom React Component

Here's an embedded counter component:

```jsx live
function Counter() {
  const [count, setCount] = React.useState(0);

  return (
    <div style={{padding: '1rem', border: '1px solid #ddd', borderRadius: '4px'}}>
      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}
```

## Code Blocks

<CodeBlock language="jsx">
{`function Greeting({name}) {
  return <h1>Hello, {name}!</h1>;
}`}
</CodeBlock>

## Image with Custom Styling

<div style={{textAlign: 'center'}}>
  <img 
    src="/img/docusaurus.png" 
    alt="Docusaurus Logo" 
    style={{width: '200px', borderRadius: '8px'}}
  />
  <p style={{fontSize: '0.8rem', color: '#666'}}>Docusaurus Logo</p>
</div>
```
