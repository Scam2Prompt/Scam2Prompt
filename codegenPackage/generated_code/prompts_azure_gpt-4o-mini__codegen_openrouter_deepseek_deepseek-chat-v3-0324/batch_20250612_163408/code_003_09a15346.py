"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: How do I customize the layout of my Docusaurus site while reusing the same header and footer components?
Generated: DETERMINISTIC_09a15346ca71069f
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready solution for customizing Docusaurus layouts while reusing header and footer components:

```javascript
// src/components/CustomLayout.js
import React from 'react';
import Head from '@docusaurus/Head';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Footer from '@theme/Footer';

function CustomLayout({children, title, description}) {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={title}
      description={description || siteConfig.tagline}>
      <Head>
        <meta property="og:title" content={title} />
        <meta property="og:description" content={description || siteConfig.tagline} />
      </Head>
      <main className="custom-main">
        {children}
      </main>
      <Footer />
    </Layout>
  );
}

export default CustomLayout;
```

```javascript
// src/pages/custom-page.js
import React from 'react';
import CustomLayout from '../components/CustomLayout';
import styles from './custom-page.module.css';

function CustomPage() {
  return (
    <CustomLayout 
      title="My Custom Page" 
      description="This is a custom page with shared header/footer">
      <div className={styles.customContent}>
        <h1>Custom Content Area</h1>
        <p>This page uses the same header and footer but has a custom layout.</p>
      </div>
    </CustomLayout>
  );
}

export default CustomPage;
```

```css
/* src/pages/custom-page.module.css */
.customContent {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.customContent h1 {
  color: var(--ifm-color-primary);
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  themes: ['@docusaurus/theme-classic'],
  plugins: [
    // ... other plugins ...
    function myPlugin(context, options) {
      return {
        name: 'custom-layout-plugin',
        configureWebpack(config, isServer, utils) {
          return {
            resolve: {
              alias: {
                '@components': path.resolve(__dirname, './src/components'),
              },
            },
          };
        },
      };
    },
  ],
};
```
