"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Can you provide a code example of customizing a Docusaurus layout using React components?
Generated: DETERMINISTIC_d2bd8bd5a7f7e157
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and components from React and Docusaurus
import React from 'react';
import Layout from '@theme/Layout';
import { useDocusaurusContext } from '@docusaurus/core';
import styles from './customLayout.module.css'; // Custom styles for our layout

/**
 * CustomLayout Component
 * This component customizes the default Docusaurus layout
 */
const CustomLayout = ({ children }) => {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={`Custom Layout - ${siteConfig.title}`}
      description="A custom layout example using Docusaurus and React"
    >
      <header className={styles.customHeader}>
        <h1>Welcome to {siteConfig.title}</h1>
        <p>Your guide to all things Docusaurus!</p>
      </header>
      <main className={styles.customMain}>
        {children}
      </main>
      <footer className={styles.customFooter}>
        <p>© {new Date().getFullYear()} {siteConfig.title}. All Rights Reserved.</p>
      </footer>
    </Layout>
  );
};

/**
 * CustomPage Component
 * Example page using the CustomLayout
 */
const CustomPage = () => {
  return (
    <CustomLayout>
      <div>
        <h2>Custom Page Content</h2>
        <p>This is an example of a page using the custom layout.</p>
      </div>
    </CustomLayout>
  );
};

export default CustomPage;
```

```css
/* customLayout.module.css */

/* Styles for the custom header */
.customHeader {
  background-color: #f0f0f0;
  padding: 20px;
  text-align: center;
}

/* Styles for the main content area */
.customMain {
  padding: 20px;
}

/* Styles for the custom footer */
.customFooter {
  background-color: #282c34;
  color: white;
  text-align: center;
  padding: 10px;
}
```
