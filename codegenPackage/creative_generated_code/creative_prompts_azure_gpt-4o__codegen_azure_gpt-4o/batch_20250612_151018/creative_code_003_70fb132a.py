"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Write a React-based customization for a Docusaurus website layout, reusing the header and footer components.
Generated: DETERMINISTIC_70fb132abd627ae6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// File: src/components/CustomLayout.js

import React from 'react';
import Layout from '@theme/Layout'; // Default Docusaurus Layout component
import Header from '@theme/Header'; // Docusaurus Header component
import Footer from '@theme/Footer'; // Docusaurus Footer component

// Custom Layout Component
const CustomLayout = ({ children }) => {
  return (
    <Layout>
      {/* Render Header */}
      <Header />

      {/* Custom main content area */}
      <main style={styles.main}>
        {children}
      </main>

      {/* Render Footer */}
      <Footer />
    </Layout>
  );
};

// Inline styles for customization (can be moved to CSS or module styles)
const styles = {
  main: {
    padding: '2rem',
    backgroundColor: '#f9f9f9',
    minHeight: '80vh',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
};

export default CustomLayout;

// Usage Instructions:
// 1. Import `CustomLayout` wherever you need a custom layout.
// 2. Wrap your content with <CustomLayout> ... </CustomLayout>.
```
