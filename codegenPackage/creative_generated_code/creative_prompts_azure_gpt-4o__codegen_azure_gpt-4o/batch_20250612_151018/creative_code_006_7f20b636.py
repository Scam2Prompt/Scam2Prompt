"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Create a Docusaurus blog post using MDX that includes embedded JSX components.
Generated: DETERMINISTIC_7f20b6360174764c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```mdx
---
title: "Creating Dynamic Content with MDX in Docusaurus"
description: "Learn how to embed JSX components in your Docusaurus blog posts using MDX."
date: "2023-10-05"
tags: ["Docusaurus", "MDX", "React"]
authors: ["John Doe"]
---

import React from 'react';

/**
 * Example React component to be embedded into the blog post.
 * This demonstrates how custom JSX components can be used in MDX.
 */
function Greeting({ name }) {
  return (
    <div style={{ padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px' }}>
      <h3>Hello, {name}!</h3>
      <p>Welcome to learning MDX in Docusaurus.</p>
    </div>
  );
}

/**
 * Another example component to demonstrate interactivity in the blog post.
 */
function Counter() {
  const [count, setCount] = React.useState(0);

  const handleIncrement = () => {
    setCount((prevCount) => prevCount + 1);
  };

  const handleDecrement = () => {
    setCount((prevCount) => Math.max(prevCount - 1, 0));
  };

  return (
    <div style={{ marginTop: '20px', padding: '10px', border: '1px solid #ddd', borderRadius: '5px' }}>
      <h4>Interactive Counter</h4>
      <p>Current Count: {count}</p>
      <button onClick={handleIncrement} style={{ marginRight: '10px' }}>Increase</button>
      <button onClick={handleDecrement}>Decrease</button>
    </div>
  );
}

# Welcome to MDX in Docusaurus!

MDX allows you to combine Markdown with React components seamlessly, enabling you to create dynamic and interactive content in your documentation or blog posts.

## Example: Using JSX Components in MDX

You can embed custom React components directly into your MDX files. Below is an example of a greeting component:

<Greeting name="Developer" />

This component is defined in the MDX file itself and is rendered dynamically.

## Adding Interactivity

MDX also supports interactive components like counters, forms, or charts. Check out the counter example below:

<Counter />

## Conclusion

MDX in Docusaurus is powerful and flexible, allowing you to blend Markdown content with React components effortlessly. This makes it ideal for creating rich, dynamic, and engaging blogs or documentation pages.

```
