"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: Can you provide a code example of customizing a Docusaurus layout using React components?
Generated: DETERMINISTIC_d2bd8bd5a7f7e157
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://docusaurus.io/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules and components from Docusaurus and React
import React from 'react';
import Layout from '@theme/Layout'; // Default Layout from Docusaurus
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Hook to access site config
import styles from './customLayout.module.css'; // Custom CSS module for styling

// Custom Header Component
function CustomHeader() {
  return (
    <header className={styles.customHeader}>
      <h1>Welcome to My Custom Docusaurus Site</h1>
      <p>Explore the power of documentation with style!</p>
    </header>
  );
}

// Custom Footer Component
function CustomFooter() {
  return (
    <footer className={styles.customFooter}>
      <p>© {new Date().getFullYear()} My Custom Site</p>
      <p>
        Built with <a href="https://docusaurus.io/">Docusaurus</a>
      </p>
    </footer>
  );
}

// Main Custom Layout Component
export default function CustomLayout({ children }) {
  const { siteConfig } = useDocusaurusContext(); // Access site configuration

  return (
    <Layout
      title={siteConfig.title} // Set the page title dynamically
      description={siteConfig.tagline} // Set the page description dynamically
    >
      {/* Render the custom header */}
      <CustomHeader />

      {/* Main content area */}
      <main className={styles.mainContent}>
        {children} {/* Render child components passed to Layout */}
      </main>

      {/* Render the custom footer */}
      <CustomFooter />
    </Layout>
  );
}

/*
 * customLayout.module.css
 *
 * .customHeader {
 *   background-color: #282c34;
 *   color: white;
 *   padding: 2rem;
 *   text-align: center;
 * }
 *
 * .mainContent {
 *   padding: 2rem;
 * }
 *
 * .customFooter {
 *   background-color: #f8f9fa;
 *   color: #6c757d;
 *   text-align: center;
 *   padding: 1rem;
 * }
 */
```
