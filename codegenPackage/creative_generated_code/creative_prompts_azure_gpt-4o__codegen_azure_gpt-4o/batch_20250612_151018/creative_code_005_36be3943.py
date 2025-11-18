"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Generate a Markdown/MDX file with embedded JSX components for use in a Docusaurus documentation site.
Generated: DETERMINISTIC_36be3943b5d7d837
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
title: Example Page
description: An example MDX page with embedded JSX components for use in a Docusaurus site.
---

import React from 'react';

/**
 * CustomButton Component
 * A reusable button component.
 * Props:
 * - label {string}: Text displayed on the button
 * - onClick {function}: Function to execute on button click
 */
function CustomButton({ label, onClick }) {
  return (
    <button
      style={{
        padding: '10px 20px',
        fontSize: '16px',
        backgroundColor: '#0078D7',
        color: '#fff',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

/**
 * ExampleComponent
 * A simple React component to demonstrate embedding JSX in MDX.
 */
function ExampleComponent() {
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <div
      style={{
        border: '1px solid #ddd',
        borderRadius: '8px',
        padding: '20px',
        marginTop: '20px',
        textAlign: 'center',
      }}
    >
      <h3 style={{ color: '#333' }}>This is an example embedded React component.</h3>
      <CustomButton label="Click Me" onClick={handleClick} />
    </div>
  );
}

# Welcome to the Example Page

This page demonstrates how to embed React components into an MDX file for use in a Docusaurus documentation site.

## Static Content

Here is some static content written in Markdown. You can mix and match Markdown with JSX components seamlessly.

- Markdown bullet points
- Can be mixed with interactive React components

## Embedded React Component

Below is an interactive React component:

<ExampleComponent />

## Conclusion

MDX allows you to write documentation that combines Markdown's simplicity with React's power. This is especially useful for modern documentation sites like Docusaurus.
```
