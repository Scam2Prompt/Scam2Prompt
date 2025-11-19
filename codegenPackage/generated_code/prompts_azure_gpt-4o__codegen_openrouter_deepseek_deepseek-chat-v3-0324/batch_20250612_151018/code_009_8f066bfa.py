"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Provide a step-by-step example of embedding JSX components into Markdown files using MDX in Docusaurus.
Generated: DETERMINISTIC_8f066bfab16fadd5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// 1. Install required dependencies
// Run in your project directory:
// npm install @mdx-js/loader @mdx-js/react

// 2. Configure Docusaurus to handle MDX files
// In your docusaurus.config.js
module.exports = {
  // ... other config
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [require('mdx-mermaid')],
        },
        blog: {
          remarkPlugins: [require('mdx-mermaid')],
        },
        pages: {
          remarkPlugins: [require('mdx-mermaid')],
        },
      },
    ],
  ],
};

// 3. Create a custom React component to embed
// src/components/Hello.js
import React from 'react';

function Hello({name}) {
  return <div style={{border: '1px solid #ddd', padding: '1rem', borderRadius: '4px'}}>
    Hello, {name}!
  </div>;
}

export default Hello;

// 4. Create an MDX file that uses the component
// docs/example.mdx
---
title: MDX Example
---

import Hello from '../src/components/Hello';

# MDX in Docusaurus

This is a regular markdown paragraph.

<Hello name="World" />

Here's some more markdown content.

```jsx
<Hello name="from code block" />
```

// 5. (Optional) Add MDXProvider for custom components
// src/theme/MDXComponents.js
import React from 'react';
import Hello from '../components/Hello';

const MDXComponents = {
  Hello,
  // Add other components here
};

export default MDXComponents;

// 6. Wrap your app with MDXProvider
// src/theme/Layout.js
import React from 'react';
import {MDXProvider} from '@mdx-js/react';
import MDXComponents from './MDXComponents';

export default function Layout(props) {
  return (
    <MDXProvider components={MDXComponents}>
      {/* Your existing layout components */}
      {props.children}
    </MDXProvider>
  );
}

// 7. (Optional) Add TypeScript support
// Add to your tsconfig.json
{
  "compilerOptions": {
    "jsx": "react-jsx"
  }
}

// 8. (Optional) Add custom remark/rehype plugins
// docusaurus.config.js
module.exports = {
  // ... other config
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [
            require('remark-math'),
            require('mdx-mermaid')
          ],
          rehypePlugins: [require('rehype-katex')],
        },
      },
    ],
  ],
};
```
