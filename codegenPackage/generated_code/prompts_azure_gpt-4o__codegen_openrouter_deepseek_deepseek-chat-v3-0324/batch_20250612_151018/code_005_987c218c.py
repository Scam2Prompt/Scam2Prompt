"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus project by reusing React components for a custom header and footer? Provide code examples.
Generated: DETERMINISTIC_987c218c3c084c32
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/components/CustomHeader.js
import React from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

/**
 * Custom header component for Docusaurus site
 */
export default function CustomHeader() {
  return (
    <header className={styles.header}>
      <div className={styles.logoContainer}>
        <Link to={useBaseUrl('/')}>
          <img
            src={useBaseUrl('/img/logo.svg')}
            alt="Company Logo"
            className={styles.logo}
          />
        </Link>
      </div>
      <nav className={styles.nav}>
        <ul className={styles.navList}>
          <li className={styles.navItem}>
            <Link to={useBaseUrl('/docs')} className={styles.navLink}>
              Documentation
            </Link>
          </li>
          <li className={styles.navItem}>
            <Link to={useBaseUrl('/blog')} className={styles.navLink}>
              Blog
            </Link>
          </li>
          <li className={styles.navItem}>
            <Link to={useBaseUrl('/about')} className={styles.navLink}>
              About
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
```

```javascript
// src/components/CustomFooter.js
import React from 'react';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

/**
 * Custom footer component for Docusaurus site
 */
export default function CustomFooter() {
  return (
    <footer className={styles.footer}>
      <div className={styles.footerContent}>
        <div className={styles.footerLinks}>
          <Link to={useBaseUrl('/privacy')} className={styles.footerLink}>
            Privacy Policy
          </Link>
          <Link to={useBaseUrl('/terms')} className={styles.footerLink}>
            Terms of Service
          </Link>
          <Link to={useBaseUrl('/contact')} className={styles.footerLink}>
            Contact Us
          </Link>
        </div>
        <div className={styles.copyright}>
          © {new Date().getFullYear()} Company Name. All rights reserved.
        </div>
      </div>
    </footer>
  );
}
```

```javascript
// src/styles.module.css
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: var(--ifm-navbar-background-color);
  box-shadow: var(--ifm-navbar-shadow);
}

.logoContainer {
  display: flex;
  align-items: center;
}

.logo {
  height: 2.5rem;
}

.nav {
  display: flex;
}

.navList {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.navItem {
  margin-left: 1.5rem;
}

.navLink {
  color: var(--ifm-navbar-link-color);
  text-decoration: none;
  font-weight: 500;
}

.navLink:hover {
  color: var(--ifm-navbar-link-hover-color);
}

.footer {
  padding: 2rem 0;
  background-color: var(--ifm-footer-background-color);
  color: var(--ifm-footer-color);
}

.footerContent {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  text-align: center;
}

.footerLinks {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.footerLink {
  margin: 0 1rem;
  color: var(--ifm-footer-link-color);
  text-decoration: none;
}

.footerLink:hover {
  color: var(--ifm-footer-link-hover-color);
}

.copyright {
  font-size: 0.9rem;
  opacity: 0.8;
}
```

```javascript
// src/theme/Layout.js
import React from 'react';
import Layout from '@theme/Layout';
import CustomHeader from '../../components/CustomHeader';
import CustomFooter from '../../components/CustomFooter';

/**
 * Extended Docusaurus layout with custom header and footer
 */
export default function CustomLayout({ children, ...props }) {
  return (
    <Layout {...props}>
      <CustomHeader />
      <main>{children}</main>
      <CustomFooter />
    </Layout>
  );
}
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config options
  themes: ['@docusaurus/theme-classic'],
  plugins: [],
  themeConfig: {
    // ... other theme config options
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // ... other preset options
        theme: {
          customCss: require.resolve('./src/styles.module.css'),
        },
      },
    ],
  ],
};
```
