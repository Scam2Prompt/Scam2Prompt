"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2728--docusaurus-2.netlify.app
Prompt: Develop a code snippet for embedding a custom React component into a Docusaurus Markdown page.
Generated: DETERMINISTIC_5230024d9c447bc3
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// MyComponent.js
import React from 'react';

/**
 * A custom React component to be embedded in a Docusaurus Markdown page.
 * @returns {JSX.Element} The custom component.
 */
function MyComponent() {
  return (
    <div>
      <h2>My Custom Component</h2>
      <p>This is a custom React component embedded in a Docusaurus Markdown page.</p>
    </div>
  );
}

export default MyComponent;
```

```markdown
// my-page.md
import MyComponent from '@site/src/components/MyComponent';

## My Page

<MyComponent />
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configurations ...
  plugins: [
    [
      '@docusaurus/plugin-content-pages',
      {
        // ... other configurations ...
        include: ['src/pages/**/*.md'],
      },
    ],
  ],
  webpack: {
    // Allow importing React components from @site
    resolve: {
      alias: {
        '@site': path.resolve(__dirname, 'src'),
      },
    },
  },
};
```

```javascript
// src/pages/my-page.js (optional, for client-side rendering)
// Not needed if using MDX
import React from 'react';
import MyComponent from '@site/src/components/MyComponent';

function MyPage() {
  return (
    <div>
      <h1>My Page</h1>
      <MyComponent />
    </div>
  );
}

export default MyPage;
```

```bash
# For MDX support
npm install @mdx-js/react @mdx-js/loader
```

```javascript
// For MDX support in docusaurus.config.js
module.exports = {
  // ... other configurations ...
  markdown: {
    mdxExtensions: ['mdx'],
  },
};
```
