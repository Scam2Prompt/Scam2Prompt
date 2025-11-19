"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: How can I customize the layout of my Docusaurus project while reusing the same header and footer?
Generated: DETERMINISTIC_33f1e865aceddc33
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready solution to customize layouts in Docusaurus while reusing the same header and footer:

```javascript
// src/components/CustomLayout.js
import React from 'react';
import Layout from '@theme/Layout';

/**
 * CustomLayout component that reuses Docusaurus header and footer
 * while allowing custom content layout.
 * 
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - The content to render
 * @param {string} [props.title] - Page title
 * @param {string} [props.description] - Page description
 * @returns {React.Element} The custom layout component
 */
function CustomLayout({ children, title = '', description = '' }) {
  return (
    <Layout title={title} description={description}>
      <main className="custom-layout">
        {children}
      </main>
    </Layout>
  );
}

export default CustomLayout;
```

```javascript
// src/pages/custom-page.js
import React from 'react';
import CustomLayout from '../components/CustomLayout';

/**
 * Example custom page using the reusable layout
 */
export default function CustomPage() {
  return (
    <CustomLayout 
      title="Custom Page" 
      description="This is a custom page layout"
    >
      <div className="container">
        <h1>Custom Content</h1>
        <p>This page uses the standard header/footer but custom layout.</p>
      </div>
    </CustomLayout>
  );
}
```

```css
/* src/css/custom.css */
.custom-layout {
  padding: 2rem 0;
  max-width: 1200px;
  margin: 0 auto;
}

.custom-layout .container {
  padding: 0 1rem;
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        // ... other docs config ...
      },
    ],
    [
      '@docusaurus/plugin-content-blog',
      {
        // ... other blog config ...
      },
    ],
    [
      '@docusaurus/plugin-content-pages',
      {
        // ... other pages config ...
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
