"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Provide an example of a Markdown file with embedded JSX components for use in a Docusaurus project.
Generated: DETERMINISTIC_fdfdc9ae30e75c12
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```markdown
---
id: example-page
title: Example Page with JSX
description: A sample page that demonstrates embedding JSX components in Docusaurus.
---

# Example Page with JSX

This is a sample Markdown file with embedded JSX components to be used in a Docusaurus project.

## Regular Markdown Content

You can use regular Markdown syntax to create your content like headings, lists, tables, etc.

- Item 1
- Item 2
- Item 3

## Embedded JSX Component

Below is an example of embedding a JSX component directly within the Markdown file:

import React from 'react';

/**
 * A simple reusable button component
 */
function CustomButton({ label, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{
        padding: '10px 20px',
        backgroundColor: '#0078D7',
        color: 'white',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      {label}
    </button>
  );
}

/**
 * Handle button click events
 */
function handleClick() {
  alert('Button clicked!');
}

<CustomButton label="Click Me!" onClick={handleClick} />

## More Markdown Content

You can mix JSX components with other content seamlessly.

### Example Table:

| Name     | Age | Occupation     |
|----------|-----|----------------|
| Alice    | 25  | Software Dev   |
| Bob      | 30  | Designer       |
| Charlie  | 22  | Data Analyst   |

### Inline JSX Example

Here is another example of inline JSX:

<span style={{ color: 'green', fontWeight: 'bold' }}>This text is styled using JSX!</span>

## Conclusion

Docusaurus Markdown files make it easy to integrate React components directly into your documentation. This allows for dynamic and interactive content alongside static Markdown.
```
