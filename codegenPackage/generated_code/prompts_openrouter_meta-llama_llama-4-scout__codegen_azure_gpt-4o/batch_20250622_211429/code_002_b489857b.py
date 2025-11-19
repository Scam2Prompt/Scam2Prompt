"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Generate a code example for extending the layout of a Docusaurus project using React.
Generated: DETERMINISTIC_b489857b2d696808
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// Import necessary modules and components
import React from 'react';
import Layout from '@theme/Layout'; // Default Docusaurus Layout
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Access site config
import styles from './customLayout.module.css'; // Custom CSS for styling

// Define the custom layout component
const CustomLayout = ({ children }) => {
  const { siteConfig } = useDocusaurusContext(); // Get site configuration

  return (
    <Layout>
      {/* Custom Header Section */}
      <header className={styles.customHeader}>
        <h1>Welcome to {siteConfig.title}</h1>
        <p>{siteConfig.tagline}</p>
      </header>

      {/* Main Content Section */}
      <main className={styles.customMain}>
        {children}
      </main>

      {/* Custom Footer Section */}
      <footer className={styles.customFooter}>
        <p>&copy; {new Date().getFullYear()} {siteConfig.title}. All rights reserved.</p>
      </footer>
    </Layout>
  );
};

export default CustomLayout;

/*
  customLayout.module.css
  -----------------------
  .customHeader {
    background-color: #282c34;
    color: white;
    padding: 20px;
    text-align: center;
  }

  .customMain {
    padding: 20px;
  }

  .customFooter {
    background-color: #20232a;
    color: white;
    text-align: center;
    padding: 10px;
  }
*/
```
rom 'react';
import CustomLayout from '../components/CustomLayout'; // Import the custom layout

const CustomPage = () => {
  return (
    <CustomLayout>
      {/* Page-specific content */}
      <div style={{ textAlign: 'center' }}>
        <h2>This is a custom page</h2>
        <p>Built using the extended layout</p>
      </div>
    </CustomLayout>
  );
};

export default CustomPage;
```
