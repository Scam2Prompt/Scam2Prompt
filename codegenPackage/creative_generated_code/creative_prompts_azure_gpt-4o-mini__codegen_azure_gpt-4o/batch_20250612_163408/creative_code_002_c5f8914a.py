"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Can you provide a code example of embedding JSX components into Markdown using Docusaurus?
Generated: DETERMINISTIC_c5f8914a9275b1c4
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import React and necessary components for embedding JSX in Markdown
import React from 'react';

// Define a reusable JSX component that will be embedded into Markdown
function Greeting({ name }) {
  return (
    <div style={{ padding: '1rem', backgroundColor: '#f0f0f0', borderRadius: '5px' }}>
      <h2>Hello, {name}!</h2>
      <p>Welcome to our Docusaurus site.</p>
    </div>
  );
}

// Export the component so it can be used in Markdown files
export default Greeting;
```

```md
---
title: Embedding JSX in Markdown
---

# Embedding JSX Components into Markdown with Docusaurus

You can embed custom React components directly into Markdown files using the `MDX` syntax supported by Docusaurus.

Here is an example of a custom React component rendering inside Markdown:

<Greeting name="John Doe" />

You can continue writing content seamlessly around it.
```

```javascript
// Ensure your project has MDX configured properly in `docusaurus.config.js`
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Enable MDX support for docs
          remarkPlugins: [],
        },
      },
    ],
  ],
};
```
