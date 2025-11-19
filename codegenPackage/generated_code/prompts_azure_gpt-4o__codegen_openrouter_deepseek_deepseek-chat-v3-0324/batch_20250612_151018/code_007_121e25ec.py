"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Provide a code example for embedding JSX components into Markdown files in a Docusaurus project using MDX.
Generated: DETERMINISTIC_121e25ece9fbf096
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// mdx-component.js
import React from 'react';

/**
 * A custom JSX component to be embedded in MDX files.
 * @param {Object} props - Component props
 * @param {string} props.title - The title to display
 * @param {React.ReactNode} props.children - Child elements
 */
export const MDXComponent = ({ title, children }) => {
  return (
    <div className="mdx-component">
      <h3>{title}</h3>
      <div className="content">
        {children}
      </div>
    </div>
  );
};
```

```markdown
<!-- example.mdx -->
import { MDXComponent } from './mdx-component';

# MDX Example Page

This is a regular Markdown content.

<MDXComponent title="Embedded Component">
  This content is rendered by a JSX component embedded in Markdown.

  - List item 1
  - List item 2
</MDXComponent>

More Markdown content here.

## Another Section

<MDXComponent title="Another Component">
  You can embed as many components as you need.
</MDXComponent>
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [require('remark-mdx')],
        },
        blog: {
          remarkPlugins: [require('remark-mdx')],
        },
        pages: {
          remarkPlugins: [require('remark-mdx')],
        },
      },
    ],
  ],
  // ... rest of config
};
```
