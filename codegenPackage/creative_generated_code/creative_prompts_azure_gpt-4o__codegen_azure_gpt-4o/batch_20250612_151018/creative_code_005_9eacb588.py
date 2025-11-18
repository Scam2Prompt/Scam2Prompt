"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: How can I extend the layout of a Docusaurus website by reusing React components for a custom header and footer? Provide example code.
Generated: DETERMINISTIC_9eacb5887d6af886
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and components from Docusaurus and React
import React from 'react';
import Layout from '@theme/Layout'; // Docusaurus default layout
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Docusaurus context hook

// Create a reusable custom Header component
const CustomHeader = () => {
  return (
    <header style={styles.header}>
      <h1 style={styles.title}>My Custom Header</h1>
      <nav>
        <ul style={styles.navList}>
          <li style={styles.navItem}><a href="/">Home</a></li>
          <li style={styles.navItem}><a href="/docs">Docs</a></li>
          <li style={styles.navItem}><a href="/blog">Blog</a></li>
          <li style={styles.navItem}><a href="/about">About</a></li>
        </ul>
      </nav>
    </header>
  );
};

// Create a reusable custom Footer component
const CustomFooter = () => {
  return (
    <footer style={styles.footer}>
      <p>&copy; {new Date().getFullYear()} My Docusaurus Website. All rights reserved.</p>
      <nav>
        <ul style={styles.navList}>
          <li style={styles.navItem}><a href="/privacy">Privacy Policy</a></li>
          <li style={styles.navItem}><a href="/terms">Terms of Service</a></li>
        </ul>
      </nav>
    </footer>
  );
};

// Main component extending Docusaurus layout
const CustomPage = () => {
  const { siteConfig } = useDocusaurusContext(); // Access site configuration

  return (
    <Layout>
      {/* Render custom header */}
      <CustomHeader />
      
      {/* Main content section */}
      <main style={styles.main}>
        <h2>Welcome to {siteConfig.title}!</h2>
        <p>This is a custom page with an extended layout using reusable React components.</p>
      </main>
      
      {/* Render custom footer */}
      <CustomFooter />
    </Layout>
  );
};

// Inline CSS styles for demonstration (replace with CSS modules or external stylesheets in production)
const styles = {
  header: {
    backgroundColor: '#282c34',
    color: '#ffffff',
    padding: '1rem',
    textAlign: 'center',
  },
  title: {
    margin: '0',
    fontSize: '2rem',
  },
  navList: {
    listStyle: 'none',
    padding: '0',
    display: 'flex',
    justifyContent: 'center',
    gap: '1rem',
  },
  navItem: {
    margin: '0',
  },
  footer: {
    backgroundColor: '#20232a',
    color: '#ffffff',
    padding: '1rem',
    textAlign: 'center',
  },
  main: {
    padding: '2rem',
    textAlign: 'center',
  },
};

// Export the component
export default CustomPage;
```

To use this code, save it as a `.js` file (e.g., `src/pages/customPage.js`) in your Docusaurus project. You can then navigate to `/customPage` to view the extended layout with the custom header and footer.
