"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Provide a code example to extend Docusaurus functionality by adding a custom React component to the site layout.
Generated: DETERMINISTIC_1634017a24cc41f5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from React and Docusaurus
import React from 'react';
import { Layout } from '@theme/Layout';

// Define a custom component
const CustomComponent = () => {
  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Welcome to My Custom Component!</h2>
      <p style={styles.description}>
        This is a custom React component added to the Docusaurus layout.
      </p>
    </div>
  );
};

// Define styles for the custom component
const styles = {
  container: {
    padding: '20px',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
  },
  title: {
    fontSize: '24px',
    marginBottom: '10px',
  },
  description: {
    fontSize: '16px',
  },
};

// Create a higher-order component to extend the Docusaurus layout
const ExtendedLayout = ({ children }) => {
  return (
    <Layout>
      {/* Render the custom component */}
      <CustomComponent />
      {/* Render the existing children (page content) */}
      <main>{children}</main>
    </Layout>
  );
};

// Export the extended layout as default
export default ExtendedLayout;
```

```javascript
// In your Docusaurus config file (docusaurus.config.js), you need to use the ExtendedLayout
module.exports = {
  // Other configurations...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Use the extended layout for the docs
          layout: require.resolve('./src/components/ExtendedLayout'),
        },
        blog: {
          // Use the extended layout for the blog
          layout: require.resolve('./src/components/ExtendedLayout'),
        },
      },
    ],
  ],
};
```
