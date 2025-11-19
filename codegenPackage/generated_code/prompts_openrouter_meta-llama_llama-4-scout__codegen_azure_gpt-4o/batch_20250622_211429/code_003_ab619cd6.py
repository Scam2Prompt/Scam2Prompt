"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Create a code example for a Docusaurus blog post that uses MDX to embed a React component.
Generated: DETERMINISTIC_ab619cd6cca6b9cc
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
title: "Embedding a React Component in Docusaurus Blog Post"
description: "Learn how to embed a React component in a Docusaurus blog post using MDX."
date: 2023-10-01
tags: [react, mdx, docusaurus]
---

import MyCustomComponent from '@site/src/components/MyCustomComponent';

# Embedding a React Component in Docusaurus Blog Post

Docusaurus supports MDX, which allows you to embed React components directly into your markdown files. Below is an example of how you can use a custom React component in your blog post.

## Example Component

Here is an example of a custom React component embedded in this blog post:

<MyCustomComponent />

## How It Works

The `MyCustomComponent` is imported at the top of this MDX file and can be used like any other JSX element. This makes it easy to integrate dynamic and interactive content into your blog posts.

---

<!-- Example React Component Code -->

```jsx
// File: src/components/MyCustomComponent.jsx

import React from 'react';

/**
 * MyCustomComponent
 * A simple React component to demonstrate embedding in MDX.
 */
const MyCustomComponent = () => {
  return (
    <div style={{ padding: '1rem', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2 style={{ color: '#0078e7' }}>Hello from MyCustomComponent!</h2>
      <p>This is a React component embedded in a Docusaurus blog post.</p>
    </div>
  );
};

export default MyCustomComponent;
```
```
