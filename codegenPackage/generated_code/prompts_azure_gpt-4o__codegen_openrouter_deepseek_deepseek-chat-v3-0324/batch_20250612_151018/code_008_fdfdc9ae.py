"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Provide an example of a Markdown file with embedded JSX components for use in a Docusaurus project.
Generated: DETERMINISTIC_fdfdc9ae30e75c12
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
---
id: jsx-markdown-example
title: JSX in Markdown Example
sidebar_label: JSX Example
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import CodeBlock from '@theme/CodeBlock';
import Admonition from '@theme/Admonition';

# JSX Components in Markdown

This is a regular markdown paragraph. Below are embedded JSX components.

## Interactive Components

<Tabs>
  <TabItem value="js" label="JavaScript" default>
    <CodeBlock language="js">
      {`function greet(name) {
  return 'Hello ' + name;
}`}
    </CodeBlock>
  </TabItem>
  <TabItem value="py" label="Python">
    <CodeBlock language="py">
      {`def greet(name):
    return f"Hello {name}"`}
    </CodeBlock>
  </TabItem>
</Tabs>

## Callout Sections

<Admonition type="warning" title="Important Note">
  This feature is experimental. Use with caution.
</Admonition>

## Custom Component

```jsx live
function Counter() {
  const [count, setCount] = React.useState(0);
  
  return (
    <div style={{padding: '1rem', border: '1px solid #ddd'}}>
      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

## Image with Caption

<div style={{textAlign: 'center'}}>
  <img 
    src="/img/docusaurus.png" 
    alt="Docusaurus Logo" 
    width="200"
  />
  <p style={{fontStyle: 'italic'}}>Docusaurus Logo</p>
</div>

## Data Display

```jsx
const data = [
  {id: 1, name: 'Alice', age: 28},
  {id: 2, name: 'Bob', age: 32}
];

function UserTable() {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Age</th>
        </tr>
      </thead>
      <tbody>
        {data.map(user => (
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.name}</td>
            <td>{user.age}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

<Admonition type="tip">
  Remember to import any custom components you use in your JSX.
</Admonition>
```
