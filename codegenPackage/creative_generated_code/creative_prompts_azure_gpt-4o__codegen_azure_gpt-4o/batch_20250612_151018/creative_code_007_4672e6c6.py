"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Provide an example of embedding a JSX component into a Markdown file in a Docusaurus project.
Generated: DETERMINISTIC_4672e6c6fba43977
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: src/components/CustomButton.js
// This is a reusable JSX component that will be embedded into the Markdown file.

import React from 'react';

// A simple button component
const CustomButton = ({ label, onClick }) => {
  return (
    <button
      onClick={onClick}
      style={{
        padding: '10px 20px',
        backgroundColor: '#0078d4',
        color: '#ffffff',
        border: 'none',
        borderRadius: '5px',
        cursor: 'pointer',
      }}
    >
      {label}
    </button>
  );
};

export default CustomButton;

```

```markdown
<!-- File: docs/example.md -->
<!-- This Markdown file demonstrates embedding the CustomButton component -->

import CustomButton from '@site/src/components/CustomButton';

/# Below is an example of embedding a JSX component inside a Markdown file in a Docusaurus project. /

# Embedding JSX Components in Markdown

This is a Markdown document that demonstrates how to embed a custom React component.

## Example Button

Below is a custom button component embedded using JSX:

<CustomButton label="Click Me!" onClick={() => alert('Button clicked!')} />
```
