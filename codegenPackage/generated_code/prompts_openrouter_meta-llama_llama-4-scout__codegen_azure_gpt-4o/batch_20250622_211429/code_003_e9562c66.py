"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
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

```jsx
// Import necessary modules and components from React and Docusaurus
import React from 'react';
import Layout from '@theme/Layout'; // Docusaurus Layout component
import useDocusaurusContext from '@docusaurus/useDocusaurusContext'; // Hook to access Docusaurus context
import PropTypes from 'prop-types'; // For prop type validation

// CustomHeader component to override the default header
const CustomHeader = () => {
  return (
    <header style={styles.header}>
      <h1 style={styles.headerTitle}>My Custom Project</h1>
      <nav style={styles.nav}>
        <a href="/" style={styles.navLink}>Home</a>
        <a href="/docs" style={styles.navLink}>Docs</a>
        <a href="/blog" style={styles.navLink}>Blog</a>
      </nav>
    </header>
  );
};

// CustomFooter component to override the default footer
const CustomFooter = () => {
  return (
    <footer style={styles.footer}>
      <p style={styles.footerText}>© {new Date().getFullYear()} My Custom Project. All rights reserved.</p>
      <nav style={styles.footerNav}>
        <a href="/privacy" style={styles.footerLink}>Privacy Policy</a>
        <a href="/terms" style={styles.footerLink}>Terms of Service</a>
      </nav>
    </footer>
  );
};

// Main CustomLayout component that extends the Docusaurus Layout
const CustomLayout = ({ children }) => {
  const { siteConfig } = useDocusaurusContext(); // Access site configuration

  return (
    <Layout>
      {/* Render the custom header */}
      <CustomHeader />
      
      {/* Main content area */}
      <main style={styles.main}>
        {children}
      </main>
      
      {/* Render the custom footer */}
      <CustomFooter />
    </Layout>
  );
};

// Prop type validation for CustomLayout
CustomLayout.propTypes = {
  children: PropTypes.node.isRequired, // Ensure children are passed to the component
};

// Inline styles for the components
const styles = {
  header: {
    backgroundColor: '#282c34',
    color: '#ffffff',
    padding: '1rem',
    textAlign: 'center',
  },
  headerTitle: {
    margin: 0,
    fontSize: '2rem',
  },
  nav: {
    marginTop: '0.5rem',
  },
  navLink: {
    color: '#61dafb',
    margin: '0 1rem',
    textDecoration: 'none',
  },
  main: {
    padding: '2rem',
  },
  footer: {
    backgroundColor: '#20232a',
    color: '#ffffff',
    padding: '1rem',
    textAlign: 'center',
  },
  footerText: {
    margin: 0,
  },
  footerNav: {
    marginTop: '0.5rem',
  },
  footerLink: {
    color: '#61dafb',
    margin: '0 1rem',
    textDecoration: 'none',
  },
};

// Export the CustomLayout component as default
export default CustomLayout;
```
