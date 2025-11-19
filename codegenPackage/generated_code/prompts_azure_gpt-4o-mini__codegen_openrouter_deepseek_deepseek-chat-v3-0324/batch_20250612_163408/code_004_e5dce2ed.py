"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: What are the steps to customize the layout of a Docusaurus site while maintaining the same header and footer?
Generated: DETERMINISTIC_e5dce2ed7b4809e2
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready code example for customizing a Docusaurus layout while preserving the header and footer:

```javascript
// src/theme/Layout.js
import React from 'react';
import Layout from '@theme-original/Layout';
import Head from '@docusaurus/Head';

export default function LayoutWrapper(props) {
  return (
    <>
      <Head>
        {/* Custom meta tags for your layout */}
        <meta property="og:type" content="website" />
      </Head>
      
      <Layout {...props}>
        {/* Wrap children in custom container while preserving header/footer */}
        <div className="custom-layout-container">
          {props.children}
        </div>
      </Layout>
    </>
  );
}
```

```css
/* src/css/custom.css */
.custom-layout-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Custom styling that won't affect header/footer */
.custom-layout-container h1 {
  color: var(--ifm-color-primary);
}

/* Mobile responsiveness */
@media (max-width: 996px) {
  .custom-layout-container {
    padding: 1rem;
  }
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  themeConfig: {
    // ... existing theme config ...
  },
  plugins: [
    // ... other plugins ...
  ],
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

```javascript
// src/pages/index.js
import React from 'react';
import Layout from '@theme/Layout';

function Home() {
  return (
    <Layout
      title="Custom Page Title"
      description="Custom page description"
    >
      <div className="custom-page-content">
        <h1>Custom Page Content</h1>
        {/* Your custom content here */}
      </div>
    </Layout>
  );
}

export default Home;
```
