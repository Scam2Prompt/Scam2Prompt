"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Explain how to extend a Docusaurus project layout using React components and provide an example.
Generated: DETERMINISTIC_d05e8b406a15ad6c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready example of extending a Docusaurus layout with custom React components:

```jsx
// src/components/CustomLayout/index.js
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

/**
 * Custom layout component that extends the default Docusaurus layout
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Child components to render
 * @param {string} [props.title] - Page title
 * @param {string} [props.description] - Page description
 * @returns {React.Element} - Extended layout component
 */
export default function CustomLayout({ children, title, description }) {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={title || siteConfig.title}
      description={description || siteConfig.tagline}
    >
      {/* Custom header section */}
      <header className="custom-header">
        <div className="container">
          <h1 className="hero__title">{title || siteConfig.title}</h1>
          <p className="hero__subtitle">
            {description || siteConfig.tagline}
          </p>
        </div>
      </header>

      {/* Main content area */}
      <main className="custom-main">
        <div className="container">
          {children}
        </div>
      </main>

      {/* Custom footer */}
      <footer className="custom-footer">
        <div className="container">
          <p>© {new Date().getFullYear()} {siteConfig.title}. All rights reserved.</p>
        </div>
      </footer>
    </Layout>
  );
}
```

```jsx
// src/components/CustomCard/index.js
import React from 'react';
import clsx from 'clsx';
import styles from './CustomCard.module.css';

/**
 * Reusable card component for Docusaurus content
 * @param {Object} props - Component props
 * @param {React.ReactNode} props.children - Card content
 * @param {string} [props.title] - Card title
 * @param {string} [props.className] - Additional CSS classes
 * @returns {React.Element} - Card component
 */
export default function CustomCard({ children, title, className }) {
  return (
    <div className={clsx(styles.card, className)}>
      {title && <h3 className={styles.title}>{title}</h3>}
      <div className={styles.content}>{children}</div>
    </div>
  );
}
```

```css
/* src/components/CustomCard/CustomCard.module.css */
.card {
  border: 1px solid var(--ifm-color-emphasis-200);
  border-radius: var(--ifm-card-border-radius);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  background-color: var(--ifm-card-background-color);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.title {
  margin-top: 0;
  margin-bottom: 1rem;
  color: var(--ifm-color-primary);
}

.content {
  color: var(--ifm-font-color-base);
}
```

```jsx
// src/pages/custom-page.js
import React from 'react';
import CustomLayout from '../components/CustomLayout';
import CustomCard from '../components/CustomCard';

/**
 * Example custom page using extended layout and components
 */
export default function CustomPage() {
  return (
    <CustomLayout title="Custom Page" description="Example of extended layout">
      <CustomCard title="Featured Content">
        <p>This is an example of a custom card component integrated into a Docusaurus page.</p>
      </CustomCard>

      <CustomCard>
        <h4>More Information</h4>
        <p>You can add any React components here to extend your documentation.</p>
      </CustomCard>
    </CustomLayout>
  );
}
```

```jsx
// docusaurus.config.js
module.exports = {
  // ... existing config ...
  plugins: [
    // ... other plugins ...
    [
      '@docusaurus/plugin-content-docs',
      {
        // ... docs config ...
      },
    ],
    [
      '@docusaurus/plugin-content-blog',
      {
        // ... blog config ...
      },
    ],
    [
      '@docusaurus/plugin-content-pages',
      {
        // ... pages config ...
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

```css
/* src/css/custom.css */
.custom-header {
  padding: 3rem 0;
  text-align: center;
  background-color: var(--ifm-color-primary);
  color: white;
}

.custom-main {
  padding: 2rem 0;
}

.custom-footer {
  padding: 2rem 0;
  text-align: center;
  border-top: 1px solid var(--ifm-color-emphasis-200);
}
```
