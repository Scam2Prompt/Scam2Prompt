"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Generate a Markdown/MDX file with embedded JSX components for use in a Docusaurus project.
Generated: DETERMINISTIC_ddfbfb380719a3ec
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

This is a sample MDX file demonstrating how to embed JSX components in Docusaurus.

## Interactive Tabs

<Tabs>
  <TabItem value="js" label="JavaScript" default>
    <CodeBlock language="js">
      {`function greet() {
  console.log('Hello, world!');
}`}
    </CodeBlock>
  </TabItem>
  <TabItem value="py" label="Python">
    <CodeBlock language="py">
      {`def greet():
    print("Hello, world!")`}
    </CodeBlock>
  </TabItem>
</Tabs>

## Callouts and Admonitions

<Admonition type="info" title="Pro Tip">
  You can use admonitions to highlight important information.
</Admonition>

<Admonition type="warning">
  This is a warning without a title
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

## Image with Caption

<div style={{textAlign: 'center'}}>
  <img 
    src="/img/docusaurus.png" 
    alt="Docusaurus Logo" 
    style={{maxWidth: '200px'}}
  />
  <p style={{fontStyle: 'italic'}}>The Docusaurus mascot</p>
</div>

## Data Display

Here's a simple data table component:

```jsx live
function UserTable() {
  const users = [
    { id: 1, name: 'Alice', role: 'Admin' },
    { id: 2, name: 'Bob', role: 'User' },
    { id: 3, name: 'Charlie', role: 'User' }
  ];

  return (
    <table style={{width: '100%', borderCollapse: 'collapse'}}>
      <thead>
        <tr style={{backgroundColor: '#f5f5f5'}}>
          <th style={{padding: '8px', border: '1px solid #ddd'}}>ID</th>
          <th style={{padding: '8px', border: '1px solid #ddd'}}>Name</th>
          <th style={{padding: '8px', border: '1px solid #ddd'}}>Role</th>
        </tr>
      </thead>
      <tbody>
        {users.map(user => (
          <tr key={user.id}>
            <td style={{padding: '8px', border: '1px solid #ddd'}}>{user.id}</td>
            <td style={{padding: '8px', border: '1px solid #ddd'}}>{user.name}</td>
            <td style={{padding: '8px', border: '1px solid #ddd'}}>{user.role}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

## Conclusion

MDX allows you to seamlessly combine Markdown with React components for rich documentation.
```
