"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website using React components while reusing the header and footer? Write the code for a custom layout.
Generated: DETERMINISTIC_563f903e72069cbf
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Docusaurus and React
import React from 'react';
import Layout from '@theme/Layout'; // Default layout provided by Docusaurus
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Provides site-wide context
import clsx from 'clsx'; // Utility for conditional className handling

// Import custom CSS for styling
import styles from './CustomLayout.module.css'; // Ensure CustomLayout.module.css exists in the same directory

// Define a custom layout component
function CustomLayout({ children }) {
  const { siteConfig } = useDocusaurusContext(); // Get site-wide configuration

  return (
    // Extend the default Docusaurus Layout component
    <Layout>
      {/* Add a custom hero section */}
      <header className={clsx('hero-banner', styles.customHero)}>
        <div className="container">
          <h1 className={styles.heroTitle}>
            Welcome to {siteConfig.title}!
          </h1>
          <p className={styles.heroSubtitle}>
            Extend your website layout seamlessly using React!
          </p>
        </div>
      </header>

      {/* Main content section */}
      <main className={styles.customMain}>
        {children}
      </main>
    </Layout>
  );
}

export default CustomLayout;

/*
  Note:
  - Save this file as `src/components/CustomLayout.js` in your Docusaurus project.
  - The `CustomLayout.module.css` file should contain custom styles for `.customHero`, `.heroTitle`, `.heroSubtitle`, and `.customMain`.
  - Use this component to wrap pages or sections where you want to apply the custom layout.
*/
```
