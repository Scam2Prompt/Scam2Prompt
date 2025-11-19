"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Create a React component that extends the Docusaurus layout and customizes the header and footer for a project.
Generated: DETERMINISTIC_e9562c662d3e3171
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

interface CustomLayoutProps {
  title?: string;
  description?: string;
  children: React.ReactNode;
}

const CustomLayout: React.FC<CustomLayoutProps> = ({
  title,
  description,
  children,
}) => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={title}
      description={description ?? siteConfig.tagline}
    >
      <header className={styles.header}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/docs/intro"
            >
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>{children}</main>
      <footer className={styles.footer}>
        <div className="container">
          <div className="row">
            <div className="col col--6">
              <h3>Resources</h3>
              <ul>
                <li>
                  <Link to="/docs">Documentation</Link>
                </li>
                <li>
                  <Link to="/blog">Blog</Link>
                </li>
                <li>
                  <Link to="/community">Community</Link>
                </li>
              </ul>
            </div>
            <div className="col col--6">
              <h3>Legal</h3>
              <ul>
                <li>
                  <Link to="/privacy">Privacy Policy</Link>
                </li>
                <li>
                  <Link to="/terms">Terms of Service</Link>
                </li>
              </ul>
            </div>
          </div>
          <div className={styles.copyright}>
            <p>
              © {new Date().getFullYear()} {siteConfig.title}. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </Layout>
  );
};

export default CustomLayout;
```
 #a777e3);
  color: white;
}

.customFooter {
  padding: 2rem 0;
  border-top: 1px solid #eaeaea;
  background-color: #f5f5f5;
}

@media screen and (max-width: 996px) {
  .customHeader {
    padding: 2rem 0;
  }
  
  .customFooter .row {
    flex-direction: column;
    text-align: center;
  }
  
  .customFooter .col.text--right {
    text-align: center;
    margin-top: 1rem;
  }
}
```
