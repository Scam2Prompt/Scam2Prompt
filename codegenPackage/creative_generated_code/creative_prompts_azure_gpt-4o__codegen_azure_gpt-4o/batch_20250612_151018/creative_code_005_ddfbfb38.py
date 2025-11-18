"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Generate a Markdown/MDX file with embedded JSX components for use in a Docusaurus project.
Generated: DETERMINISTIC_ddfbfb380719a3ec
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
id: example-page
title: Example Page
description: A Markdown/MDX file with embedded JSX components for a Docusaurus project.
---

# Example Page

Welcome to the example page! This is a demonstration of using MDX with embedded JSX components in a Docusaurus project.

## Static Content

This is a regular Markdown section with static content.

### Embedded JSX Components

Here is a dynamic component embedded within the page.

import React from 'react';

/**
 * A simple React component for demonstration purposes.
 */
function Greeting({ name }) {
  return <p>Hello, {name}! Welcome to the MDX page.</p>;
}

/**
 * Another example component for demonstration.
 */
function Counter() {
  const [count, setCount] = React.useState(0);

  const handleIncrement = () => setCount(count + 1);
  const handleDecrement = () => setCount(count - 1);

  return (
    <div>
      <p>Current Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
      <button onClick={handleDecrement}>Decrement</button>
    </div>
  );
}

// Render custom components inline in the MDX content
<Greeting name="Docusaurus User" />
<Counter />

## Conclusion

This page demonstrates how to mix Markdown content with interactive JSX components in a Docusaurus MDX file.

```
