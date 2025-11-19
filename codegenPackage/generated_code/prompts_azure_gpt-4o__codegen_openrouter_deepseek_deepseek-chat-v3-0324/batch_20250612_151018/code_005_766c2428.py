"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Provide a code example for customizing the layout of a Docusaurus site using React components while reusing the default header and footer.
Generated: DETERMINISTIC_766c2428e20a52d1
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/components/CustomLayout.js
import React from 'react';
import Head from '@docusaurus/Head';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

/**
 * Custom layout component that reuses Docusaurus default header and footer
 * while allowing custom content layout.
 * 
 * @param {Object} props - Component props
 * @param {string} props.title - Page title
 * @param {string} props.description - Page description
 * @param {React.ReactNode} props.children - Page content
 */
function CustomLayout({ title, description, children }) {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={title}
      description={description || siteConfig.tagline}
    >
      <Head>
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description || siteConfig.tagline} />
      </Head>

      <main className="custom-layout">
        <div className="container">
          {children}
        </div>
      </main>
    </Layout>
  );
}

export default CustomLayout;
```

```jsx
// src/pages/custom-page.js
import React from 'react';
import CustomLayout from '../components/CustomLayout';

/**
 * Example custom page using our CustomLayout component
 */
function CustomPage() {
  return (
    <CustomLayout
      title="Custom Page"
      description="This is a custom page layout example"
    >
      <section className="custom-content">
        <h1>Welcome to My Custom Page</h1>
        <p>This content is wrapped in a custom layout while preserving the default header and footer.</p>
      </section>
    </CustomLayout>
  );
}

export default CustomPage;
```

```css
/* src/css/custom.css */
.custom-layout {
  padding: 2rem 0;
  min-height: calc(100vh - var(--ifm-navbar-height) - var(--ifm-footer-height));
}

.custom-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Responsive adjustments */
@media (max-width: 996px) {
  .custom-layout {
    padding: 1rem 0;
  }
}
```
