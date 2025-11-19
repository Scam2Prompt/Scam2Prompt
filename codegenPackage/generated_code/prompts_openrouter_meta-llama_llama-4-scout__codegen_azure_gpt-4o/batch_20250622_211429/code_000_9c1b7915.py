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
title: Example Page
description: This is an example page with a JSX component.
---

import React from 'react';

/**
 * A simple React component to display a greeting message.
 * Props:
 * - name (string): The name to display in the greeting.
 */
function Greeting({ name }) {
  if (!name) {
    // Handle missing name prop gracefully
    return <p>Error: Name is required.</p>;
  }

  return <p>Hello, {name}! Welcome to the documentation.</p>;
}

# Example Page

This is an example page that demonstrates how to include a JSX component in a Docusaurus Markdown/MDX file.

## Greeting Component

Below is an example of the `Greeting` component in action:

<Greeting name="Docusaurus User" />

## Code Explanation

The `Greeting` component is a simple React component that accepts a `name` prop and displays a personalized greeting message. If the `name` prop is missing, it will display an error message instead.
```
age. If the `name` prop is missing, it will display an error message instead.
```
   return <p>Error: Name is required!</p>;
  }

  return <p>Hello, {name}! Welcome to the documentation.</p>;
}
```

You can use this component in your MDX files by importing it and embedding it directly in the content.
```
ng it and embedding it directly in the content.
```
