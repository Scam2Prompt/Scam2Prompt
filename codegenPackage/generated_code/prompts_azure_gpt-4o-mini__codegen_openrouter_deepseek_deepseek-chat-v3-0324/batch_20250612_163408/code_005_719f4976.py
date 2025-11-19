"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: How can I customize the layout of my Docusaurus site while reusing the same header and footer?
Generated: DETERMINISTIC_719f49769fab574f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready solution for customizing Docusaurus layouts while reusing headers and footers:

```jsx
// src/components/CustomLayout.js
import React from 'react';
import Head from '@docusaurus/Head';
import Layout from '@theme/Layout';

/**
 * CustomLayout component that reuses Docusaurus header and footer
 * while allowing custom content layout.
 * 
 * @param {Object} props - Component props
 * @param {string} props.title - Page title
 * @param {string} props.description - Page description
 * @param {React.ReactNode} props.children - Page content
 * @returns {JSX.Element} Custom layout component
 */
export default function CustomLayout({ title, description, children }) {
  return (
    <Layout title={title} description={description}>
      <Head>
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description} />
      </Head>
      
      <main className="custom-layout">
        <div className="container">
          {children}
        </div>
      </main>
    </Layout>
  );
}
```

```css
/* src/css/custom.css */
.custom-layout {
  padding: 2rem 0;
}

.custom-layout .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}
```

```jsx
// Example usage in a page component
import React from 'react';
import CustomLayout from '../components/CustomLayout';

export default function CustomPage() {
  return (
    <CustomLayout
      title="Custom Page"
      description="This is a custom page layout"
    >
      <h1>My Custom Content</h1>
      <p>This content appears within the custom layout while maintaining the site header and footer.</p>
    </CustomLayout>
  );
}
```

```js
// docusaurus.config.js - Add the custom CSS
module.exports = {
  // ... other config
  stylesheets: [
    './src/css/custom.css',
  ],
};
```
ting config ...
  plugins: [
    // ... other plugins ...
    [
      '@docusaurus/plugin-content-pages',
      {
        path: 'src/pages',
        routeBasePath: '/',
        include: ['**/*.{js,jsx,ts,tsx}'],
      },
    ],
  ],
  themes: [
    // ... other themes ...
    [
      '@docusaurus/theme-classic',
      {
        customCss: require.resolve('./src/css/custom.css'),
      },
    ],
  ],
};
```
 box-shadow: var(--ifm-global-shadow-lw);
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config
  stylesheets: [
    // ... other stylesheets
    './src/css/custom.css',
  ],
  // ... rest of config
};
```
